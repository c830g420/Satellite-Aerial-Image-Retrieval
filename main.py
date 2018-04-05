import sys
import os

from TileSystem import TileSystem
from Srch import Search
from Download import Download
from Tile import Tile
from Imerge import Imerge

def main():
	# print(sys.argv[0])
	# print(type(sys.argv[1]))
	print('\t\t###########\n\t\t# WELCOME #\n\t\t###########\n')
	lat1 = float(sys.argv[1])
	lon1 = float(sys.argv[2])
	lat2 = float(sys.argv[3])
	lon2 = float(sys.argv[4])
	print((lat1, lon1))
	print((lat2, lon2))
	print('\tStart searching ...\n')
	sc = Search(lat1, lat2, lon1, lon2)
	sc.searchLevels()
	picl = sc.qkll[-1]
	lod = len(sc.qkll)
	print('\tSearching complete ... \n')
	dl = Download()
	tl = list()
	for qk in picl:
		dl.getUrlImage(qk)
		tl.append(Tile(qk))
	ts = TileSystem()
	
	pX1, pY1 = ts.latLongToPixelXY(sc.MinLatitude, sc.MinLongitude, lod)
	
	pX2, pY2 = ts.latLongToPixelXY(sc.MaxLatitude, sc.MaxLongitude, lod)
	print('\tStart merging ...\n')
	mg = Imerge(pX1, pX2, pY1, pY2, lod)
	for t in tl:
		mg.fillIm(t)
	print('\tMerging complete ...\n')
	fname = input('\tPlease give a name to the Image.\n\t\t')
	mg.saveFig(fname)
	if 'y' == input('\tRemove caches? y?\n\t\t') :
		os.remove('./temp/')

	print('DONE')




if __name__ == '__main__':
	main()