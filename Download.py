import urllib.request
import os

class Download:
	def __init__(self) :
		self.bingMapsKey = '41W7SFbE1T0EL5ZXwqs3~1Qz6gK41TViufkWWMdrxbg~Au2gvdXSyRpNSFsqjlnA5hVuP-2kaFHPdz3pUKMZasjOWt89LqbSAyUCSjx8qsJm'
		self.urlBase = 'http://h0.ortho.tiles.virtualearth.net/tiles/h%s.jpeg?g=131&key=%s'
		self.quadKey = list()

	def setQuadKey(self, quadKey) :
		if (isinstance(quadKey, str)) :
			self.quadKey = list(quadKey)
		else :
			self.quadKey = quadKey

	def getUrl(self) : 
		url = self.urlBase % (''.join(self.quadKey), self.bingMapsKey)
		return url

	def getUrlResponse(self, quadKey) :
		self.setQuadKey(quadKey)
		url = self.getUrl()
		print('\tGetting image by quadKey %s' % quadKey)
		# urllib.request.urlretrieve(url, './temp/%s.jpg' % ''.join(self.quadKey))
		with urllib.request.urlopen(url) as repsonse:
			re = repsonse.read()

		if len(re) > 1033:
			return quadKey
		else :
			return None

	def getUrlImage(self, quadKey) :
		self.setQuadKey(quadKey)
		url = self.getUrl()
		
		urllib.request.urlretrieve(url, './temp/%s.jpg' % ''.join(self.quadKey))

