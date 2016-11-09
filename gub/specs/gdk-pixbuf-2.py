from gub import gnome
from gub import target

class Gdk_pixbuf_2 (target.AutoBuild):
#    source = 'http://ftp.gnome.org/pub/GNOME/platform/2.32/2.32.1/sources/gdk-pixbuf-2.22.1.tar.gz'
#    patches = ['gdk-pixbuf-mmx.patch']
    source = 'http://ftp.acc.umu.se/pub/GNOME/sources/gdk-pixbuf/2.31/gdk-pixbuf-2.31.3.tar.xz'
    dependencies = ['tools::libtool', 'tools::glib', 'libtiff-devel', 'libpng', 'libjpeg-devel']
    #patches = ['gdk-pixbuf-2.28.2-no-gio-sniff.patch']

    configure_flags = (target.AutoBuild.configure_flags
			   + ' --disable-glibtest'
			   + ' --enable-introspection=no'
			   + ' --disable-introspection'
			   + ' --enable-gdiplus'
			   + ' --disable-modules'
			   + ' --disable-dependency-tracking'
				)
class Gdk_pixbuf_2__mingw(target.AutoBuild):
    source = 'http://ftp.acc.umu.se/pub/GNOME/sources/gdk-pixbuf/2.30/gdk-pixbuf-2.30.8.tar.xz'
#    source = 'http://ftp.gnome.org/pub/GNOME/sources/gdk-pixbuf/2.24/gdk-pixbuf-2.24.0.tar.bz2'
    dependencies = ['tools::libtool', 'tools::glib', 'libtiff-devel', 'libpng', 'libjpeg-devel']
    #patches = ['gdk-pixbuf-mmx.patch']

    configure_flags = (target.AutoBuild.configure_flags
			   + ' --disable-glibtest'
			   + ' --enable-introspection=no'
			   + ' --disable-introspection'
			   + ' --disable-gdiplus'
			   + ' --disable-modules'
			   #+ ' --without-libtiff'
			   #+ ' --without-libjpeg'
			   + ' --disable-dependency-tracking'
				)
class Gdk_pixbuf_2__darwin(Gdk_pixbuf_2):
    patches = ['gdk-pixbuf-2.28.2-no-gio-sniff.patch']

    source = 'http://ftp.gnome.org/pub/gnome/sources/gdk-pixbuf/2.26/gdk-pixbuf-2.26.5.tar.xz'
    #source = 'http://ftp.gnome.org/pub/GNOME/platform/2.32/2.32.1/sources/gdk-pixbuf-2.22.1.tar.gz'
    #patches = ['gdk-pixbuf-mmx.patch']
 