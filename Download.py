import urllib.request

class Download:
	def __init__(self) :
		self.bingMapsKey = 'PcyWU9OvD5ekcciniRcl~9OChkYYOEagqQbR4FM-6wQ~Ai9r98N1UgCFvW_8mhZ8mWGudmj4Lhd0sClEQnreqQrIuOVokAIDt8Rc7oGgC57o'
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
		# urllib.request.urlretrieve(url, './temp/%s.jpg' % ''.join(self.quadKey))
		with urllib.request.urlopen(url) as repsonse:
			re = repsonse.read()

		if len(re) > 1033:
			return self.quadKey
		else :
			return None

	def getUrlImage(self.quadKey) :
		self.setQuadkey(quadKey)
		url = self.getUrl()
		return urllib.request.urlretrieve(url, './temp/%s.jpg' % ''.join(self.quadKey))

