"""
Test if the zip file is working.

Usage:

1) install pyqode from pypi (or from github)
2) run ``python2 test_zip_file.py gen``
3) uninstall pyqode: pip uninstall pyqode.qt pyqode.core pyqode.python
4) run ``python2 test_zip_file.py``, you should see the following output:

```
['/home/colin/dev/QIdle/libs.zip', '/home/colin/dev/QIdle', '/home/colin/dev/QIdle', '/usr/lib/python27.zip', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-linux2', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/lib/python2.7/site-packages', '/usr/lib/python2.7/site-packages/gtk-2.0']
/home/colin/dev/QIdle/libs.zip/pyqode/core/api/code_edit.py
```

"""
import sys
import os
ZIP = os.path.join(os.getcwd(), 'libs.zip')

if len(sys.argv) == 2 and sys.argv[1] == 'gen':
    #--- gen zip file
    import jedi, pep8, pyqode, pyqode.core, pyqode.python, pyqode.qt, frosted, pies
    from qidle.system import embed_package_into_zip
    embed_package_into_zip([jedi, pep8, pyqode, pyqode.core, pyqode.python,
                            pyqode.qt, frosted, pies], ZIP)
else:
    # importing a pyqode module should fail
    fail = False
    try:
        from pyqode.core.api import code_edit
    except ImportError:
        fail = True
    assert fail is True

    # mount zip file
    sys.path.insert(0, ZIP)
    print(sys.path)

    # test it!
    from pyqode.core.api import code_edit
    print(code_edit.__file__)
    assert ZIP in code_edit.__file__
