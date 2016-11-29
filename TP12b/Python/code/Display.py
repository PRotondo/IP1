from PIL import Image


def getGray(filename):
	im = Image.open(filename, 'r')
	pix = im.convert('L')
	width, height = im.size
	ans = [[pix.getpixel((i, j)) for j in range(height)] for i in range(width)]
	return ans
    
def drawGray(px):
	width, height = len(px),len(px[0])
	im = Image.new('L', (width,height))
	for i in range(width) :
		for j in range(height) :
			im.putpixel((i,j), px[i][j])
	im.show()
	
def saveGray(px,filename) :
	width, height = len(px),len(px[0])
	im = Image.new('L', (width,height))
	for i in range(width) :
		for j in range(height) :
			im.putpixel((i,j), px[i][j])
	im.save(filename)
 
