#!/usr/bin/env python
import zipfile, tempfile, os, sys

handle, filename = tempfile.mkstemp('.zip')
os.close(handle)
# When you open file, the operating system will assign a FD that is available and
# when you close it then OS release the FD and may assign that FD to another file
# opened after that. Its Operating system's way to track Opened Files and it has
# nothing to do with a specific file.
z = zipfile.ZipFile(filename, 'w')
z.writestr('hello.py', 'def f(): return "hello world from "+__file__\n')
z.close()
sys.path.insert(0, filename)
import hello
print hello.f()
os.unlink(filename)
