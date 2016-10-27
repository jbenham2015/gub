from gub import target

class Librsvg (target.AutoBuild):
    source = 'http://ftp.acc.umu.se/pub/GNOME/sources/librsvg/2.34/librsvg-2.34.2.tar.xz'
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
