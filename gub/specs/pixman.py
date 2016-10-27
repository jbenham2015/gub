from gub import target

 
class Pixman (target.AutoBuild):
    source = 'http://xorg.freedesktop.org/archive/individual/lib/pixman-0.32.6.tar.gz'
    dependencies = ['libtool', 'libpng']
    patches = ['pixman-no-tests.patch']

class Pixman__linux (Pixman):
     patches = ['pixman-no-tests.patch']
#    configure_variables = (Pixman.configure_variables
#                          + ' LDFLAGS="-L%(system_prefix)s/lib -lgcc_eh -lgcc" ')
  #  configure_flags = (Pixman.configure_flags
   #                		+ ' --disable-static-testprogs'
#				+ ' --disable-gtk')
class Pixman__linux__ppc (Pixman):
     patches = ['pixman-0.13.2-auxvec.patch']

class Pixman__darwin (Pixman):
    source = 'http://xorg.freedesktop.org/archive/individual/lib/pixman-0.32.4.tar.bz2'
    configure_variables = (Pixman.configure_variables
                           + ' LDFLAGS="-L%(system_prefix)s/lib -lgcc_eh -lgcc" ')


class Pixman (target.AutoBuild):
    source = 'http://xorg.freedesktop.org/archive/individual/lib/pixman-0.32.4.tar.bz2'
    dependencies = ['libtool', 'libpng']

class Pixman__linux__ppc (Pixman):
    patches = ['pixman-0.13.2-auxvec.patch']
