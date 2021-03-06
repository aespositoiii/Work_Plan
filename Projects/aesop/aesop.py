import numpy as np
import cv2 as cv
from skimage.draw import line

def aesops_Filter(image, kernel_size_start=3, kernel_size_end=3, kernel_step=2, series=False, steps=51):
    
    # Set up the resulting image
    
    result = np.zeros(image.shape, dtype='uint8')

    
    # Set the step size for increasing or decreasing kernel size
    
    if kernel_size_start > kernel_size_end:
        step = -kernel_step
        
    else:
        step = kernel_step
    
    
    # Iterate through the range of kernel sizes
    
    for i in range(kernel_size_start, kernel_size_end+1, step):
        

        
        # Set the end of the range index to be one less than the size 
        
        end = i - 1
        
        
        # Apply the filter to the horizontals, verticals and diagonals
        
        result = _apply_filter(result, image, 0, 0, end, 0)
        result = _apply_filter(result, image, 0, 0, 0, end)
        result = _apply_filter(result, image, 0, 0, end, end)
        result = _apply_filter(result, image, 0, end, end, 0)        
        
        steps_list = np.linspace(0, end, steps+1, dtype='uint8')
        steps_list = np.unique(steps_list)
        
            # Traverse the edges of the square
            
        for a in steps_list[1:]:
            result = _apply_filter(result, image, 0, 0, end, a)
            result = _apply_filter(result, image, end, 0, 0, a)
            result = _apply_filter(result, image, 0, 0, a, end)
            result = _apply_filter(result, image, 0, end, a, 0)

        if series == True :
            image = np.copy(result)
    
    return result

def _apply_filter(result, image, x1, y1, x2, y2):
    
    # Establish the temporary arrays
    
    temp_filtered = np.zeros(image.shape, dtype='uint8')
    temp_dilated = np.zeros(image.shape, dtype='uint8')
    
    
    # Set the dimensions for the kernel shape
    
    kx = np.abs(x2-x1) + 1
    ky = np.abs(y2-y1) + 1
    
    
    # Apply the filter checking for matching perimiter points

    kernel_filter = np.zeros((ky,kx), dtype='uint8')   
    kernel_filter [y1, x1] = 1
    kernel_filter [y2, x2] = 1
    
    temp_filtered = cv.filter2D( image, cv.CV_8U, kernel_filter, anchor=(x1, y1), borderType = cv.BORDER_CONSTANT|0)
    temp_filtered[temp_filtered<2] = 0
    
    
    # Apply the filter connecting matching perimiter points
    
    kernel_dil = np.zeros((ky,kx), dtype='uint8')
    lx, ly = line(x1, y1, x2, y2)
    kernel_dil[ ly, lx ] = 1
    
    temp_dilated = cv.dilate(temp_filtered, kernel_dil, anchor=(x2,y2), borderType = cv.BORDER_CONSTANT|0)
    temp_dilated[temp_dilated>0] = 1

    
    # Add the mask generated by the current iteration to the result
    
    result = np.maximum(result, temp_dilated)


    return result