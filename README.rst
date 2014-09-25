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
- 2 type of windows: script window (mono document) and project window (multiple
  documents)
- IPython shell dock widget (a.k.a interactive interpreter) usable from both
  window types.
- Project support: simply open an existing directory to import a project
- Debugger with breakpoints and watch windows
- Interpreter independent: you can target a different interpreter than the one
  used to run the IDE, including virtualenvs!
- Package manager interface: let you install, upgrade or remove python
  packages (using pip).


Status
------

This project is still under heavy development.

At the moment, the script window has been implemented (you can edit and run
your python script) but there is still no debugger and no project window.


Road-map
--------

Here is the expected list of milestones till version 1.0:

- [ ] 0.1: implement script window and application settings
- [ ] 0.2: implement project window
- [ ] 1.0: implement debugger interface
- [ ] 1.x: add more features (such as refactoring, add editors for more
           languages (cython, json, html, c))
