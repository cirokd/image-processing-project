import sys
import numpy as np
import cv2

defaultFlags = {
    'characters': False,
    'lines': True,
    'paragraphs': True
}

# main image processing function
def process(
    path,
    flags = defaultFlags,
    lineCloseKernelWidth = 40,
    paragraphCloseKernelHeight = 10):

    # (1) read
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # (2) threshold
    th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    # (3) minAreaRect on the nozeros
    pts = cv2.findNonZero(threshed)
    ret = cv2.minAreaRect(pts)

    (cx, cy), (w, h), ang = ret
    if w > h:
        w, h = h, w
        ang += 90

    # (4) Find rotated matrix, do rotation
    M = cv2.getRotationMatrix2D((cx, cy), ang, 1.0)
    rotated = cv2.warpAffine(threshed, M, (img.shape[1], img.shape[0]), borderValue=255)
    rotatedOriginal = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]), borderValue=255)

    if (flags['characters']):
        # (5) Add bounding boxes to characters
        kernel = np.ones((5,1),np.uint8)
        gray = cv2.morphologyEx(rotated, cv2.MORPH_OPEN, kernel)
        # threshold image
        ret, threshed_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        # find contours and get the external one
        image, contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)

        # with each contour, draw boundingRect in red
        for c in contours:
            # get the bounding rect
            x, y, w, h = cv2.boundingRect(c)
            # draw a green rectangle to visualize the bounding rect
            cv2.rectangle(rotatedOriginal, (x, y), (x + w, y + h), (0, 0, 255), 1)

    if (flags['lines']):
        # (6) perform a morph. close to segment the lines
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (lineCloseKernelWidth,1))
        closed = cv2.morphologyEx(rotated, cv2.MORPH_CLOSE, kernel)
        ret, contours, hierarchy = cv2.findContours(closed,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(ret,(x,y),(x+w,y+h),(255,255,255),-1)
            cv2.rectangle(rotatedOriginal,(x,y),(x+w,y+h),(0,255,0),2)

    if (flags['paragraphs']):
        # (7) perform a morph. close to segment the paragraphs
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,paragraphCloseKernelHeight))
        closed = cv2.morphologyEx(ret, cv2.MORPH_CLOSE, kernel)
        ret, contours, hierarchy = cv2.findContours(closed,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(rotatedOriginal,(x,y),(x+w,y+h),(0,0,255),3)

    # (8) rotate the annotated image back to the original angle
    M = cv2.getRotationMatrix2D((cx, cy), -ang, 1.0)
    result = cv2.warpAffine(rotatedOriginal, M, (img.shape[1], img.shape[0]))

    cv2.imshow('result', result)


# when run as a script, the image path comes from a command line argument
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Please provide the image path, e.g:')
        print('$ python process_img.py ./images/sample.png')
    else:
        process(sys.argv[1])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
