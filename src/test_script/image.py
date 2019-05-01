from PIL import Image
import cv2
import numpy as np
import pytesseract


def handle_verification_code(self, img):
	img1 = self.inverse_color(img, (0, 160))
	img2 = self.clear_noise(img1)
	return img2
def inverse_color(self, image, col_range):
	# 讀取圖片，0意味著圖片變為灰度圖
	image = cv2.imread(image, 0)
	# 圖片二值化，100為設定閥值，255為最大閥值，1為閥值型別，當前點值大於閥值，設定為0，否則設定為255。ret是return value縮寫，代表當前的閥值
	ret, image = cv2.threshold(image, 110, 255, 1)
	# 圖片的高度和寬度
	height, width = image.shape
	print(height, width)
	# 圖片反色處理，原因：上面的處理只能生成白字黑底的圖片，而我們需要的是黑字白底的圖片
	img2 = image.copy()
	for i in range(height):
		for j in range(width):
			img2[i, j] = (255 - image[i, j])
	img = np.array(img2)
	# 對處理後的圖片做擷取
	height, width = img.shape
	new_image = img[0:height, 0:width]
	cv2.imwrite('handle_one.png', new_image)
	image = Image.open('handle_one.png')
	#image.show()
	return image
def clear_noise(self, img):
	# 圖片降噪處理
	x, y = img.width, img.height
	for i in range(x):
		for j in range(y):
			if self.sum_9_region(img, i, j) < 2:
				# 改變畫素點顏色，白色
				img.putpixel((i, j), 255)
	img = np.array(img)
	cv2.imwrite('handle_two.png', img)
	img = Image.open('handle_two.png')
	img.show()
	return img
def sum_9_region(self, img, x, y):
	"""
	田字格
	"""
	# 獲取當前畫素點的顏色值
	cur_pixel = img.getpixel((x, y))
	width = img.width
	height = img.height
	if cur_pixel == 255: # 如果當前點為白色區域,則不統計鄰域值
		return 10
	if y == 0: # 第一行
		if x == 0: # 左上頂點,4鄰域
			# 中心點旁邊3個點
			sum_1 = cur_pixel + img.getpixel((x, y + 1)) + img.getpixel((x + 1, y)) + img.getpixel((x + 1, y + 1))
			return 4 - sum_1 / 255
		elif x == width - 1: # 右上頂點
			sum_2 = cur_pixel + img.getpixel((x, y + 1)) + img.getpixel((x - 1, y)) + img.getpixel((x - 1, y + 1))
			return 4 - sum_2 / 255
		else: # 最上非頂點,6鄰域
			sum_3 = img.getpixel((x - 1, y)) + img.getpixel((x - 1, y + 1)) + cur_pixel + img.getpixel((x, y + 1)) + img.getpixel((x + 1, y)) + img.getpixel((x + 1, y + 1))
			return 6 - sum_3 / 255
	elif y == height - 1: # 最下面一行
		if x == 0: # 左下頂點
			# 中心點旁邊3個點
			sum_4 = cur_pixel + img.getpixel((x + 1, y)) + img.getpixel((x + 1, y - 1)) + img.getpixel((x, y - 1))
			return 4 - sum_4 / 255
		elif x == width - 1: # 右下頂點
			sum_5 = cur_pixel + img.getpixel((x, y - 1)) + img.getpixel((x - 1, y)) + img.getpixel((x - 1, y - 1))
			return 4 - sum_5 / 255
		else: # 最下非頂點,6鄰域
			sum_6 = cur_pixel + img.getpixel((x - 1, y)) + img.getpixel((x + 1, y)) + img.getpixel((x, y - 1)) + img.getpixel((x - 1, y - 1)) + img.getpixel((x + 1, y - 1))
			return 6 - sum_6 / 255
	else: # y不在邊界
		if x == 0: # 左邊非頂點
			sum_7 = img.getpixel((x, y - 1)) + cur_pixel + img.getpixel((x, y + 1)) + img.getpixel((x + 1, y - 1)) + img.getpixel((x + 1, y)) + img.getpixel((x + 1, y + 1))
			return 6 - sum_7 / 255
		elif x == width - 1: # 右邊非頂點
			sum_8 = img.getpixel((x, y - 1)) + cur_pixel + img.getpixel((x, y + 1)) + img.getpixel((x - 1, y - 1)) + img.getpixel((x - 1, y)) + img.getpixel((x - 1, y + 1))
			return 6 - sum_8 / 255
		else: # 具備9領域條件的
			sum_9 = img.getpixel((x - 1, y - 1)) + img.getpixel((x - 1, y)) + img.getpixel((x - 1, y + 1)) + img.getpixel((x, y - 1)) + cur_pixel + img.getpixel((x, y + 1)) + img.getpixel((x + 1, y - 1)) + img.getpixel((x + 1, y)) + img.getpixel((x + 1, y + 1))
			return 9 - sum_9 / 255

if __name__ == '__main__':
	Image.open('Verification.png').show()
	# 對驗證碼進行灰度，二值化處理，而後降噪處理
	self.handle_verification_code('Verification.png')
	#self.handle_verification_code(newphoto)
	# 對處理後的驗證碼圖片進行識別
	image = Image.open('handle_two.png')
	result = pytesseract.image_to_string(image)
	# 畢竟提供的庫識別能力有限，不一定能完整得到結果，需要對結果進行篩選
	result = re.sub('[a-zA-Z’!"#$%&()*+,-./:;<=>，。?★、…【】《》？“”‘’！[]^_`{|}~]+', '', result.replace(' ', ''), re.S)
	print(result)
