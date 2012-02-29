import matplotlib
import aplpy
import os

filename = 'D1740P30.FIT'
if os.path.exists('D1740P30.FIT'):
    F = aplpy.FITSFigure('D1740P30.FIT')
    F.show_grayscale()
else:
    import urllib
    import pyfits
    ff = pyfits.open(urllib.urlretrieve('http://eta.colorado.edu/aplpy-debug/%s' % filename)[0])
    F = aplpy.FITSFigure(ff)
    F.show_grayscale()

