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
- IPython console dock widget (a.k.a interactive interpreter) usable from both
  window types.
- Project support: simply open an existing directory to import a project
- Debugger with breakpoints and watch windows
- Interpreter independent: you can target a different interpreter than the one
  used to run the IDE, including virtualenvs!
- Package manager interface: let you install, upgrade or remove python
  packages (using pip).

Installation
------------

The project is under heavy development and has not been released on pypi yet.

You can install from the git repository::

    pip install git+https://github.com/ColinDuquesnoy/QIdle.git

Then you can run bootstrap.py (it will warn you if there are any missing
requirements)

Road-map
--------

Here is the expected list of milestones till version 1.0:

- [x] 0.1: add script window and application settings
- [x] 0.2: add project window
- [0] 0.3: improve preferences: add a keyboard shortcuts page and an appearance tab
- [ ] 1.0: add debugger interface
- [ ] 1.x: add more features (such as refactoring, add editors for more
  languages (cython, json, html, c))

Screenshots
-----------

.. image:: https://raw.githubusercontent.com/ColinDuquesnoy/QIdle/master/share/screenshot.png
