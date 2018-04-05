from TileSystem import TileSystem

class Tile:

	def __init__(self, quadKey) :
		self.quadKey = quadKey
		self.levelOfDetail = len(quadKey)
		self.ts = TileSystem()
		# top left corner	
		# self.tileX = -1
		# self.tileY = -1
		self.tileX, self.tileY = self.ts.quadKeyToTileXY(quadKey, self.levelOfDetail)
		# self.pixelX = -1
		# self.pixelY = -1
		self.pixelX, self.pixelY = self.ts.tileXYToPixelXY(self.tileX, self.tileY)
		# self.MinLatitude = ts.MinLatitude
		# self.MinLongitude = ts.MinLongitude
		# self.ts.pixelXYToLatLong(self.pixelX, self.pixelY, self.levelOfDetail, self.MinLatitude, self.MinLongitude)

		# bottom right corner
		# self.MaxLatitude = ts.MaxLatitude
		# self.MaxLongitude = ts.MaxLongitude
		# self.ts.pixelXYToLatLong(self.pixelX + 255, self.pixelY + 255, self.levelOfDetail, self.MaxLatitude, self.MaxLongitude)
		self.pixelX1 = self.pixelX + 255
		self.pixelY1 = self.pixelY + 255

	def crop(self, pX0, pX1, pY0, pY1) :
		pixelXs = self.ts.clip(pX0, self.pixelX, self.pixelX1)
		pixelXe = self.ts.clip(pX1, self.pixelX, self.pixelX1)
		pixelYs = self.ts.clip(pY0, self.pixelY, self.pixelY1)
		pixelYe = self.ts.clip(pY1, self.pixelY, self.pixelY1)
		return pixelXs - self.pixelX, pixelYs - self.pixelY, pixelXe - self.pixels, pixelYe - self.pixelY







