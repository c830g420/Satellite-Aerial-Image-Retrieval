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

    def latLongToPixelXY(self, latitude, longitude, levelOfDetail) :
        latitude = self.clip(latitude, self.MinLatitude, self.MaxLatitude)
        longitude = self.clip(longitude, self.MinLongitude, self.MaxLongitude)

        x = (longitude + 180) / 360
        sinLatitude = math.sin(latitude * math.pi / 180)
        y = 0.5 - math.log((1 + sinLatitude) / (1 - sinLatitude)) / 4 / math.pi

        mapSize = self.mapSize(levelOfDetail)
        pixelX = int(self.clip(x * mapSize + 0.5, 0, mapSize - 1))
        pixelY = int(self.clip(y * mapSize + 0.5, 0, mapSize - 1))

        return pixelX, pixelY

    def pixelXYToLatLong(self, pixelX, pixelY, levelOfDetail) :
        mapSize = self.mapSize(levelOfDetail)
        x = (self.clip(pixelX, 0, mapSize - 1) / mapSize) - 0.5
        y = 0.5 - (self.clip(pixelY, 0, mapSize - 1) / mapSize)

        latitude = 90 - 360 * math.atan(math.exp(-y * 2 * math.pi)) / math.pi
        longitude = 360 * x

        return latitude, longitude

    def pixelXYToTileXY(self, pixelX, pixelY) :
        tileX = round(pixelX / 256)
        tileY = round(pixelY / 256)
        
        return tileX, tileY

    def tileXYToPixelXY(self, tileX, tileY) :
        pixelX = tileX * 256
        pixelY = tileY * 256

        return pixelX, pixelY

    def tileXYToQuadKey(self, tileX, tileY, levelOfDetail) :
        quadKey = list()

        for i in range(levelOfDetail, 0, -1) :
            digit = 0
            mask = 1 << (i - 1)
            if (tileX & mask) :
                digit += 1
            if (tileY & mask) : 
                digit += 2
            quadKey.append(str(digit))

        return ''.join(quadKey)

    def quadKeyToTileXY(self, quadKey, levelOfDetail) :
        tileX = 0
        tileY = 0
        levelOfDetail = len(quadKey)
        for i in range(levelOfDetail, 0, -1) : 
            mask = 1 << (i - 1)
            digit = quadKey[-i]
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
                return None

        return tileX, tileY
            








