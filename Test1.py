# This statement will print hello world
print("Hello World")
print("Change by Jeevan0023")
"""This is a multiple line comment statement
    This is the second line 
    and this is the third"""
print("Multiple comment lines skipped")
print("Multiple comment lines skipped")
print("Multiple comment lines skipped")
print("Multiple comment lines skipped by Bishal")
print("Multiple comment lines skipped by Bishal Sahoo")

print("chnages by pravakar")

print("Changes by Neha")

x = 2
x += 10
x = x*2
print(x)

def cropImage(self, img):
        grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _,thresholded = cv2.threshold(grayscale, 0, 255, cv2.THRESH_OTSU)
        #cv2.imwrite("otsu.png", thresholded)
        bbox = cv2.boundingRect(thresholded)
        x, y, w, h = bbox
        #print(bbox)
        croppedImg = img[y:y+h, x:x+w]
        return croppedImg

