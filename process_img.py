import sys
import numpy as np
import cv2

# main image processing function
def process(path):
    img = cv2.imread(path, 0)

    ret,img2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

    # kernel = np.ones((5,5), np.uint8)
    kernel = np.matrix('0 0 0; 1 1 1; 0 0 0', np.uint8)
    img3 = cv2.dilate(img2, kernel, iterations=3)
    img4 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    cv2.imshow('view', img3)



# when run as a script, the image path comes from a command line argument
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Please provide the image path, e.g:')
        print('$ python process_img.py ./images/sample.png')
    else:
        process(sys.argv[1])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
