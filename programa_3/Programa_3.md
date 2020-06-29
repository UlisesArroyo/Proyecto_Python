# Programa_3n
* Objetivo

	* Leer una imagen RGB
	* Separar los canales de color en matrices/tensores individuales: R(rojo), G(verde) y B(azul)
	* Guardar como jpg imagenes individuales de sus tres canales. El resultado sera una imagen en escala de grises que representa la intensidad de cada color.
	* Generar una imagen que cobine solo dos canales de color (el faltante debe contener valores cero)
	* Guardar 3 imagenes en RGB (.jpg) con canales faltantes de cada color:

	1.Solo canales R y G, y mandando a ceros el canal B
	2.Solo canales R y B, y mandando a ceros el canal G
	3.Solo canales G y B, y mandando a ceros el canal R

	* El resultado deben ser imagenes a color pero 'raras' debido a la falta de un canal
	* Para este programa pueden usar OpenCV y/o numpy y/o PIL