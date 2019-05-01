import re
import cv2
import time
import numpy as np
import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
USER = '你的使用者名稱'
PASSWORD = '你的密碼'
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 20)

import cv2
import numpy as np
from PIL import Image
def inverse_color(image, col_range):
 # 讀取圖片，0意味著圖片變為灰度圖
 image = cv2.imread(image, 0)
 # 圖片二值化，100為設定閥值，255為最大閥值，1為閥值型別，當前點值大於閥值，設定為0，否則設定為255。ret是return value縮寫，代表當前的閥值
 ret, image = cv2.threshold(image, 110, 255, 1)
 # 圖片的高度和寬度
 height, width = image.shape
 # 圖片反色處理，原因：上面的處理只能生成白字黑底的圖片，而我們需要的是黑字白底的圖片
 img2 = image.copy()
 for i in range(height):
 for j in range(width):
 img2[i, j] = (255 - image[i, j])
 img = np.array(img2)
 # 對處理後的圖片做擷取
 height, width = img.shape
 new_image = img[0:height, col_range[0]:col_range[1]]
 cv2.imwrite('handle_one.png', new_image)
 image = Image.open('handle_one.png')
 return image
def clear_noise(img):
 # 圖片降噪處理
 x, y = img.width, img.height
 for i in range(x):
 for j in range(y):
 if sum_9_region(img, i, j) < 2:
 # 改變畫素點顏色，白色
 img.putpixel((i, j), 255)
 img = np.array(img)
 cv2.imwrite('handle_two.png', img)
 img = Image.open('handle_two.png')
 return img
def sum_9_region(img, x, y):
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


def auto_login():
 """
 實現網頁自動登陸
 """
 url = 'http://www.quanben9.com/'
 browser.get(url)
 # 查詢登陸按鈕並點選
 button = browser.find_element_by_css_selector('#top1 > div > a:nth-child(3)')
 button.click()
 # 查詢使用者名稱輸入框並輸入使用者名稱
 input_first = browser.find_element_by_name('username')
 input_first.send_keys(USER)
 # 查詢密碼輸入框並輸入密碼
 input_second = browser.find_element_by_name('password')
 input_second.send_keys(PASSWORD)
 # 獲取瀏覽器截圖後，手動定位驗證碼位置，獲得驗證碼截圖
 browser.save_screenshot('Login_page.png')
 photo = Image.open('login_page.png')
 box = (1210, 710, 1360, 755)
 photo.crop(box).save('Verification.png')
 # 對驗證碼進行灰度，二值化處理，而後降噪處理
 handle_verification_code('Verification.png')
 # 對處理後的驗證碼圖片進行識別
 image = Image.open('handle_two.png')
 image.show()
 result = pytesseract.image_to_string(image)
 # 畢竟提供的庫識別能力有限，不一定能完整得到結果，需要對結果進行篩選
 result = re.sub('[a-zA-Z’!"#$%&()*+,-./:;<=>，。?★、…【】《》？“”‘’！[]^_`{|}~]+', '', result.replace(' ', ''), re.S)
 print(result)
 # 判斷識別是否成功
 if len(result) == 4:
 # 獲得驗證碼輸入框並輸入驗證碼資訊
 input_third = browser.find_element_by_name('code')
 input_third.send_keys(result)
 time.sleep(2)
 # 獲得登陸按鈕並點選
 button_2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.main > div > form > ul > li:nth-child(5) > input[type="submit"]')))
 button_2.click()
 time.sleep(5)
 else:
 return auto_login()
def handle_verification_code(img):
 img = inverse_color(img, (0, 160))
 img = clear_noise(img)
 return img
def main():
 auto_login()
if __name__ == '__main__':
 main()
 # 結束程式
 exit()