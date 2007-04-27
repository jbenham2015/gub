import gub
import mirrors

class Linux_headers (gub.BinarySpec, gub.SdkBuildSpec):
    def __init__ (self, settings):
        gub.BinarySpec.__init__ (self, settings)
        self.with_tarball (mirror=mirrors.linux_2_4,
                           version='2.4.34', format='bz2')
    def get_subpackage_names (self):
        return ['']
    def patch (self):
        self.system ('''
cd %(srcdir)s && yes yes | make ARCH=%(package_arch)s oldconfig symlinks include/linux/version.h
#cd %(srcdir)s && yes yes | make ARCH=i386 oldconfig
#cd %(srcdir)s && make ARCH=%(package_arch)s symlinks include/linux/version.h
cd %(srcdir)s && mv include .include
cd %(srcdir)s && rm -rf *
cd %(srcdir)s && mkdir usr
cd %(srcdir)s && mv .include usr/include
cd %(srcdir)s && rm -f\
 usr/include/scsi/sg.h\
 usr/include/scsi/scsi.h\
 usr/include/scsi/scsi_ioctl.h\
 usr/include/net/route.h
''')

import debian
Linux_headers__powerpc = debian.Linux_kernel_headers
Linux_headers__linux__64 = debian.Linux_kernel_headers
Linux_headers__arm__linux__softfloat = debian.Linux_kernel_headers
Linux_headers__arm__linux__vfp = debian.Linux_kernel_headers
