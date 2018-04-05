from TileSystem import TileSystem
from Download import Download

class Search:
    def __init__(self, lat1, lat2, lon1, lon2) :
        self.ts = TileSystem()
        self.dl = Download()
        self.qkll = list()

        if lat1 > lat2 :
            self.MinLatitude = lat1
            self.MaxLatitude = lat2
        else :
            self.MinLatitude = lat2
            self.MaxLatitude = lat1

        if lon1 < lon2 :
            self.MinLongitude = lon1
            self.MaxLongitude = lon2
        else :
            self.MinLongitude = lon2
            self.MaxLongitude = lon1

    def getTileXY(self, lat, lon, levelOfDetail) :
        
        pX, pY = self.ts.latLongToPixelXY(lat, lon, levelOfDetail)
        tX, tY = self.ts.pixelXYToTileXY(pX, pY)
        return tX, tY

    def search1Level(self, levelOfDetail) :
        tX1, tY1 = self.getTileXY(self.MinLatitude, self.MinLongitude, levelOfDetail)
        tX2, tY2 = self.getTileXY(self.MaxLatitude, self.MaxLongitude, levelOfDetail)
        print((tX1, tY1))
        print((tX2, tY2))
        re = list()

        for i in range(tY1, tY2 + 1) :
            for j in range(tX1, tX2 + 1) :
                qk = self.ts.tileXYToQuadKey(j, i, levelOfDetail)
                if self.dl.getUrlResponse(qk) :
                    re.append(qk)
                else :
                    return None

        return re

    def searchLevels(self) :
        lod = 1
        ql = self.search1Level(lod)
        while ql:
            self.qkll.append(ql)
            lod += 1
            ql = self.search1Level(lod)







