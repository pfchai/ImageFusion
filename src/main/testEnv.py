#!/usr/bin/env python
# encoding: utf-8

from PIL import Image
from pylab import *

IMAGEPATH = "../../images/multifocus/"

def average_fusion(imList):
    """算数平均法的图像融合 """

    averageImage = array(Image.open(imList[0]), 'f')
    for name in imList[1:]:
        try:
            averageImage += array(Image.open(name))
        except:
            print name + '...skipped'
    averageImage /= len(imList)
    return  averageImage.astype(int32)


if __name__ == '__main__':

    im = array(Image.open(IMAGEPATH+"a01_1.tif"))
    # imshow(im)
    imLists = [IMAGEPATH+"a01_1.tif",IMAGEPATH+"a01_2.tif"]
    imFusion = average_fusion(imLists)
    figure()
    gray()
    imshow(imFusion)
    show()
