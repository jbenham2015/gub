from gub import gnome
from gub import misc
from gub import tools
from gub import target

class Glib (target.AutoBuild):
<<<<<<< HEAD
    source = 'http://ftp.gnome.org/pub/GNOME/sources/glib/2.44/glib-2.44.1.tar.xz'
    dependencies = ['tools::glib', 'tools::libtool', 'tools::xzutils', 'gettext-devel', 'zlib-devel', 'libffi-devel', ]
=======
    #source = 'http://ftp.gnome.org/pub/GNOME/sources/glib/2.30/glib-2.30.3.tar.xz'
    source = 'http://ftp.gnome.org/pub/GNOME/sources/glib/2.43/glib-2.43.4.tar.xz'
    dependencies = ['tools::glib', 'tools::libtool', 'gettext-devel', 'zlib', 'libxml2', 'libffi']
    #patches = ['glib-2.27.ZLIB_VERNUM.patch']
>>>>>>> fe5abd652386985530dc1142f1e7a5657e6d6e58
    config_cache_overrides = target.AutoBuild.config_cache_overrides + '''
glib_cv_stack_grows=${glib_cv_stack_grows=no}
glib_cv_long_long_format=${glib_cv_long_long_format=I64}
'''
<<<<<<< HEAD
=======
    if 'stat' in misc.librestrict (): # stats for /USR/include/glib/...
        install_flags = (target.AutoBuild.install_flags
                         + ' LD_PRELOAD=%(tools_prefix)s/lib/librestrict-open.so')
    #def patch (self):
        #target.AutoBuild.patch (self)
        #self.file_sub ([('GIO_MODULE_DIR', 'getenv ("GIO_MODULE_DIR")')],
         #              '%(srcdir)s/gio/giomodule.c', must_succeed=True)
    def update_libtool (self): # linux-x86, linux-ppc, freebsd-x86
        target.AutoBuild.update_libtool (self)
        self.map_locate (w32.libtool_disable_relink, '%(builddir)s', 'libtool')
        #URGME, 2.19.5: relinking libgio is broken, /usr/lib is inserted
        '''root/usr/lib/usr/lib -L/usr/lib -lgobject-2.0 -L/home/janneke/vc/gub/target/linux-ppc/install/glib-2.19.5-root/usr/lib/home/janneke/vc/gub/target/linux-ppc/build/glib-2.19.5/gmodule/.libs -lgmodule-2.0 -ldl -lglib-2.0    -Wl,-soname -Wl,libgio-2.0.so.0 -Wl,-version-script -Wl,.libs/libgio-2.0.ver -o .libs/libgio-2.0.so.0.1905.0
/home/janneke/vc/gub/target/linux-ppc/root/usr/cross/bin/powerpc-linux-ld: skipping incompatible /usr/lib/libgobject-2.0.so when searching for -lgobject-2.0
/home/janneke/vc/gub/target/linux-ppc/root/usr/cross/bin/powerpc-linux-ld: skipping incompatible /usr/lib/libgobject-2.0.a when searching for -lgobject-2.0
/home/janneke/vc/gub/target/linux-ppc/root/usr/cross/bin/powerpc-linux-ld: cannot find -lgobject-2.0
collect2: ld returned 1 exit status
libtool: install: error: relink `libgio-2.0.la' with the above command before installing it
make[5]: *** [install-libLTLIBRARIES] Error 1
'''
>>>>>>> fe5abd652386985530dc1142f1e7a5657e6d6e58
    def install (self):
        target.AutoBuild.install (self)
        self.system ('rm -f %(install_prefix)s/lib/charset.alias')

class Glib__darwin (Glib):
    # Darwin 8 SDK (Mac OS X 10.4) can not compile glib 2.45.3+.
    # It needs OS X 10.9.
    patches = Glib.patches + ['glib-2.44.1-darwin-in.patch']
    def configure (self):
        Glib.configure (self)
