import math
def getdistancePoints(ax,ay,bx,by):
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

def dist(x1, y1, x2, y2, x3, y3): # x3,y3 is the point
	""" calcul la distance entre un point et un segement """

	px = x2-x1
	py = y2-y1

	norm = px*px + py*py

	u =  ((x3 - x1) * px + (y3 - y1) * py) / float(norm)

	if u > 1:
		u = 1
	elif u < 0:
		u = 0

	x = x1 + u * px
	y = y1 + u * py

	dx = x - x3
	dy = y - y3

	dist = (dx*dx + dy*dy)**.5
	print("dist ", dist)
	return dist

def inf(liste):
	"""
	retourne le plus petit element de liste
	"""
	tmp=min(liste)
	print("inf :", tmp)
	return tmp 

def angle_of_vectors(a,b,c,d):
	dotProduct = a*c + b*d
	# for three dimensional: dotProduct = a*c + b*d  + e*f
	modOfVector1 = math.sqrt( a*a + b*b)*math.sqrt(c*c + d*d) 
	# for three dimensional: modOfVector = math.sqrt( a*a + b*b + e*e)*math.sqrt(c*c + d*d +f*f)
	angle = dotProduct/modOfVector1
	angleInDegree = math.degrees(math.acos(angle))
	return angleInDegree


#print(getdistance(2,3,4,5))
#print (centreline(1,1,-1,-1))

