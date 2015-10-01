#!/usr/bin/env python
# encoding: utf-8

class ImageFusion:
    """ Interface for image fusion """

    def __init__(self, imageNames):
        self._imageNames = imageNames

    def fusion(self):
        raise NotImplementedError()
