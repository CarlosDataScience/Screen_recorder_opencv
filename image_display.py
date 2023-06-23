import cv2


"""
imread() Flasg Argument
cv2.imread_color = 1 : Loads a color image.
cvs.imread_grayscale = 0 : Loads a GrayScale image.
cvs2.imread_unchanged = -1 : Load image as it is.

"""
img = cv2.imread('image.png', 0)
cv2.imshow('Image', img)

key = cv2.waitKey(0)

#With two if we can add the functionality of duplicate with pressing a letter.

if key==27:
    cv2.destroyAllWindows()
    #Also cs2.destroyWindows()

if key== ord('s'):
    cv2.imwrite("Imagen image.png", img) #Duplicate
    cv2.destroyAllWindows()