<<<<<<< HEAD
        self.file_sub ([('-Werror=format=2', '')],
                       '%(builddir)s/glib/Makefile')
        self.file_sub ([('-Werror=declaration-after-statement', '')],
                       '%(builddir)s/gio/Makefile')

class Glib__darwin__x86 (Glib__darwin):
    patches = Glib__darwin.patches + [
        'glib-2.44.1-darwin-x86-lib-depend.patch',
        'glib-2.44.1-darwin-x86-zlib.patch',
    ]
    def patch (self):
        Glib__darwin.patch (self)
        # darwin-x86 inline asm seems broken.
        self.file_sub ([('#define USE_ASM_GOTO 1', '')],
                       '%(srcdir)s/glib/gbitlock.c')

=======
        self.file_sub ([('nmedit', '%(target_architecture)s-nmedit')],
                       '%(builddir)s/libtool')
    #patches = ['patches/glib-2.27.ZLIB_VERNUM.patch']
class Glib__linux__x86 (Glib):
    config_cache_overrides = target.AutoBuild.config_cache_overrides + '''
glib_cv_stack_grows=${glib_cv_stack_grows=no}
'''

class Glib__darwin__x86 (Glib__darwin):
    source = 'http://ftp.gnome.org/pub/GNOME/sources/glib/2.38/glib-2.38.2.tar.xz'
    patches = ['glib-2.43.mac-patch', 'glib-2.38-ZLIB_VERNUM.patch']
    config_cache_overrides = target.AutoBuild.config_cache_overrides + '''
glib_cv_stack_grows=${glib_cv_stack_grows=no}
'''
 
    configure_flags = (Glib.configure_flags
		       + ' --disable-compile-warnings'
		       + ' --disable-maintainer-mode' 
		       + ' --disable-silent-rules' 
		       + ' --disable-dtrace' 
		       + ' --disable-modular-tests'
                       )
       
>>>>>>> fe5abd652386985530dc1142f1e7a5657e6d6e58
class Glib__mingw (Glib):
    patches = Glib.patches + [
        'glib-2.44.1-mingw-w64-if_nametoindex.patch',
    ]
    dependencies = Glib.dependencies + ['libiconv-devel']
<<<<<<< HEAD
    def configure (self):
        Glib.configure (self)
        self.file_sub ([('-Werror=format=2', ''),
                        ('-Werror=format-extra-args', ''),],
                       '%(builddir)s/glib/Makefile')
        self.file_sub ([('-Werror=format=2', ''),
                        ('-Werror=format-extra-args', ''),],
                       '%(builddir)s/gobject/Makefile')
        self.file_sub ([('-Werror=format=2', ''),
                        ('-Werror=format-extra-args', ''),],
                       '%(builddir)s/gio/Makefile')
=======
    def update_libtool (self): # linux-x86, linux-ppc, freebsd-x86
        #target.AutoBuild.update_libtool (self)
        self.map_locate (w32.libtool_disable_relink, '%(builddir)s', 'libtool')
>>>>>>> fe5abd652386985530dc1142f1e7a5657e6d6e58

class Glib__freebsd (Glib):
    dependencies = Glib.dependencies + ['libiconv-devel']
    # FreeBSD 6 can not compile glib 2.40.0+. It needs FreeBSD 8.1.
    source = 'http://ftp.gnome.org/pub/GNOME/sources/glib/2.38/glib-2.38.2.tar.xz'

class Glib__tools (tools.AutoBuild, Glib):
    dependencies = [
            #'gettext',
            'libtool',
            'pkg-config',
<<<<<<< HEAD
            'zlib',
            'libffi',
            'xzutils',
=======
	    'libffi'
>>>>>>> fe5abd652386985530dc1142f1e7a5657e6d6e58
            ]            
    def install (self):
        tools.AutoBuild.install (self)
        self.system ('rm -f %(install_root)s%(packaging_suffix_dir)s%(prefix_dir)s/lib/charset.alias')
