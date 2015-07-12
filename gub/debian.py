import os
import re
import new
#
from gub.syntax import printf
from gub import build
from gub import context
from gub import cross
from gub import misc

mirror = 'http://ftp.de.debian.org/debian'

# http://ftp.de.debian.org/debian/pool/main/l/linux-kernel-headers/

gcc_version = '4.8.2'
glibc_version='2.3.2.ds1-22sarge4'
linux_version = '2.5.999-test7-bk-17'
def get_cross_build_dependencies (settings):
    global gcc_version, glibc_version, linux_version
    #FIXME too late
    gcc_version = '4.8.2'
    if settings.debian_branch == 'stable':
        glibc_version='2.3.2.ds1-22sarge4'
        linux_version = '2.5.999-test7-bk-17'
    else:
        glibc_version='2.3.6.ds1-9'
        linux_version = '2.6.18-6'
    return ['cross/gcc', 'guile-config', 'python-config']

def change_target_package (p):
    cross.change_target_package (p)

def get_debian_packages (settings, package_file):
    printf ('parsing: %s...' % package_file)
    return [get_debian_package (settings, j) for j in open (package_file).read ().split ('\n\n')[:-1]]

def get_debian_package (settings, description):
    s = description[:description.find ('\nDescription')]
    d = dict ([line.split (': ', 1) for line in list (map (''.strip, s.split ('\n')))])
    # FIXME: should blacklist toplevel bin/gub argument iso lilypond
    blacklist = [
        'binutils',
        'cpp',
        'gcc-3.3',
        'cpp-3.3',
        'gcc',
        'gcc-3.4',
        'libgcc1',
        'libgcc1-3.4',
        'lilypond',
        'libstdc++6',
        'libstdc++-dev',
        'libtool',
        'perl',
        'perl-modules',
        'perl-base',
#        'pkg-config',
        ]
    if d['Package'] in blacklist:
        d['Package'] += '::blacklisted'
    package_class = new.classobj (d['Package'], (build.BinaryBuild,), {})
    from gub import repository
    source = repository.DebianPackage (settings.downloads + '/Debian/' + settings.debian_branch,
                                       os.path.join (mirror, d['Filename']),
                                       d['Version'])
    package = package_class (settings, source)
    package.name_dependencies = []
    if 'Depends' in d:
        deps = list (map (''.strip,
                    re.sub ('\([^\)]*\)', '', d['Depends']).split (', ')))
        # FIXME: BARF, ignore choices
        deps = [x for x in deps if x.find ('|') == -1]
        # FIXME: how to handle Provides: ?
        # FIXME: BARF, fixup libc Provides
        deps = [re.sub ('libc($|-)', 'libc6\\1', x) for x in deps]
        deps = [re.sub ('liba52-dev', 'liba52-0.7.4-dev', x) for x in deps]
        deps = [re.sub ('libpng12-0-dev', 'libpng12-dev', x) for x in deps]
        # FIXME: ugh, skip some
        deps = [x for x in deps if x not in blacklist]
        package.name_dependencies = deps

    def get_build_dependencies (self):
        return self.name_dependencies
    package.get_build_dependencies = misc.bind_method (get_build_dependencies,
                                                       package)
    pkg_name = d['Package']
    @context.subst_method
    def name (self):
        return pkg_name
    message = 'FIXME: enter .name into package_class; see cygwin.py'
    printf (message)
    raise Exception (message)
    package.name = misc.bind_method (name, package)
    context.subst_method (package.name)
    return package

## FIXME: c&p cygwin.py
class Dependency_resolver:
    def __init__ (self, settings, todo):
        self.settings = settings
        self.packages = {}
        self.source = todo
        self.load_packages ()

    def grok_packages_file (self, file):
        for p in get_debian_packages (self.settings, file):
            self.package_fixups (p)
            self.packages[p.name ()] = p

    def package_fixups (self, package):
        if package.name () == 'libqt4-dev':
            def untar (whatsthis):
                build.BinaryBuild.untar (package)
                for i in ('QtCore.pc', 'QtGui.pc', 'QtNetwork.pc'):
                    package.file_sub ([
                            ('includedir', 'deepqtincludedir'),
                            ('(-I|-L) */usr',
                             '''\\1%(system_prefix)s''' % locals ()),
                            ],
                                      '%(srcdir)s/usr/lib/pkgconfig/%(i)s',
                                      env=locals ())
            package.untar = misc.MethodOverrider (package.untar, untar)

    def load_packages (self):
        from gub import gup
        p = gup.DependencyManager (self.settings.system_root)
#        arch = settings.platform
#        if settings.platform == 'debian':
#            arch = 'i386'
        arch = self.settings.package_arch
        branch = self.settings.debian_branch
        packages_path = '/dists/%(branch)s/main/binary-%(arch)s/Packages.gz' \
                        % locals ()
        url = mirror + packages_path
        dir = self.settings.downloads + '/Debian'
        os.system ('mkdir -p %(dir)s' % locals ())
        base = dir + '/Packages'
        file = '.'.join ((base, arch, branch))

        # FIXME: download/offline update
        if not os.path.exists (file):
            misc.download_url (url, dir,
                               local=['file://' + self.settings.downloads + '/Debian'],
                               )
            os.system ('gunzip  %(base)s.gz' % locals ())
            os.system ('mv %(base)s %(file)s' % locals ())
        self.grok_packages_file (file)

    def get_packages (self):
        return self.packages
        
dependency_resolver = None

def init_dependency_resolver (settings, todo):
    global dependency_resolver
    dependency_resolver = Dependency_resolver (settings, todo)

def debian_name_to_dependency_names (name):
    return dependency_resolver.get_dependencies (name)

def get_packages ():
    return dependency_resolver.get_packages ()

#FIXME: stable/unstable?
gub_to_distro_dict = {
    'fontconfig' : ['libfontconfig1'],
    'fontconfig-devel' : ['libfontconfig1-dev'],
    'freetype' : ['libfreetype6'],
    'freetype-devel' : ['libfreetype6-dev'],
    'gettext' : ['gettext'],
    'gettext-devel' : ['gettext'],
    'gmp-devel': ['libgmp3-dev'],
    'gmp-runtime': ['libgmp3'],
    'ghostscript': ['gs'],
    'guile-devel' : ['guile-1.8-dev'],
    'guile-runtime' : ['guile-1.8-libs'],
    'libtool-runtime': ['libltdl3'],
    'libiconv-devel': ['libiconv2'],
    'pango': ['libpango1.0-0'],
    'python-devel': ['python2.6-dev'],
    'python-runtime': ['python2.6'],
    }
