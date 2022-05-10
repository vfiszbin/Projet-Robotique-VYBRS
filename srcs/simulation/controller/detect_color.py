# Import the necessary libraries
from lib2to3.pygram import python_grammar_no_print_statement
from sqlite3 import PARSE_COLNAMES
from PIL import Image
from numpy import asarray
import numpy



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



def detect_RGB_rectangles_in_mask(mask):
	'''Détecte les rectangles (True) dans un mask (composé de True/False)'''
	nb_lines = mask.shape[0]
	nb_cols = mask.shape[1]
	rectangles = []
	for line in range(0, nb_lines):
		for col in range(0, nb_cols):
			previous_line = line
			previous_col = col

			new_col = col

			#tant qu'on détecte la couleur recherchée
			while (line < (nb_lines - 1) and col < (nb_cols - 1) and mask[line][col] == True and check_intersection(rectangles, (line,col)) == False):
				col += 1
				#si la couleur n'est plus présente sur la ligne, passe à la suivante
				if (mask[line][col] == False) :
					line += 1
					new_col = col - 1 #garde jusqu'à quelle coval_minnne on est allé en mémoire
					col = previous_col
					
			
			new_line = line - 1
			if (new_line - previous_line >= 10 and new_col - previous_col >= 10): #si un carré d'une taille suffisante est trouvé
				# print("TROUVE !")
				# print("(" + str(previous_line) + "," + str(previous_col) + ")")
				# print("(" + str(new_line) + "," + str(new_col) + ")")
				rectangles.append( ((previous_line,previous_col), (new_line,new_col)) )


			else : #sinon, on continue la recherche
				line = previous_line
				col = previous_col

	return rectangles

def pick_biggest_rectangle(rectangles):
	'''Choisit le plus grand rectangle parmi les rectangles détectés'''
	biggest_rect = ((0,0),(0,0))
	biggest_rect_surface = 0
	for rect in rectangles:
		y1 = rect[0][0]
		x1 = rect[0][1]

		y2 = rect[1][0]
		x2 = rect[1][1]
		surface = (x2 - x1) * (y2 - y1)
		if surface > biggest_rect_surface:
			biggest_rect = rect
			biggest_rect_surface = surface
	return biggest_rect

###SCANNER QUE LE CENTRE DE LIMAGE POUR LIMITER LES CALCULS ET ASSURER QUE ROBOT FAIT FACE A LOBJET ?
###Calculer moyenne des coordonnées des pixels de la couleur recherchée et voir si c'est au centre ?
###Réduire la qualité de l'image pour avoir moins de pixels



def detect_biggest_RGB_rectangle(image_name, RGB_color):
	'''Retourne le plus grand rectangle de la couleur RGB indiquée détecté dans l'image'''
	img = Image.open(image_name)

	#convertit RGB en HSV pour meilleure détection de couleur
	img_HSV = img.convert('HSV')
	
	#convertit image en numpy array
	np_array = asarray(img_HSV)

	if RGB_color == "R":
		# Degrés correspondants aux pixels rouges 340 < Hue < 20
		val_min, val_max = 340,20
	elif RGB_color == "G":
		# Degrés correspondants aux pixels verts 100 < Hue < 140
		val_min, val_max = 100,140
	elif RGB_color == "B":
		# Degrés correspondants aux pixels bleus 220 < Hue < 260
		val_min, val_max = 220,260
	else:
		print("La couleur doit être R,G ou B")
		return

	# Passage des degrés 0-360 en valeur 0-255
	val_min = int((val_min * 255) / 360)
	val_max = int((val_max * 255) / 360)

	if RGB_color == "R": #cas spécial pour l'intervalle Hue du rouge (autour de 0)
		#Mask (array de True/False) des coordonnées où la couleur apparait
		mask = (np_array[:,:,0] >= 170) & (np_array[:,:,1] >= 70) & (np_array[:,:,2] >= 50) & (np_array[:,:,0] <= 180) & (np_array[:,:,1] <= 255) & (np_array[:,:,2] <= 255)
	else: 
		#Mask (array de True/False) des coordonnées où la couleur apparait
		mask = (np_array[:,:,0] > val_min) & (np_array[:,:,0] < val_max)

	print(mask)
	print(mask.shape)


	# rectangles = detect_RGB_rectangles_in_mask(mask)
	# print(pick_biggest_rectangle(rectangles))


# detect_biggest_RGB_rectangle("test.jpg", "R")


def blockshaped(arr, nrows, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    h, w = arr.shape
    assert h % nrows == 0, f"{h} rows is not evenly divisible by {nrows}"
    assert w % ncols == 0, f"{w} cols is not evenly divisible by {ncols}"
    return (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))




def detect_RGB_rectangle(image_name, RGB_color):
	'''Retourne le plus grand rectangle de la couleur RGB indiquée détecté dans l'image'''
	img = Image.open(image_name)

	#convertit RGB en HSV pour meilleure détection de couleur
	img_HSV = img.convert('HSV')
	
	#convertit image en numpy array
	np_array = asarray(img_HSV)

	print (np_array)
	print (np_array.shape)

	print(np_array.shape)
	
	splits = blockshaped(np_array[0], 50, 50)
	# splits = numpy.array_split(np_array[0], 50)
	
	print(splits.shape)



# detect_RGB_rectangle("rgb.jpg", "R")

np_array = numpy.arange(120).reshape((10, 12))
print (np_array)
print (np_array.shape)

#Nombre de de blocs en lignes/colonnes qu'on souhaite avoir
n_lines = 3
n_col = 2

pas_lines = np_array.shape[0] // n_lines #de combien l'indice doit progresser dans l'image pour passer au bloc suivant
pas_col = np_array.shape[1] // n_col

print("pas_lines = " + str(pas_lines))
print("pas_col = " + str(pas_col))

#Calcule les dimensions que va avoir la matrice contenant les informations sur les blocs de couleur
if np_array.shape[0] % n_lines != 0:
	n_lines_color_blocks = n_lines + 1
else:
	n_lines_color_blocks = n_lines
if np_array.shape[1] % n_col != 0:
	n_col_color_blocks = n_col + 1
else:
	n_col_color_blocks = n_col
color_blocks = numpy.zeros((n_lines_color_blocks, n_col_color_blocks), dtype=object)
print("Shape color_block = " + str(color_blocks.shape))

l = 0
c = 0
l_color_blocks = 0
c_color_blocks = 0
while(l < np_array.shape[0]):
	while(c < np_array.shape[1]):
		print(np_array[l:l+pas_lines, c:c+pas_col])
		print('\n')
		color_blocks[l_color_blocks, c_color_blocks] = ("R", ((l, l+pas_lines), (c, c+pas_col)))

		c += pas_col
		c_color_blocks += 1

	c = 0
	l += pas_lines
	c_color_blocks = 0
	l_color_blocks += 1

print(color_blocks)





