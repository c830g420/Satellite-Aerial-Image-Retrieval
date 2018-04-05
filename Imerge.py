from TileSystem import TileSystem
from Tile import Tile
import cv2
import numpy as np

class Imerge:
	def __init__(self, pX1, pX2, pY1, pY2, lod) :
		# self.levelOfDetail = lod
		self.ts = TileSystem()
		self.pX1 = pX1
		self.pX2 = pX2
		self.pY1 = pY1
		self.pY2 = pY2
		self.dir = './temp/%s.jpg'
		# print(pX2 - pX1)
		# print(pY2 - pY1)
		self.img = self.blankIm()
	
	def blankIm(self) :
		# pX1 = 0
		# pY1 = 0
		# self.ts.latLongToPixelXY(self.MinLatitude, self.MinLongitude, self.levelOfDetail, pX1, pY1)
		# pX2 = 0
		# pY2 = 0
		# self.ts.latLongToPixelXY(self.MaxLatitude, self.MaxLongitude, self.levelOfDetail, pX2, pY2)
		return np.zeros((self.pY2 - self.pY1 + 1, self.pX2 - self.pX1 + 1, 3), dtype = 'uint8')

	def fillIm(self, tl) :
		timg = cv2.imread(self.dir % tl.quadKey)
		xst = tl.pixelX - self.pX1
		yst = tl.pixelY - self.pY1
		xed = tl.pixelX1 - self.pX2
		yed = tl.pixelY1 - self.pY2

		if xst < 0:
			txst = - xst
			xst = 0
		else :
			txst = 0

		if yst < 0:
			tyst = - yst
			yst = 0
		else :
			tyst = 0

		if xed > 0:
			txed = - xed
			xed = self.pX2 - self.pX1 + 1
		else :
			txed = 256

		if yed > 0:
			tyed = - yed
			yed = self.pY2 - self.pY1 + 1
		else :
			tyed = 256

		self.img[yst:yed, xst:xed, :] = timg[tyst:tyed, txst:txed, :]

	def saveFig(self, fname = 'Result.jpg') :
		return cv2.imwrite('%s.jpg' % fname, self.img)


