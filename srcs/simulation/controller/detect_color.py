# Import the necessary libraries
from lib2to3.pygram import python_grammar_no_print_statement
from sqlite3 import PARSE_COLNAMES
from PIL import Image
from numpy import asarray
import numpy

TAILLE_MIN_RECT = 1 #taille minimum du rectangle (carre) de blocks de la couleur cherchéè
#Nombre de de blocs en lignes/colonnes qu'on souhaite avoir
N_LINES = 40
N_COL = 40
COLOR = "R"
FICHIER = "test1.jpg"
RATIO_COLOR_IN_BLOCK = 0.5



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



def detect_rectangles(color_blocks):
	'''Détecte les rectangles'''
	nb_lines = color_blocks.shape[0]
	nb_cols = color_blocks.shape[1]
	rectangles = []
	for line in range(0, nb_lines):
		for col in range(0, nb_cols):
			previous_line = line
			previous_col = col

			new_col = col

			#tant qu'on détecte la couleur recherchée
			while (line < (nb_lines - 1) and col < (nb_cols - 1) and color_blocks[line][col] != 0 and check_intersection(rectangles, (line,col)) == False):
				col += 1
				#si la couleur n'est plus présente sur la ligne, passe à la suivante
				if (color_blocks[line][col] == 0) :
					line += 1
					new_col = col - 1 #garde jusqu'à quelle col on est allé en mémoire
					col = previous_col
					
			
			new_line = line - 1
			if (new_line - previous_line >= TAILLE_MIN_RECT and new_col - previous_col >= TAILLE_MIN_RECT): #si un carré d'une taille suffisante est trouvé
				# print("TROUVE !")
				# print("(" + str(previous_line) + "," + str(previous_col) + ")")
				# print("(" + str(new_line) + "," + str(new_col) + ")")
				rectangles.append( ((color_blocks[previous_line,previous_col][1][0][0], color_blocks[previous_line,previous_col][1][0][1]), (color_blocks[new_line,new_col][1][1][0], color_blocks[new_line,new_col][1][1][1])) )


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



# def detect_biggest_rectangle(image_name, RGB_color):
# 	'''Retourne le plus grand rectangle de la couleur RGB indiquée détecté dans l'image'''
# 	img = Image.open(image_name)

# 	#convertit RGB en HSV pour meilleure détection de couleur
# 	img_HSV = img.convert('HSV')
	
# 	#convertit image en numpy array
# 	np_array = asarray(img_HSV)

# 	if RGB_color == "R":
# 		# Degrés correspondants aux pixels rouges 340 < Hue < 20
# 		val_min, val_max = 340,20
# 	elif RGB_color == "G":
# 		# Degrés correspondants aux pixels verts 100 < Hue < 140
# 		val_min, val_max = 100,140
# 	elif RGB_color == "B":
# 		# Degrés correspondants aux pixels bleus 220 < Hue < 260
# 		val_min, val_max = 220,260
# 	else:
# 		print("La couleur doit être R,G ou B")
# 		return

# 	# Passage des degrés 0-360 en valeur 0-255
# 	val_min = int((val_min * 255) / 360)
# 	val_max = int((val_max * 255) / 360)

# 	if RGB_color == "R": #cas spécial pour l'intervalle Hue du rouge (autour de 0)
# 		#Mask (array de True/False) des coordonnées où la couleur apparait
# 		mask = (np_array[:,:,0] >= 170) & (np_array[:,:,1] >= 70) & (np_array[:,:,2] >= 50) & (np_array[:,:,0] <= 180) & (np_array[:,:,1] <= 255) & (np_array[:,:,2] <= 255)
# 	else: 
# 		#Mask (array de True/False) des coordonnées où la couleur apparait
# 		mask = (np_array[:,:,0] > val_min) & (np_array[:,:,0] < val_max)

# 	print(mask)
# 	print(mask.shape)


