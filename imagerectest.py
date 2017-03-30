import re
import urllib

from PIL import Image
import pytesseract
from resizeimage import resizeimage
import os
import cv2
import webbrowser
import numpy as np
import urllib2
from bs4 import BeautifulSoup


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

src_path = "C:/Users/John/Pictures/"

#quote_page = 'http://www.google.com/search?btnG=1&q=%s'

#page = urllib2.urlopen(quote_page)

#soup = BeautifulSoup(page, 'html.parser')

#name_box = soup.find('script', attrs={'class': 'html-tag'})

#name = name_box.text.strip() # strip() is used to remove starting and trailing

def get_string(img_path):

    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    cv2.imwrite(src_path + "removed_noise.png", img)

    # Apply threshold to get image with only black and white
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(img_path), config='outputbase digits')

    if not result:
        print ('No text found in image!')
        return False
    else:
        url = 'http://timetable.ait.ie/reporting/textspreadsheet;location;id;%s' % result
        url1 = '%0D%0A?t=location+textspreadsheet&days=1-5&weeks=&periods=3-20&template=location+textspreadsheet'
        result = url + url1
        #result = webbrowser.open_new_tab(url + url1)
        #print ('code is: ' + result.getcode())
    return result

#print '--- Start recognize text from image ---'
#print get_string(src_path + "11.jpg")

#print "------ Done -------"