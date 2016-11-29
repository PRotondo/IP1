def transpose(v) :
	n, m = len(v),len(v[0])
	ans = [[ v[i][j] for i in range(n)] for j in range(m)]
	return ans

def readNext(f) :
	while True :
		s = f.readline()
		if len(s) == 0 :
			return ''
		if s[0] == '#' :
			continue
		return s

def getGray(filename):
	f = open(filename,'r')
	s = f.readline()
	width, height = map(int,readNext(f).split())
	maximumIntensity = int(readNext(f))
	assert(maximumIntensity==255)
	if s == 'P2\n' :
		aux = [ list(map(int,readNext(f).split())) for i in range(height)]
		ans = [[aux[j][i] for j in range(height)] for i in range(width)]
		return ans
	return []

def saveGray(px,filename) :
	width, height = len(px), len(px[0])
	f = open(filename,'w')
	f.write('P2\n' + str(width) + " " + str(height) + "\n255\n")
	py = transpose(px)
	f.write("\n".join(map(lambda l : " ".join(map(str,l)),py )))
