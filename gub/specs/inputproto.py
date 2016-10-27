from gub import target

class Inputproto (target.AutoBuild):
    source = 'http://pkgs.fedoraproject.org/repo/pkgs/xorg-x11-proto-devel/inputproto-2.3.1.tar.bz2/6caebead4b779ba031727f66a7ffa358/inputproto-2.3.1.tar.bz2'
#    source = 'http://xorg.freedesktop.org/releases/X11R7.4/src/everything/inputproto-1.4.4.tar.gz'
    dependencies = ['tools::libtool']
