import cv2


img = cv2.imread('image.png', 1)
cv2.imshow('Image', img)


"""
Notes: Is BGR not RGB / don't use black and withe images and colorful lines.

cv2.line(image variable, 
    start cordinates(X,Y), 
    end cordinates(X, Y), 
    color in BGR format (B, G, R),
    thickness)
"""
img= cv2.line(img, (0,0), (255,255), (0,0,255), 5)
img= cv2.arrowedLine(img, (0,255), (255,255), (0,255,0), 5)
img= cv2.rectangle(img, (255,255), (500,500), (0,255,0), 5) #If thickness -1 filled rectangle

#Circle img, center, radius, color, thickness.
img= cv2.circle(img, (400,70), 60, (0,0,255), 5)

"""
putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) -> img

@brief Draws a text string.

The function cv::putText renders the specified text string in the image. 
Symbols that cannot be rendered using the specified font are replaced by question marks. 
See #getTextSize for a text rendering code example.

@param img Image.

@param text Text string to be drawn.

@param org Bottom-left corner of the text string in the image.

@param fontFace Font type, see #HersheyFonts.

@param fontScale Font scale factor that is multiplied by the font-specific base size.

@param color Text color.

@param thickness Thickness of the lines used to draw a text.

@param lineType Line type. See #LineTypes

@param bottomLeftOrigin When true, the image data origin is at the bottom-left corner. 
Otherwise, it is at the top-left corner.
"""
font=cv2.FONT_ITALIC
img= cv2.putText(img, "My image", (10,500),font,4,(0,0,255),10,cv2.LINE_AA)


key = cv2.waitKey(0)

#With two if we can add the functionality of duplicate with pressing a letter.

if key==27:
    cv2.destroyAllWindows()
    #Also cs2.destroyWindows()

if key== ord('s'):
    cv2.imwrite("Imagen image.png", img) #Duplicate
    cv2.destroyAllWindows()
