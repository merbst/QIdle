QIdle
=====

QIdle is a Python IDE built with the PyQt GUI toolkit and pyQode.


Features
--------

QIdle has the following features:

- Coded in 100% pure Python, using the PyQt GUI toolkit
- Cross-platform: works on Windows, Unix, and OS X
- Multi-window text editor with multiple undo, Python colorizing, smart indent,
  call tips, JEDI CODE COMPLETION and many other features
- IPython shell dock widget (a.k.a interactive interpreter) usable from both
  window types.
- Project support: simply open an existing directory to import a project,
  projects have a dedicated view and support for run configurations.
- Debugger with breakpoints and watch windows
- Interpreter independent: you can target a different interpreter than the one
  used to run the IDE, including virtualenvs!
- Package manager interface: let you install, upgrade or uninstall python
  packages from pypi.

QIdle has two window types: the script window and the project window. The
script window is a single document window that let you edit and run one single
python script. The project window is a multi document window that let you work
on an entire python package.


Status
------

This project is still under heavy development.

At the moment, the script window has been implemented (you can edit and run
your python script) but there is still no debugger and no project window.
