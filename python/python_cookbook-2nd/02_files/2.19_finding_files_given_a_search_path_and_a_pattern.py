#!/usr/bin/env python
import glob, os


def all_files(pattern, search_path, pathsep=os.pathsep):
    for path in search_path.split(pathsep):
        for match in glob.glob(os.path.join(path, pattern)):
            yield match

print all_files('*.pyc', os.environ['PATH']).next()

print list(all_files('*.pyc', os.environ['PATH']))

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2 or sys.argv[1].startswith('-'):
        print 'Use: %s <pattern>' % sys.argv[0]
        sys.exit(1)
    matches = list(all_files(sys.argv[1], os.environ['PATH']))
    print os.environ['PATH']
    print '%d match:' % len(matches)
    for match in matches:
        print match
