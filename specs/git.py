import toolpackage
import targetpackage
import repository

class Git (toolpackage.ToolBuildSpec):
    def __init__ (self, settings):
        toolpackage.ToolBuildSpec.__init__ (self, settings)
        self.with (mirror="http://kernel.org/pub/software/scm/git/git-%(version)s.tar.bz2",
                   version="1.5.0.rc3")
    def patch (self):
        self.shadow_tree ("%(srcdir)s", '%(builddir)s')
    def configure (self):
        self.dump ('prefix=%(system_root)s/usr', '%(builddir)s/config.mak')
        
    def wrap_executables (self):
        # GIT executables use ancient unix style smart name-based
        # functionality switching.  Did Linus not read or understand
        # Standards.texi?
        pass

class Git (targetpackage.TargetBuildSpec):
    def __init__ (self, settings):
        targetpackage.TargetBuildSpec.__init__ (self, settings)
        source = 'git://repo.or.cz/git/mingw.git'

        repo = repository.GitRepository (
            self.get_repodir (),
            branch=settings.git_branch,
            
            source=source)
        self.with_vc (repo)
        self.target_gcc_flags = ' -mms-bitfields '
        
    def version (self):
        return '1.4.9993'

    def get_dependency_dict (self):
        return {'': [
            'bash',
            'zlib',
            'regex', 
            ]}    

    def get_subpackage_names (self):
        return ['']

    def get_build_dependencies (self):
        return ['zlib-devel',
                'regex-devel', 
                ]

    def patch (self):
        targetpackage.TargetBuildSpec.patch (self)
        self.system ('rm -rf %(builddir)s')
        self.shadow_tree ('%(srcdir)s', '%(builddir)s')

class Git__mingw (Git):
    def __init__ (self, settings):
        Git.__init__ (self, settings)
        self.target_gcc_flags = ' -mms-bitfields '
        
    def configure (self):
        targetpackage.TargetBuildSpec.configure (self)
        self.file_sub ([('CFLAGS = -g',
                         'CFLAGS = -I compat/ -g')],
                       '%(builddir)s/config.mak.autogen')
        self.file_sub ([('-lsocket',
                         '-lwsock32'),
                        ('TRACK_CFLAGS *=', 'XXX_TRACK_CFLAGS = '),
                        ],
                       '%(builddir)s/Makefile')

    def compile_command (self):
        return (targetpackage.TargetBuildSpec.compile_command (self)
                + ' uname_S=MINGW'
                + ' SHELL_PATH=/bin/sh')
    def install_command (self):
        return (targetpackage.TargetBuildSpec.install_command (self)
                + ' uname_S=MINGW'
                + ' SHELL_PATH=/bin/sh')
    
