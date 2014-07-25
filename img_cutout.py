#!/usr/bin/python
#creates cutouts from images 
#helpful for a large field and one wants to view individual objects
#this may be used in a loop to create individual images 

import pyfits
import re
from pylab import *
#
#
def img_cutout(im,xc,yc,dx,dy,wcs=None):
    """This is a tool to cut image regions (rectangular slabs) 
    and rewrites the header info to preserve the WCS information
    im = 'file.fits' name of fits image to be opened
    xc = x-center of cut
    yc = y-center of cut
    dx = x-size in pixels
    dy = y-size in pixels
    wcs = set TRUE if you want to keep WCS correct, 
          leave default if you want just the image coordinates."""
###read image to array
    f,hd = pyfits.getdata(im,header=True)
###corners of slice and cut of image
    x1 = xc-dx/2
    x2 = x1+dx
    y1 = yc-dy/2
    y2 = y1+dy
    sl = f[y1:y2,x1:x2]
###display image cutout
    imshow(sl,origin='lower')
    if wcs:
	hd.update('LTV1',x1)
    	hd.update('LTV2',y1)
   	hd.update('CRPIX1',hd.get('CRPIX1')-x1)
    	hd.update('CRPIX2',hd.get('CRPIX2')-y1)
###prompt for saving as fits file
   # in1 = raw_input('Do you want to save this cutout (y/n)? ')
   # p = re.compile('^[yY]')
   # if re.match(p,in1):
    #   nm = raw_input('Name of file (format: name.fits): ')
     #  pyfits.writeto(nm,sl,header=hd)
     #  close()    
    return sl,hd
