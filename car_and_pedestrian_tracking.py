
import cv2
"""
#our image
img_file = 'car image.png'

#our pre-trained car classifier
classifier_file = 'car_detector.xml'

# create opencv image
img = cv2.imread(img_file)

# convert to grayscale (needed for haar cascade)
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# create car classifier
car_tracker = cv2.CascadeClassifier(classifier_file)   

# detect cars 
cars = car_tracker.detectMultiScale(black_n_white)

# draw rectangles around car
    #car6 = cars[7]
     #(x, y, w, h) = car6
for (x, y, w, h) in cars:
   cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)

# display the image with faces spotted
cv2.imshow('Clever Programmer Car Detector', img)

# Dont autoclose (wait here in the code and listen for a key press)
cv2.waitKey()
"""

#Our Video
#video = cv2.VideoCapture('Tesla dashcam.mp4')
video = cv2.VideoCapture('Pedestrian Crossing.mp4')

#our pre-trained car classifier
car_classifier = 'car_detector.xml'

#Our pre-trained pedestrian classifier
pedestrian_classifier = 'haarcascade_fullbody.xml'

# create car & pedestrian classifier
car_tracker1 = cv2.CascadeClassifier(car_classifier)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_classifier)



# Run forever until car stops or something
while True:
     
    # Read the current frame
     (read_successful, frame) = video.read()

     
    # Safe coding
     if read_successful:
         # Must convert to grayscale
         grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     else:
         break    

     
     # detect cars 
     cars = car_tracker1.detectMultiScale(grayscaled_frame)   
     pedestrian = pedestrian_tracker.detectMultiScale(grayscaled_frame)

     # Draw rectangles around the cars pedestrians
     for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
     for (x, y, w, h) in pedestrian:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255), 2)   

     # display the image with faces spotted
     cv2.imshow('Car Detector', frame)

     # Dont autoclose (wait here in the code and listen for a key press)
     key = cv2.waitKey(5)   

     # Stop if Q key is pressed
     if key==81 or key==113:
         break

# Release the VideoCapture object
video.release()

print("code completed")