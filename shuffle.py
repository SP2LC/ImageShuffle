# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import random
import Image

if len(sys.argv) < 4:
  print "引数が間違っています。"
  print "python shuffle.py 元ファイル 横分割数 縦分割数 [シード値]"
  sys.exit(-1)

filename = sys.argv[1]
cols = int(sys.argv[2])
rows = int(sys.argv[3])

seed = 10
if len(sys.argv) >= 5:
  seed = int(sys.argv[4])

random.seed(seed)

def split(img, w, h):
  cols = np.hsplit(img, w)
  return [np.vsplit(a, h) for a in cols]

def addNum(splitImgs):
  return [[((x, y), img) for y, img in enumerate(col)] for x, col in enumerate(splitImgs)]

# 破壊的
def shuffle(splitImgs):
  [random.shuffle(col) for col in splitImgs]
  random.shuffle(splitImgs)

def connect(splitImgs):
  return np.hstack([np.vstack([img for pos, img in col]) for col in splitImgs])

orig = mpimg.imread(filename)
print orig

split = addNum(split(orig, cols, rows))

shuffle(split)

newImg = connect(split)
pil = Image.fromarray(np.uint8(newImg * 255))
pil.save(os.path.splitext(filename)[0] + ".ppm")


for x, col in enumerate(split):
  for y, img in enumerate(col):
    print "moved %s to %s" % (img[0], (x, y))

plt.imshow(newImg)
plt.show()
