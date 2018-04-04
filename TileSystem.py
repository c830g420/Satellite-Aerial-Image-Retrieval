import math

class TileSystem:

	def __init__(self) :
		self.EarthRadius = 6378137
        self.MinLatitude = -85.05112878
        self.MaxLatitude = 85.05112878
        self.MinLongitude = -180
        self.MaxLongitude = 180

    def clip(self, n, minValue, maxValue) :
    	return max(min(n, maxValue), minValue)

    def mapSize(self, levelOfDetail) :
    	return 256 << levelOfDetail

    def groundResolution(self, latitude, levelOfDetail) :
    	latitude = self.clip(latitude, self.MinLatitude, self.MaxLatitude)
        return math.cos(latitude * math.pi / 180) * 2 * math.pi * self.EarthRadius / self.mapSize(levelOfDetail)

    def mapScale(self, latitude, levelOfDetail, screenDpi) :
    	return self.groundResolution(latitude, levelOfDetail) * screenDpi / 0.0254

    def latLongToPixelXY(self, latitude, longitude, levelOfDetail, pixelX, pixelY) :
    	latitude = self.clip(latitude, self.MinLatitude, self.MaxLatitude)
    	longitude = self.clip(longitude, self.MinLongitude, self.MaxLongitude)

    	x = (longitude + 180) / 360
    	sinLatitude = math.sin(latitude * math.pi / 180)
    	y = 0.5 - math.log((1 + sinLatitude) / (1 - sinLatitude)) / 4 / math.pi

    	mapSize = self.mapSize(levelOfDetail)
    	pixelX = int(self.clip(x * mapSize + 0.5, 0, mapSize - 1))
    	pixelY = int(self.clip(y * mapSize + 0.5, 0, mapSize - 1))

    	# return pixelX, pixelY

    def pixelXYToLatLong(pixelX, pixelY, levelOfDetail, latitude, longitude) :
    	mapSize = self.mapSize(levelOfDetail)
    	x = (self.clip(pixelX, 0,, mapSize - 1) / mapSize) - 0.5
    	y = 0.5 - (self.clip(pixelY, 0, mapSize - 1) / mapSize)

    	latitide = 90 - 360 * math.atan(math.exp(-y * 2 * math.pi)) / math.pi
    	longitude = 360 * x

    def pixelXYToTileXY(pixelX, pixelY, tileX, tileY) :
    	tileX = pixelX / 256
    	tileY = pixelY / 256

    def tileXYToPixelXY(tileX, tileY, pixelX, pixelY) :
    	pixelX = tileX * 256
    	pixelY = tileY * 256

    def tileXYToQuadKey(tileX, tileY, levelOfDetail) :
    	quadKey = list()

    	for i in range(levelOfDetail, 0, -1) :
    		digit = 0
    		mask = 1 << (i - 1)
    		if (not tileX & mask) :
    			digit += 1
    		if (not tileY & mask) : 
    			digit += 2
    		quadKey.append(str(digit))

    	return ''.join(quadKey)

    def quadKeyToTileXY(quadKey, tileX, tileY, levelOfDetail) :
    	tileX = 0
    	tileY = 0
    	levelOfDetail = len(quadKey)
    	for i in range(levelOfDetail, 0, -1) : 
    		mask = 1 << (i - 1)
    		digit = quadkey[-i]
    		if (digit == '0') :
    			continue
    		elif (digit == '1') :
    			tileX |= mask
    		elif (digit == '2') :
    			tileY |= mask
    		elif (digit == '3') :
    			tileX |= mask
    			tileY |= mask
    		else :
    			print('Invalid Quadkey digit sequence.')
    			break
    		








