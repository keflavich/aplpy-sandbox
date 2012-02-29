import matplotlib
import aplpy
import os
import numpy as np
import pytest
import pyfits

# Test initialization 
@pytest.mark.parametrize(('data'), [np.arange(256).reshape((16, 16)), None])
def test_init(data):
    header = pyfits.Header()
    header.fromTxtFile('MSX.hdr')
    HDU = pyfits.PrimaryHDU(data=data, header=header)
    f = aplpy.FITSFigure(HDU)
    suffix = 'withdata' if data is not None else 'nodata'
    f.save('MSX_frame_%s.png' % suffix)
    f.close()
    print "Ran test MSX_frame_%s" % suffix
                        


# Test simple contour generation with Numpy example (but real, MSX header)
@pytest.mark.parametrize(('filled'), [True, False])
def test_numpy_contour(filled):
    data = np.arange(256).reshape((16, 16))
    header = pyfits.Header()
    header.fromTxtFile('MSX.hdr')
    HDU = pyfits.PrimaryHDU(data=data, header=header)
    f = aplpy.FITSFigure(HDU)
    f.show_grayscale()
    f.show_contour(HDU, levels=np.linspace(1., 254., 10), filled=filled)
    suffix = 'filled' if filled else 'notfilled'
    f.save('MSX_contours_%s.png' % suffix)
    f.close()
    print "Ran test %s" % suffix
                        

