import math
def getdistance(ax,ay,bx,by):
	"""
	calcule la distance entre deux points a et b
	"""
	return math.sqrt((pow(ax-bx,2)+pow(ay-by,2)))
def centreline(ax,ay,bx,by):
	"""
	calcule le centre d'une ligne
	"""
	return ((ax+bx)/2,(ay+by)/2)
def overlap(x0,x1,y0,y1,x2,x3,y2,y3):
	"""
	rend false si deux rectangles s'intersecte
	"""
	if ((x0 >= x2 )and(x0<=x3)and(y0>=y2)and(y0<= y3)) or ((x0 >= x2 )and(x0<=x3)and(y1>=y2)and(y1<= y3)) or ((x1 >= x2 )and(x1<=x3)and(y0>=y1)and(y0<=y3)) or ((x1 >= x2 )and(x1<=x3)and(y1>=y2)and(y1<= y3)):
		return True

#print(getdistance(2,3,4,5))
#print (centreline(1,1,-1,-1))

