from gub import target

class Evince (target.AutoBuild):
  source = 'http://ftp.gnome.org/pub/GNOME/sources/evince/3.2/evince-3.2.1.tar.xz'
  dependencies = ['intltool', 'poppler']

  patches = ['evince-3.2.1-strip.patch',
		'evince-3.2.1-backenddir.patch']
  configure_flags = (target.AutoBuild.configure_flags
			   + ' --enable-static'
			   + ' --disable-shared'
                           + ' --without-help'
			   + ' --without-libgnome'
			   + ' --without-gconf'
                           + ' --without-keyring'
			   + ' --disable-help'
			   + ' --disable-thumbnailer'
			   + ' --disable-nautilus'
			   + ' --disable-dbus'
			   + ' --disable-gtk-doc'
			   + ' --disable-previewer'
			   + ' --disable-nls'
			   + ' --disable-scrollkeeper'
			   + ' --disable-tiff'
			   + ' --disable-comics'
			   + ' --without-gtk-unix-print')
#  def install (self):
#	target.AutoBuild.install (self)
#        self.system ('cd %(install_prefix)s/lib/ && ln -s libevview3.a libevview3.dll.a')
#	self.system ('cd %(install_prefix)s/lib/ && ln -s libevdocument3.a libevdocument3.dll.a')

class Evince__darwin__x86 (Evince):
  source = 'http://ftp.gnome.org/pub/GNOME/sources/evince/2.32/evince-2.32.0.tar.bz2'

  dependencies = ['intltool','tools::intltool',
                  'poppler', 'gdk-pixbuf-2','gtk+']
  #patches = ['evince-4-Makefile.patch']
  patches = ['evince-4-Makefile.patch']
  #patches = (Evince.patches + ['evince-3.2.1-no-x11.patch'])
  #configure_variables = (target.AutoBuild.configure_variables
   #                        + ' CFLAGS="-g -O0" ')
  configure_flags = (target.AutoBuild.configure_flags
                           + ' --without-libgnome'
                           + ' --without-gconf'
                           + ' --without-keyring'
                           #+ ' --with-platform=win32'
                           + ' --with-smclient-backend=quartz' #not sure what this is
                           + ' --disable-help'
                           + ' --disable-thumbnailer'
                           + ' --disable-nautilus'
                           + ' --disable-dbus'
                           + ' --disable-gtk-doc'
                           + ' --enable-pdf' #FIXME probably need pdf support
                           + ' --disable-previewer' #not sure if this is needed
                           + ' --disable-nls'
                           + ' --without-gtk-unix-print')


class Evince__mingw (Evince):
  configure_flags = (Evince.configure_flags
                           + ' --with-platform=win32'
			   + ' --with-smclient-backend=win32')

  configure_variables = (Evince.configure_variables
                           + ' CPPFLAGS="-D_WIN32_WINNT=0x0501"')

class Evince__linux__x86 (Evince):
  configure_flags = (Evince.configure_flags
                           + ' --with-platform=gnome'
			   + ' --with-smclient-backend=xsmp')

               
