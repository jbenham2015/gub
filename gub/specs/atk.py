from gub import gnome
from gub import target

class Atk (target.AutoBuild):
    source = 'http://ftp.gnome.org/pub/gnome/sources/atk/2.16/atk-2.16.0.tar.xz'
    dependencies = ['tools::libtool', 'glib-devel']

class Atk__mingw (Atk):
    patches = [
        #'atk-mingw.patch',
        ]
    #def patch (self):
        #target.AutoBuild.patch (self)
        #self.file_sub ([('\$\(srcdir\)/atk.def', 'atk.def')], '%(srcdir)s/atk/Makefile.in', must_succeed=True)

from gub import build
class Atk__darwin (build.BinaryBuild, build.SdkBuild):
    #dependencies = ['tools::glib', 'tools::libtool', 'gettext-devel', 'zlib', 'libffi']
    source = 'http://www.denemo.org/downloads/gub/atk.zip'
    def untar (self):
        build.BinaryBuild.untar (self)
        self.system ('''
cd  %(srcdir)s/ && ls && mkdir usr && mv opt/local/include opt/local/lib opt/local/share usr/
''')


