import TileSystem

class Tile:

	def __init__(self, quadKey) :
		self.quadKey = quadKey
		self.levelOfDetail = len(quadKey)
		self.ts = TileSystem()
		# top left corner	
		self.tileX = -1
		self.tileY = -1
		self.pixelX = -1
		self.pixelY = -1
		self.MinLatitude = ts.MinLatitude
		self.MinLongitude = ts.MinLongitude
		# bottom right corner
		self.MaxLatitude = ts.MaxLatitude
		self.MaxLongitude = ts.MaxLongitude

