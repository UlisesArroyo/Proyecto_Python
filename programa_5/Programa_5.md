# Programa_5
* Objetivo 
	* 5   	verificar que el programa este usando memoria de cuda con el comando nvidia-smi
			para poder verificar el uso de cuda es necesario usar dos terminales. Una con el programa principal detenido con pdb.set_trace(), y otra con watch nvidia-smi

	* 4_b  	1.	Cargar todas las imagenes de /home/space0/datasets/IPN_hand/segment a la gpu 				usando pytorch
			2. 	Pueden hacerlo de manera recursiva pero deben tener cuidado de no sobreescribir 	las imagenes para que se vea reflejado el peso de todas ellas en total (1 GB 		approx.) en la memoria de la gpu
			3. 	El objetivo de este programa es verificar el incremento de memoria en gpu con 		nvidia-smi, asi que deben tomar captura de la salida de ese comando antes (			pdb.set_trace()) y despues de cargar todas las imagenes
