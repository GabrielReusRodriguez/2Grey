#!/bin/env python3


from PIL import Image

Image.open('./img.png').convert('L').save('grr.png')