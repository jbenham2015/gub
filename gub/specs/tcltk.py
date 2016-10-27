from gub import context
from gub import target
 
class Tcltk (target.AutoBuild):
    source = 'http://lilypond.org/downloads/gub-sources/tcltk-8.4.14.tar.gz'
    parallel_build_broken = True
    license_files = ['%(srcdir)s/tcl/license.terms']
    def configure (self):
        self.system ('''cd %(srcdir)s/tcl &&  ./unix/configure --prefix=%(install_prefix)s
cd %(srcdir)s/tk/ && ./unix/configure --prefix=%(install_prefix)s
''')
    def compile (self):
        self.system ('cd %(builddir)s/tcl && make')
        self.system ('cd %(builddir)s/tk && make')
    def patch (self):
        self.system ("cd %(srcdir)s/tcl/ && patch -p1 < %(patchdir)s/tcl-8.4.14-dde.patch")
    def install (self):
        self.system ('cd %(builddir)s/tcl && make DESTDIR=%(install_root)s install')
        self.system ('cd %(builddir)s/tk && make DESTDIR=%(install_root)s install')
    def get_subpackage_definitions (self):
        s = target.AutoBuild.get_subpackage_definitions (self)
        s['doc'].append (self.settings.prefix_dir + '/lib/tk8.4/demos')
        return s
    
class Tcltk__mingw (Tcltk):
    @context.subst_method
    def RC (self):
        return  '%(cross_prefix)s/bin/%(target_architecture)s-windres'
    def configure (self):
        self.system ('''mkdir -p %(builddir)s/tcl  %(builddir)s/tk ''')
        self.system ('''cd %(builddir)s/tcl &&  %(srcdir)s/tcl/win/configure --prefix=%(install_prefix)s
cd %(builddir)s/tk/ && %(srcdir)s/tk/win/configure --prefix=%(install_prefix)s --with-tcl=%(builddir)s/tcl/
''')
