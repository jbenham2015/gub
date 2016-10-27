from gub import target

class Libxfixes (target.AutoBuild):
    source = 'http://pkgs.fedoraproject.org/repo/pkgs/libXfixes/libXfixes-5.0.1.tar.bz2/b985b85f8b9386c85ddcfe1073906b4d/libXfixes-5.0.1.tar.bz2'
    dependencies = ['tools::libtool', 'fixesproto-devel', 'libx11-devel', 'libxau-devel', 'libxdmcp-devel']
