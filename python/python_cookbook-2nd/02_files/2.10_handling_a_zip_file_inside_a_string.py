import zipfile
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class ZipString(zipfile):
    def __init__(self, datastring):
        zipfile.__init__(self, StringIO(datastring))
