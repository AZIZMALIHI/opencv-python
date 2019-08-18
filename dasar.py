import cv2

def baca_img():
	im = cv2.imread('dd.jpg');
	h,w = im.shape[:2]

	new_h, new_w = int(h/4), int(w/4)
	res = cv2.resize(im, (new_w,new_h))

	print(im.shape) #resolusi gambar

	cv2.imshow('res', res)
	cv2.waitKey(0)

def croping():
	img = cv2.imread('dd.jpg');
	
	crop = img[440:520, 730:870]
	cv2.imshow('Resizing', crop)
	cv2.waitKey(0)

def rotating():
	img = cv2.imread('dd.jpg')
	h,w = img.shape[:2]
	center = (w/2, h/2)

	rotate = cv2.getRotationMatrix2D(center, 180, 1)
	rotImg = cv2.warpAffine(img, rotate, (w,h))
	cv2.imshow('Rotating', rotImg)
	cv2.waitKey(0)

def binary():
	img = cv2.imread('images.jpg', 0) #dd.jpg dalam format grayscale(parameter kedua)
	a,thresh = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
	b,thresh_inv = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY_INV)
	c,thresh_trunch = cv2.threshold(img, 125, 255, cv2.THRESH_TRUNC)
	d,thresh_tozero = cv2.threshold(img, 125, 255, cv2.THRESH_TOZERO)
	e,thresh_tozero_inv = cv2.threshold(img, 125, 255, cv2.THRESH_TOZERO_INV)

	cv2.imshow('threshold', thresh)
	cv2.imshow('thresh_inv', thresh_inv)
	cv2.imshow('thresh_trunch', thresh_trunch)
	cv2.imshow('thresh_tozero', thresh_tozero)
	cv2.imshow('thresh_tozero_inv', thresh_tozero_inv)

	cv2.imshow('original', img)
	cv2.waitKey(0)
	cv2.destroyAllWindow()


def video():
	#cap = cv2.VideoCapture(0) #webcam
	cap = cv2.VideoCapture('tes.mp4') #play dari file

	while(True):
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #RGB diubah ke GrayScale

		#cv2.imwrite('tangkapRGB.png', frame) #img disimpan
		#cv2.imwrite('tangkapGRAY.png', gray)

		#cv2.imshow("Hasil capture", gray)
		cv2.imshow("Hasil capture", frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
			cap.release()
			cv2.destroyAllWindow()

def video_save_webcam():
	cap = cv2.VideoCapture(0)
	fourcc = cv2.cv.CV_FOURCC(*'DIVX') #cv2.VideoWriter(['namafile', [nilai fourcc], [nilai fps], [nilai lebar,panjang]])
	out = cv2.VideoWriter('output.avi', fourcc, 5, (640,480))

	raw_input('Tekan enter untuk mulai esc untuk saving dan keluar')

	while(cap.isOpened()):
		ret, frame = cap.read()
		if ret == True:
			frame = cv2.flip(frame, 180) #mengatur drajat
			out.write(frame)
			
			cv2.imshow("Hasil capture", frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
			else:
				break
				cap.release()
				cv2.destroyAllWindow()

if __name__ == '__main__':
	video_save_webcam()