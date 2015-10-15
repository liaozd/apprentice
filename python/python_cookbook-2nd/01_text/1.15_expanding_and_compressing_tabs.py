import re

def unexpand(astring, tablen=4):
    # split into alternating space and non-space sequences
    pieces = re.split(r'( +)', astring.expandtabs(tablen))
    lensofar = 0
    for i, piece in enumerate(pieces):
        thislen = len(piece)
        lensofar += thislen
        if piece.isspace():
            # change each space sequences into tabs+spaces
            numblanks = lensofar % tablen
            numtabs = (thislen-numblanks+tablen-1)/tablen
            pieces[i] = '\t'*numtabs + ' '*numblanks

    return ''.join(pieces)

astring = """4 spaces:    8 spaces:       |"""

print unexpand(astring)

def expand_at_linestart(P, tablen=4):
    def exp(mo):
        print type(mo)
        return mo.group().expandtabs(tablen)
    return ''.join([re.sub(r'^\s+', exp, s) for s in P.splitlines(True)])

p = """
      start with 6 spaces
     start with 5 spaces.
"""

print expand_at_linestart(p)