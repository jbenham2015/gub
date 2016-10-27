from gub import target
from gub import tools

class Libffi (target.AutoBuild):
<<<<<<< HEAD
    source = 'ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz'
    patches = [ 'libffi-3.2.1-includedir.patch', ]
=======
    source = 'ftp://sourceware.org/pub/libffi/libffi-3.0.13.tar.gz'
>>>>>>> fe5abd652386985530dc1142f1e7a5657e6d6e58
    dependencies = [
        'tools::automake',
        'tools::libtool',
        'tools::pkg-config',
        ]
<<<<<<< HEAD

class Libffi__linux__64 (Libffi):
    # For using /usr/lib instead of /usr/lib64
    patches = Libffi.patches + [
        'libffi-3.2.1-linux-64-libdir.patch',
    ]

class Libffi__darwin__x86 (Libffi):
    # darwin-x86 can not compile libffi 3.1, 3.2.1.
    source = 'ftp://sourceware.org/pub/libffi/libffi-3.0.13.tar.gz'
    patches = [ 'libffi-3.0.13-includedir.patch', ]

class Libffi__tools (tools.AutoBuild, Libffi):
    pass
=======
    # huh?
    install_flags = (target.AutoBuild.install_flags
                     + """ includesdir='$(includedir)' """ )
    def install (self):
        target.AutoBuild.install (self)
        self.system ('cd %(install_prefix)s && mv lib/libffi-3.0.13/include .')
        self.system ('cd %(install_prefix)s && rm -rf lib/libffi-3.0.13')
                
class Libffi__tools (tools.AutoBuild, Libffi):
    dependencies = [
        'automake',
        'libtool',
        'pkg-config',
        ]
    # huh?
    install_flags = (tools.AutoBuild.install_flags
                     + """ includesdir='$(includedir)' """ )
    def install (self):
        tools.AutoBuild.install (self)
        self.system ('cd %(install_prefix)s && mv lib/libffi-3.0.13/include .')
        self.system ('cd %(install_prefix)s && rm -rf lib/libffi-3.0.13')
>>>>>>> fe5abd652386985530dc1142f1e7a5657e6d6e58
