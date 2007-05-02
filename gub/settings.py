import os
import re
from gub import oslog
from gub import distcc
from gub import gubb

from context import *

platforms = {
    'debian-arm': 'arm-linux',
    'cygwin': 'i686-cygwin',
    'darwin-ppc': 'powerpc-apple-darwin7',
    'darwin-x86': 'i686-apple-darwin8',
    'debian': 'i686-linux',
    'freebsd-x86': 'i686-freebsd4',
    
    'freebsd4-x86': 'i686-freebsd4',
    'freebsd6-x86': 'i686-freebsd6',
    'linux-arm-softfloat': 'armv5te-softfloat-linux',
    'linux-arm-vfp': 'arm-linux',
    'linux-x86': 'i686-linux',
    'linux-64': 'x86_64-linux',
    'linux-ppc': 'powerpc-linux',
    'local': 'local',
    'mingw': 'i686-mingw32',
    'mipsel': 'mipsel-linux',
}

distros = ('debian-arm', 'cygwin', 'debian', 'mipsel')
            
class Settings (Context):
    def __init__ (self, options):
        Context.__init__ (self)
        self.platform = options.platform

        if self.platform not in platforms.keys ():
            raise 'unknown platform', self.platform
        
        self.target_gcc_flags = '' 
        if self.platform == 'darwin-ppc':
            self.target_gcc_flags = '-D__ppc__'
        elif self.platform == 'mingw':
            self.target_gcc_flags = '-mwindows -mms-bitfields'

        self.set_branches (options.branches)
        self.build_source = options.build_source
        self.cpu_count = options.cpu_count
        self.set_distcc_hosts (options)
        self.lilypond_versions = options.lilypond_versions
        self.options = options ##ugh

        #urg
        self.verbose = self.options.verbose
    
        self.os = re.sub ('[-0-9].*', '', self.platform)
    
        self.target_architecture = platforms[self.platform]
        self.cpu = self.target_architecture.split ('-')[0]
        self.build_source = False
        self.is_distro = self.platform in distros

        self.topdir = os.getcwd ()
        self.logdir = self.topdir + '/log'
        self.downloads = self.topdir + '/downloads'
        self.patchdir = self.topdir + '/patches'
        self.sourcefiledir = self.topdir + '/sourcefiles'
        # FIXME: absolute path
        self.specdir = self.topdir + '/gub/specs'
        self.nsisdir = self.topdir + '/nsis'
        self.gtk_version = '2.8'

        self.tool_prefix = self.target_architecture + '-'
        self.system_root = self.topdir + '/target/' + self.platform
        self.targetdir = self.system_root + '/gubfiles'

        ## Patches are architecture dependent, 
        ## so to ensure reproducibility, we unpack for each
        ## architecture separately.
        self.allsrcdir = os.path.join (self.targetdir, 'src')
        
        self.allbuilddir = self.targetdir + '/build'
        self.statusdir = self.targetdir + '/status'

        ## Safe uploads, so that we can rm -rf target/*
        ## and still cheaply construct a (partly) system root
        ## from .gub packages.
        self.uploads = self.topdir + '/uploads'
        self.gub_uploads = self.uploads + '/' + self.platform

        # Hmm, change `cross/' to `cross.' or `cross-' in name?
        self.cross_gub_uploads = self.gub_uploads + '/cross'
        self.cross_allsrcdir = self.allsrcdir + '/cross'
        self.cross_statusdir = self.statusdir + '/cross'

        self.distcc_hosts = ''
        
        self.core_prefix = self.system_root + '/usr/cross/core'
        # FIXME: rename to target_root?
        self.cross_prefix = self.system_root + '/usr/cross'
        self.installdir = self.targetdir + '/install'
        self.local_prefix = self.topdir + '/target/local/usr'
        self.cross_distcc_bindir = self.topdir + '/target/cross-distcc/bin'
        self.native_distcc_bindir = self.topdir + '/target/native-distcc/bin'
        
	if self.target_architecture.startswith ('x86_64'):
	    self.package_arch = 'amd64'
            self.debian_branch = 'unstable'
	else:
            self.package_arch = re.sub ('-.*', '', self.target_architecture)
            self.package_arch = re.sub ('i[0-9]86', 'i386', self.package_arch)
            self.package_arch = re.sub ('arm.*', 'arm', self.package_arch)
#            self.package_arch = re.sub ('powerpc.*', 'ppc', self.package_arch)
            self.debian_branch = 'stable'
        
        self.keep_build = False
        self.use_tools = False
        self.build_autopackage = self.allbuilddir + '/autopackage'

        if not os.path.isdir ('log'):
            os.mkdir ('log')
            
        self.os_interface = oslog.Os_commands ('log/build-%s.log'
                                               % self.target_architecture,
                                               self.options.verbose)
        self.create_dirs ()
        self.build_architecture = self.os_interface.read_pipe ('gcc -dumpmachine',
                                                               silent=True)[:-1]

        try:
            self.cpu_count_str = '%d' % os.sysconf ('SC_NPROCESSORS_ONLN')
        except ValueError:
            self.cpu_count_str = '1'

        ## make sure we don't confuse build or target system.
        self.LD_LIBRARY_PATH = '%(system_root)s/'
        
    def create_dirs (self): 
        for a in (
            'downloads',
            'logdir',
            'gub_uploads',
            'specdir',
            'allsrcdir',
            'statusdir',
            'system_root',
            'core_prefix',
            'cross_prefix',
            'targetdir',
            'local_prefix',
            'topdir',

            'cross_gub_uploads',
            'cross_statusdir',
            'cross_allsrcdir',
            ):
            dir = self.__dict__[a]
            if os.path.isdir (dir):
                continue

            self.os_interface.system ('mkdir -p %s' % dir)


    def set_distcc_hosts (self, options):
        def hosts (xs):
            return reduce (lambda x,y: x+y,
                           [ h.split (',') for h in xs], [])
        
        self.cross_distcc_hosts = ' '.join (distcc.live_hosts (hosts (options.cross_distcc_hosts)))

        self.native_distcc_hosts = ' '.join (distcc.live_hosts (hosts (options.native_distcc_hosts), port=3634))



    def set_branches (self, bs):
        "set branches, takes a list of name=branch strings."

        self.branch_dict = {}
        for b in bs:
            (name, br) = tuple (b.split ('='))

            self.branch_dict[name] = br
            self.__dict__['%s_branch' % name]= br
