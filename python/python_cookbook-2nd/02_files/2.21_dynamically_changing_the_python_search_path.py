#!/usr/bin/env python


def AddSysPath(new_path):
    """ AddSysPath(new_path): adds a "directory" to Python sys.path
    Does not add the directory if it does not exists or if it's already on
    sys.path. Return 1 if OK, -1 if new_path does not exist, 0 if it was 
    already on sys.path.
    """
    import sys, os
    # Avoid adding nonexisent path
    if not os.path.exists(new_path):
        return -1
    # Standardize on path. Windows is case-insensitive, so lowercase
    # for definitness if we are on Windows.
    new_path = os.path.abspath(new_path)
    if sys.platform == 'win32':
        new_path = new_path.lower()
    # Check against all currently available paths
    for x in sys.path:
        x = os.path.abspath(x)
        if sys.platform == 'win32':
            x = x.lower()
        if new_path in (x, x + os.sep):
            return 0
    sys.path.append(new_path)
    # if you want the new_path to take precedence over existing
    # directories already in sys.path, instead of appending, use:
    # sys.path.insert(0, sys.path)
    return 1


if __name__ == '__main__':
    # Test and show usage
    import sys
    print('Before:')
    for x in sys.path:
        print(x)
    if sys.platform == 'win32':
        print(AddSysPath('c:\\Temp'))
        print(AddSysPath('c:\temp'))
    else:
        print(AddSysPath('/usr/lib/'))
    print('After:')
    for x in sys.path:
        print(x)
