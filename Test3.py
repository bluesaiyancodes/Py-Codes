if __name__ == '__main__':
    n = int(input())
    #for i in range(1,n+1):
    #    print(i, end='')

    b = ''

    for i in range(1,n+1):
        b = b + str(i)

    print(b)
    print(type(b))
    
    def cropImage(self, img):
        grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _,thresholded = cv2.threshold(grayscale, 0, 255, cv2.THRESH_OTSU)
        #cv2.imwrite("otsu.png", thresholded)
        bbox = cv2.boundingRect(thresholded)
        x, y, w, h = bbox
        #print(bbox)
        croppedImg = img[y:y+h, x:x+w]
        return croppedImg
