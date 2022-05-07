# Import the necessary libraries
from lib2to3.pygram import python_grammar_no_print_statement
from PIL import Image
from numpy import asarray
import numpy


# load the image and convert into
# numpy array
img = Image.open('rgb2.jpg')

# asarray() class is used to convert
# PIL images into NumPy arrays
numpydata = asarray(img)

# <class 'numpy.ndarray'>
print(type(numpydata))

# shape
print(numpydata.shape)


mask = (numpydata[:,:,0] <= 15) & (numpydata[:,:,1] >= 240) & (numpydata[:,:,2] <= 15)
print(mask)
print(mask.shape)

nb_lines = mask.shape[0]
nb_cols = mask.shape[1]

def check_intersection(rectangles, point):
	y = point[0]
	x = point[1]
	for rect in rectangles:
		y1 = rect[0][0]
		x1 = rect[0][1]

		y2 = rect[1][0]
		x2 = rect[1][1]

		if x1 < x < x2 and y1 < y < y2:
			return True
	return False


rectangles = []

for line in range(0, nb_lines):
	for col in range(0, nb_cols):
		previous_line = line
		previous_col = col

		new_col = col
		init = False

		#tant qu'on détecte la couleur recherchée
		while (line < (nb_lines - 1) and col < (nb_cols - 1) and mask[line][col] == True and check_intersection(rectangles, (line,col)) == False):
			# print("col = " + str(col))
			# print("line = " + str(line))
			col += 1
			#si la couleur n'est plus présente sur la ligne, passe à la suivante
			if (mask[line][col] == False) :
				line += 1
				new_col = col - 1 #garde jusqu'à quelle colonne on est allé en mémoire
				col = previous_col

			init = True
				
		
		new_line = line - 1
		# if init == True :
		# 	# print("new_line : " + str(new_line))
		# 	# print("previous_line : " + str(previous_line))
		init = False
		if (new_line - previous_line >= 10 and new_col - previous_col >= 10): #si un carré d'une taille suffisante est trouvé
			print("TROUVE !")
			print("(" + str(previous_line) + "," + str(previous_col) + ")")
			print("(" + str(new_line) + "," + str(new_col) + ")")
			rectangles.append( ((previous_line,previous_col), (new_line,new_col)) )


		else : #sinon, on continue la recherche
			line = previous_line
			col = previous_col


# yr,xr = numpy.where(numpydata[:,:,0] <= 15) #coordinates in red array
# yg,xg = numpy.where(numpydata[:,:,1] >= 240) #coordinates in green array
# yb,xb = numpy.where(numpydata[:,:,2] <= 15) #coordinates in blue array

# #Calcule l'intersection de toutes les coordonnées y RGB
# y_inter = numpy.intersect1d(yr, yg)
# y_inter = numpy.intersect1d(y_inter, yb)

# #Calcule l'intersection de toutes les coordonnées x RGB
# x_inter = numpy.intersect1d(xr, xg)
# x_inter = numpy.intersect1d(x_inter, xb)

# print(y_inter)
# print(y_inter.shape)

# print(x_inter)
# print(x_inter.shape)



# res = numpy.where(mask == True)

# print(res)
# print(res.shape)

# print(res1)
# print(numpydata[res1])
# print(numpydata[res1].shape)

# print(numpydata[:,:,1])
# print(numpydata[:,:,1].shape)

# Get list of X,Y coordinates of red pixels
# Y, X = numpy.where(numpy.all(numpydata==[0,0,255],axis=0))
# print(Y)
# print(X)


