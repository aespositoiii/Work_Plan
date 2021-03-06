"""
@file laplace_demo.py
@brief Sample code showing how to detect edges using the Laplace operator
"""
import sys
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import time

def main(argv):
    # [variables]
    # Declare the variables we are going to use
    t1 = time.time()
    ddepth = cv.CV_16S
    kernel_size = 3
    window_name = "Laplace Demo"
    # [variables]

    # [load]
    imageName = argv[0] if len(argv) > 0 else '/Users/anthonyesposito/Pictures/macroni/Rosasite_w_Conacalcite/1/JPG/ExportDSCF69422022-43-14.jpg'

    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR) # Load an image

    # Check if image is loaded fine
    if src is None:
        print ('Error opening image')
        print ('Program Arguments: [image_name -- default lena.jpg]')
        return -1
    # [load]

    # [reduce_noise]
    # Remove noise by blurring with a Gaussian filter
    src = cv.GaussianBlur(src, (3, 3), 0)
    # [reduce_noise]
 
    # [convert_to_gray]
    # Convert the image to grayscale
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    # [convert_to_gray]

    # Create Window
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

    # [laplacian]
    # Apply Laplace function
    dst = cv.Laplacian(src_gray, ddepth, ksize=kernel_size)
    #dst = dst**2
    # [laplacian]

    # [convert]
    # converting back to uint8
    abs_dst = cv.convertScaleAbs(dst)
    #ret,abs_dst_disp = cv.threshold(abs_dst,np.median(abs_dst[abs_dst>10])+np.std(abs_dst[abs_dst>10]),255,cv.THRESH_TOZERO)
    
    
    #plt.hist(abs_dst[abs_dst>0].ravel(),256,[0,256]); plt.show()
    # [convert]
    print(abs_dst.max())
    print(abs_dst.min())
    print(np.unique(abs_dst).shape)

    abs_dst = (abs_dst/(np.percentile(abs_dst[abs_dst>0], 10)))**1.5
    abs_dst = (abs_dst/abs_dst.max())*255
    abs_dst = abs_dst.astype('uint8')

    # [display]
    cv.imshow(window_name, abs_dst)
    print(src.shape, '\n\n', abs_dst.shape)
    cv.waitKey(100)
   
   

    # [display]
    ind = 0
    
    for i in range(5):
        abs_dst = cv.GaussianBlur(abs_dst, (151,151),0)
        abs_dst = (abs_dst/abs_dst.max())*255
        abs_dst = abs_dst.astype('uint8')

    print(time.time()-t1)

    cv.imshow('window', abs_dst)
    c = cv.waitKey(5000)
    
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
