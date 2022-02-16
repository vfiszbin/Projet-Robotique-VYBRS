import math
def getdistance(ax,ay,bx,by):
	"""
	calcul la distance entre deux points a et b
	"""
	return math.sqrt((pow(ax-bx,2)+pow(ay-by,2)))
def centreline(ax,ay,bx,by):
	"""
	calcul le centre d'une ligne
	"""
	return ((ax+bx)/2,(ay+by)/2)
#print(getdistance(2,3,4,5))
#print (centreline(1,1,-1,-1))

