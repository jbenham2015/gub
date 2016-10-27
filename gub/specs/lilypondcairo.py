from gub.specs import lilypond

# FIXME: this is a version of lilypond which uses pangocairo used by
# Denemo We probably do not want to build pango + cairo for standalone
# lilypond packages, because that would also pull libX11 dependencies
# in.  Hmm.

class Lilypondcairo (lilypond.Lilypond):
<<<<<<< HEAD
    source = 'http://lilypond.org/downloads/source/v2.13/lilypond-2.13.62.tar.gz'
    dependencies = [x.replace ('pango', 'pangocairo')
                    for x in lilypond.Lilypond.dependencies]
=======
>>>>>>> fe5abd652386985530dc1142f1e7a5657e6d6e58
    patches = [
               'lilypond-chord-names.patch',
        ]
    source = 'http://download.linuxaudio.org/lilypond/sources/v2.19/lilypond-2.19.21.tar.gz'
 
    def get_conflict_dict (self):
        return {'': ['lilypond']}

class Lilypondcairo__mingw (lilypond.Lilypond__mingw):
    source = Lilypondcairo.source
    dependencies = [x.replace ('pango', 'pangocairo')
             for x in lilypond.Lilypond__mingw.dependencies]
    def get_conflict_dict (self):
        return {'': ['lilypond']}

class Lilypondcairo__darwin (lilypond.Lilypond__darwin):
    source = 'http://download.linuxaudio.org/lilypond/sources/v2.19/lilypond-2.19.21.tar.gz'

    def get_conflict_dict (self):
        return {'': ['lilypond']}
    dependencies = [x.replace ('pango', 'pangocairo')
             for x in lilypond.Lilypond__mingw.dependencies]

class Lilypondcairo__darwin__ppc (lilypond.Lilypond__darwin__ppc):
    def get_conflict_dict (self):
        return {'': ['lilypond']}
