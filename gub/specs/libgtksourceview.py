from gub import target

class Libgtksourceview (target.AutoBuild):
    source = 'http://ftp.gnome.org/pub/gnome/sources/gtksourceview/3.2/gtksourceview-3.2.3.tar.xz'
    patches = ['gtksourceview-3.2.3.no.po.patch']
    dependencies = [
            'gtk+-devel',
            'libxml2-devel',
            'tools::intltool',
            ]
    configure_flags = (target.AutoBuild.configure_flags
			+ ' --enable-static'
			+ ' --disable-shared'
                       	)
class Libgtksourceview__darwin (Libgtksourceview):
   source = 'http://ftp.gnome.org/pub/gnome/sources/gtksourceview/2.6/gtksourceview-2.6.2.tar.gz'
   #source = 'http://ftp.gnome.org/pub/gnome/sources/gtksourceview/2.11/gtksourceview-2.11.2.tar.gz'
   patches = []
   dependencies = [
            'gtk+-devel',
            'tools::intltool',
            ]
