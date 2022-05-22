from PIL import Image
from numpy import asarray
import numpy

TAILLE_MIN_RECT = 1 #taille minimum du rectangle (carre) de blocks de la couleur cherchée
#Nombre de blocs en lignes/colonnes qu'on souhaite avoir
# N_LINES = 40
# N_COL = 40
RATIO_LINES_COL = 0.1 #ratio pour obtenir le nombre de lignes/colonnes par qu'on utilise pour subdiviser l'image. ex : taille_verticale_img * ratio = nb_lignes
COLOR = "R"
FICHIER = "test1.jpg"
RATIO_COLOR_IN_BLOCK = 0.5 #le nombre de pixels de la couleur cherchée (parmi toues les pixels du bloc) doit excéder ce ratio pour que le bloc soit considéré comme étant de cette couleur



def check_intersection(rectangles, point, color_blocks):
	'''Vérifie si un point se trouve dans un rectangle'''
	y = color_blocks[point[0],point[1]][1][0][0] #conversion des coordonnées dans color_block en coordonnées de la véritable image
	x = color_blocks[point[0],point[1]][1][0][1]

	for rect in rectangles:
		y1 = rect[0][0]
		x1 = rect[0][1]

		y2 = rect[1][0]
		x2 = rect[1][1]
		

		if x1 <= x <= x2 and y1 <= y <= y2:
			return True
	return False



def detect_rectangles(color_blocks):
	'''Détecte les amas de blocks formant des rectangles et retourne la liste'''
	nb_lines = color_blocks.shape[0]
	nb_cols = color_blocks.shape[1]
	rectangles = []
	for line in range(0, nb_lines):
		for col in range(0, nb_cols):
			previous_line = line
			previous_col = col

			new_col = col

			#tant qu'on détecte la couleur recherchée
			while (line < (nb_lines - 1) and col < (nb_cols - 1) and color_blocks[line][col] != 0 and check_intersection(rectangles, (line,col), color_blocks) == False):
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
	'''Choisit le plus grand rectangle parmi une liste de rectangles'''
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




def detect_RGB_rectangle(image_name, RGB_color):
	'''Retourne le plus grand rectangle de la couleur RGB indiquée détecté dans l'image'''
	img = Image.open(image_name)

	#convertit RGB en HSV pour meilleure détection de couleur
	img_HSV = img.convert('HSV')
	
	#convertit image en numpy array
	np_array = asarray(img_HSV)
	print (np_array.shape)

	#Nombre de blocs en lignes/colonnes qu'on souhaite avoir
	n_lines = int(np_array.shape[0] * RATIO_LINES_COL)
	n_col = int(np_array.shape[1] * RATIO_LINES_COL)

	print("n_lines = " + str(n_lines))
	print("n_col = " + str(n_col))

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
		# Mask (array de True/False) des coordonnées où la couleur apparait
		mask = (np_array[:,:,0] > val_min) | (np_array[:,:,0] < val_max) & (np_array[:,:,1] >= 60) & (np_array[:,:,2] >= 60)
		print("val_min = " + str(val_min))
		print("val_max = " + str(val_max))
		print("sum_mask = " + str(numpy.sum(mask)))
	else:
		mask = (np_array[:,:,0] > val_min) & (np_array[:,:,0] < val_max) & (np_array[:,:,1] >= 60) & (np_array[:,:,2] >= 60)
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
	print(rectangles)
	biggest_rect = pick_biggest_rectangle(rectangles)
	print(biggest_rect)

detect_RGB_rectangle(FICHIER, COLOR)



def getCenterofFrame(img):
	"""fonction qui retourne la postion x,y du centre de la balise"""

	return x,y
