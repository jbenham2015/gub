from gub import target

class Poppler (target.AutoBuild):
    source = 'http://poppler.freedesktop.org/poppler-0.24.5.tar.xz'
    dependencies = ['tools::libtool', 'tools::glib',
                'zlib-devel',
                'fontconfig-devel',
                'libpng',
                'libjpeg-devel',
                'libxml2-devel',
                ]
    configure_flags = (target.AutoBuild.configure_flags
                + ' --disable-poppler-qt'
                + ' --disable-poppler-qt4'
                + ' --enable-xpdf-headers'
                + ' --disable-gtk-test'
		+ ' --disable-libjpeg'
		+ ' --disable-libopenjpeg')

class Poppler__mingw (Poppler):
    #patches = ['poppler-0.11.2-mingw.patch']
    pass
class Poppler__darwin (Poppler):
    source = 'http://poppler.freedesktop.org/poppler-0.16.1.tar.gz'
 #    source = 'http://poppler.freedesktop.org/poppler-0.20.5.tar.gz'


