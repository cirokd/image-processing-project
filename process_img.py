import sys
import numpy as np
import cv2

# main image processing function
def process(path):
    img = cv2.imread(path, 0)
    cv2.imshow('image', img)



# when run as a script, the image path comes from a command line argument
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Please provide the image path, e.g:')
        print('$ python process_img.py ./images/sample.png')
    else:
        process(sys.argv[1])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