# 	# rectangles = detect_RGB_rectangles_in_mask(mask)
# 	# print(pick_biggest_rectangle(rectangles))


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
	print (np_array.shape)

	#Nombre de de blocs en lignes/colonnes qu'on souhaite avoir
	n_lines = N_LINES
	n_col = N_COL

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
	color_blocks = numpy.zeros((n_lines_color_blocks, n_col_color_blocks), dtype=object) #matrice contenant les informations de chaque bloc
	print("Shape color_block = " + str(color_blocks.shape))

	#Choisit les valeurs min/max pour détecter la couleur passée en argument
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
		# mask = (np_array[:,:,0] >= 170) & (np_array[:,:,1] >= 70) & (np_array[:,:,2] >= 50) & (np_array[:,:,0] <= 180) & (np_array[:,:,1] <= 255) & (np_array[:,:,2] <= 255)
		mask = (np_array[:,:,0] > val_min) | (np_array[:,:,0] < val_max) & (np_array[:,:,1] >= 50) & (np_array[:,:,2] >= 50)
		print("val_min = " + str(val_min))
		print("val_max = " + str(val_max))
		print("sum_mask = " + str(numpy.sum(mask)))
	else:
		mask = (np_array[:,:,0] > val_min) & (np_array[:,:,0] < val_max)
		print("val_min = " + str(val_min))
		print("val_max = " + str(val_max))
		print("sum_mask = " + str(numpy.sum(mask)))

	l = 0
	c = 0
	l_color_blocks = 0
	c_color_blocks = 0
	while(l < np_array.shape[0]):
		while(c < np_array.shape[1]):

			if mask[l:l+pas_lines, c:c+pas_col].sum() / (pas_lines * pas_col) > RATIO_COLOR_IN_BLOCK:
				color_blocks[l_color_blocks, c_color_blocks] = (RGB_color, ((l, c), (l+pas_lines, c+pas_col))) #enregistre les infos du bloc

			c += pas_col
			c_color_blocks += 1

		c = 0
		l += pas_lines
		c_color_blocks = 0
		l_color_blocks += 1


	rectangles = detect_rectangles(color_blocks)
	biggest_rect = pick_biggest_rectangle(rectangles)
	print(rectangles)
	print(biggest_rect)
	
	



detect_RGB_rectangle(FICHIER, COLOR)

# np_array = numpy.arange(120).reshape((10, 12))
# print (np_array)
# print (np_array.shape)

# #Nombre de de blocs en lignes/colonnes qu'on souhaite avoir
# n_lines = 3
# n_col = 2

# pas_lines = np_array.shape[0] // n_lines #de combien l'indice doit progresser dans l'image pour passer au bloc suivant
# pas_col = np_array.shape[1] // n_col

# print("pas_lines = " + str(pas_lines))
# print("pas_col = " + str(pas_col))

# #Calcule les dimensions que va avoir la matrice contenant les informations sur les blocs de couleur
# if np_array.shape[0] % n_lines != 0:
# 	n_lines_color_blocks = n_lines + 1
# else:
# 	n_lines_color_blocks = n_lines
# if np_array.shape[1] % n_col != 0:
# 	n_col_color_blocks = n_col + 1
# else:
# 	n_col_color_blocks = n_col
# color_blocks = numpy.zeros((n_lines_color_blocks, n_col_color_blocks), dtype=object) #matrice contenant les informations de chaque bloc
# print("Shape color_block = " + str(color_blocks.shape))

# l = 0
# c = 0
# l_color_blocks = 0
# c_color_blocks = 0
# while(l < np_array.shape[0]):
# 	while(c < np_array.shape[1]):
# 		mask = (np_array[l:l+pas_lines, c:c+pas_col] > 0) & (np_array[l:l+pas_lines, c:c+pas_col] < 100)
# 		print(mask)
# 		print('\n')
# 		color_blocks[l_color_blocks, c_color_blocks] = ("R", ((l, c), (l+pas_lines, c+pas_col))) #enregistre les infos du bloc

# 		c += pas_col
# 		c_color_blocks += 1

# 	c = 0
# 	l += pas_lines
# 	c_color_blocks = 0
# 	l_color_blocks += 1

# print(color_blocks)





