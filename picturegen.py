from sys import argv
from sys import stdin
from math import floor
from PIL import Image
import PIL
import struct

class HashThings:
    internalStates = [0, 0, 0]
    def add(self, nums):
        self.internalStates = [self.internalStates[i] + nums[i] for i in range(3)]
        for i, state in enumerate(self.internalStates):
            if state > 255:
                self.internalStates[i] = state - ((state // 255) * 255)
    def reset(self):
        self.internalStates = [0, 0, 0]
    def getPix(self):
        return tuple(self.internalStates)

if '-f' in argv:
    outFile = argv[argv.index('-f') + 1]
    BIter = False
else:
    outFile = '1.png'
    BIter = True
if '-d' in argv:
    outDir = argv[argv.index('-d') + 1]
else:
    outDir = ''
if '-i' in argv:
    iterations = int(argv[argv.index('-i') + 1])
else:
    iterations = 2
if '-w' in argv:
    w = int(argv[argv.index('-w') + 1])
else:
    w = 100
if '-h' in argv:
    h = int(argv[argv.index('-h') + 1])
else:
    h = 100
reset = not ('-nre' in argv)
verbose = ('-v' in argv)

im = Image.new('RGB', (w, h))
imArray = []
hashThing = HashThings()
vbArray = [25, 50, 75, 100]

for inBytes in range(1, iterations+1):
    if verbose:
        print('Starting iteration ' + str(inBytes))
    for x in range(w):
        for y in range(h):
            if verbose and (floor((((x * w) + y) / ((w * h) - 1)) * 100)) in vbArray:
                print('Picture ' + str(inBytes) + ': Pixel ' + str((x * w) + y) + ' out of ' + str((w * h) - 1))
                vbArray.pop(0)
            if reset:
                hashThing.reset()
            hashThing.add((int.from_bytes(stdin.buffer.read(inBytes), byteorder='little'),
                            int.from_bytes(stdin.buffer.read(inBytes), byteorder='little'),
                            int.from_bytes(stdin.buffer.read(inBytes), byteorder='little')))
            imArray.append(hashThing.getPix())
    im.putdata(imArray)
    im.save(outDir + outFile)
    imArray = []
    vbArray = [25, 50, 75, 100]
    if BIter:
        outFile = str(int(outFile[:-4])+1) + outFile[-4:]
