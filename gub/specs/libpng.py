from gub import target
from gub import tools 

class Libpng (target.AutoBuild):
     source = 'http://sourceforge.net/projects/libpng/files/libpng16/1.6.17/libpng-1.6.17.tar.gz'
     dependencies = ['zlib-devel', 'tools::autoconf', 'tools::automake', 'tools::libtool']
     def name (self):
         return 'libpng'
   
class Libpng__tools (tools.AutoBuild, Libpng):
    dependencies = ['libtool']
    def patch (self):
        Libpng.patch (self)
