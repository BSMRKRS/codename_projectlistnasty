import directionlibrary as dl
import keyboardControl as kc



while True:
	if FRONT == 0:
		dl.forward()
	elif FRONT == 1 and LEFT == 0:
		dl.left()