from gub import target

class Xextproto (target.AutoBuild):
    source = 'http://xorg.freedesktop.org/archive/individual/proto/xextproto-7.3.0.tar.bz2'
    #source = 'http://xorg.freedesktop.org/releases/X11R7.4/src/proto/xextproto-7.0.3.tar.gz'
    dependencies = ['tools::libtool']
