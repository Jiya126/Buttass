import cv2
import pytesseract as pyt

# read text from image
def ocr(img):
    text = pyt.image_to_string(img)
    return text

# process image for feeding as input to read text
def preprocess(img):
    cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.GaussianBlur(img,(5,5),0)
    cv2.threshold(img,0,255,cv2.THRESH_BINARY)
    cv2.medianBlur(img,5)
    return img


cap = cv2.VideoCapture(0)
while(1):
    ret, img = cap.read()
    img = preprocess(img)
    text = ocr(img)
    cv2.imshow('frame', img)
    print(text)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        cap.release()
        break
cv2.destroyAllWindows()
