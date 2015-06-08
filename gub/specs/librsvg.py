from gub import target

class Librsvg (target.AutoBuild):
    source = 'http://ftp.gnome.org/pub/GNOME/sources/librsvg/2.26/librsvg-2.26.0.tar.gz'
    dependencies = ['tools::libtool',
                'fontconfig',
                'glib',
                'gtk+',
                'libxml2']

class Librsvg__darwin (Librsvg):
    dependencies = [x for x in Librsvg.dependencies
                if x.replace ('-devel', '') not in [
                'libxml2', # Included in darwin-sdk, hmm?
                ]]
