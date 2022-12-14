import cv2
import pytesseract as pyt

# example data
A = [[("RB00001-GS1222", 1),("RB00002-GS1222", 1),("RB00003-GS1122", 1),("RC00004-GP0922", 0),("RC00005-GS0922", 1),("RE00006-SS1122", 1)],
          [("ES00010-YG1022", 1),("ES00012-YG0522", 1),("ED00007-GS0922", 0),("ED00009-WG1022", 1),("EJ00018-GS0622", 1),("EJ00020-GS1122", 0)],
          [("BC00022-YG1022", 0),("BC00015-YG0123", 1),("BC00014-GS0922", 1),("BC00008-RG1122", 1),("BO00028-GS0223", 1),("BF00027-YG1022", 1)],
          [("NP00030-GS0523", 1),("NP00032-GS0522", 1),("NC00031-DS0223", 0),("NC00036-GS0423", 1),("NC00037-DG0422", 1),("NC00039-GS0422",0)]]


# read text from image
def ocr(img):
    text = pyt.image_to_string(img)
    return text

# process image for feeding as input to read text
def preprocess(img):
    cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.GaussianBlur(img,(5,5),0)
    cv2.threshold(img,0,255,cv2.THRESH_BINARY)
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    # opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    # img = 255 - opening
    # cv2.medianBlur(img,5)
    return img

# add sku code to example data
def addItem(text):
    if text == '':
        return A
    else:
        if text[0] == 'R':
            A[0].append((text, 1))
        elif text[0] == 'E':
            A[1].append((text, 1))
        elif text[0] == 'B':
            A[2].append((text, 1))
        elif text[0] == 'N':
            A[3].append((text, 1))
        else:
            A.append([(text,1)])
        return A


cntr = 0
cap = cv2.VideoCapture(0)
while(1):
    ret, img = cap.read()
    cntr = cntr+1;
    if((cntr%60)==0):
        img = preprocess(img)
        text = ocr(img)

#         display text detected on image
        iw,ih,_ = img.shape
        x1,y1,w1,h1 = 0,0,iw,ih
        imgbox = pyt.image_to_boxes(img)
        for boxes in imgbox.splitlines():
            boxes = boxes.split(' ')
            x,y,w,h = int(boxes[1]), int(boxes[2]), int(boxes[3]), int(boxes[4])
            cv2.rectangle(img, (x, ih+y), (w, ih+h), (0,0,255), 3)

            cv2.putText(img, text, (x1+int(w1/50), y1+int(h1/50)), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 2)
        
        
        cv2.imshow('frame', img)
        # print(text)

        A = addItem(text)
        # print(A)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            cap.release()
            break
cv2.destroyAllWindows()
