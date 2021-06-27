#import the required libraries including OpenCV
import cv2
#image processing utility functions
#install by running - pip install imutils
import imutils

#Get the images you want to compare.
original = cv2.imread("CodeDeepAI-home.png")
new = cv2.imread("CodeDeepAI-home-1.png")
#resize the images to make them small in size. A bigger size image may take a significant time
#more computing power and time
original = imutils.resize(original, height = 600)
new = imutils.resize(new, height = 600)

#create a copy of original image so that we can store the
#difference of 2 images in the same
diff = original.copy()
cv2.absdiff(original, new, diff)

#converting the difference into grascale images
gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

#increasing the size of differernces so we can capture them all
for i in range(0, 3):
	dilated = cv2.dilate(gray.copy(), None, iterations= i+ 1)


#threshold the gray image to binary it. Anything pixel that has
#value higher than 3 we are converting to white
#(remember 0 is black and 255 is exact white)
#the image is called binarised as any value lower than 3 will be 0 and
# all of the values equal to and higher than 3 will be 255
(T, thresh) = cv2.threshold(dilated, 3, 255, cv2.THRESH_BINARY)

# nicely fiting a bounding box to the contour
cnts = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the contours and draw a bounding rectangle on the changes
# we are using the new image as reference to show where web page has changed
for c in cnts:
	# fit a bounding box to the contour
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(new, (x, y), (x + w, y + h), (0, 255, 0), 2)

#remove comments from below 2 lines if you want to
#for viewing the image press any key to continue
#simply write the identified changes to the disk
cv2.imwrite("changes.png", new)


"""

 # loop over the contours
for c in cnts:
# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.05 * peri, True)

# if the approximated contour has 4 vertices, then we are examining
# a rectangle
	image = img2
	if len(approx) >= 1:
	# draw the outline of the contour and draw the text on the image
		cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
		(x, y, w, h) = cv2.boundingRect(approx)
		#cv2.putText(image, "Rectangle", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

 # show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
"""

#mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
#threshold = 1
#imask =  mask > threshold

#canvas = np.zeros_like(img2, np.uint8)
#canvas[imask] = img2[imask]

#cv2.imwrite("result.png", canvas)

#cv2.imshow("Result",canvas)
#cv2.waitKey(0)

