"""
This package contains the various type of main window of the application:

   - base: BaseWindow
   - script: ScriptWindow (mono-document window)
   - project: ProjectWindow (multi-document window)

"""
from .project import ProjectWindow
from .script import ScriptWindow