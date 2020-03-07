
import speech_recognition as sr                               #done
from playsound import playsound#done
from scipy.spatial import distance as dist#done
from imutils.video import FileVideoStream#done
from imutils.video import VideoStream#done
from imutils import face_utils#done
import argparse#done
import imutils#done
import time#done
import dlib#done
import cv2#done
import keyboard#done  



def eye_aspect_ratio(eye):
	# compute the euclidean distances between the two sets of
	# vertical eye landmarks (x, y)-coordinates
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])

	# compute the euclidean distance between the horizontal
	# eye landmark (x, y)-coordinates
	C = dist.euclidean(eye[0], eye[3])
	# compute the eye aspect ratio
	ear = (A + B) / (2.0 * C)
	# return the eye aspect ratio
	return ear
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor",default="shape_predictor_68_face_landmarks.dat",
	help="path to facial landmark predictor")
ap.add_argument("-v", "--video", type=str, default="camera",
	help="path to input video file")
ap.add_argument("-t", "--threshold", type = float, default=0.27,
	help="threshold to determine closed eyes")
ap.add_argument("-f", "--frames", type = int, default=2,
	help="the number of consecutive frames the eye must be below the threshold")

def main() :
    args = vars(ap.parse_args())
    EYE_AR_THRESH = args['threshold']
    EYE_AR_CONSEC_FRAMES = args['frames']

    # initialize the frame counters and the total number of blinks
    COUNTER = 0
    TOTAL = 0

    # initialize dlib's face detector (HOG-based) and then create
    # the facial landmark predictor
    print("[INFO] loading facial landmark predictor...")
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(args["shape_predictor"])
 
    # grab the indexes of the facial landmarks for the left and
    # right eye, respectively
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
    print("[INFO] doing initual settings...")
    ear_value = 0.22
    event = True
    search = 0
    searchCount = 0
    Face_mode = 0
    Face_modeLim = 20
    Face_modeKey = False
    targetA = False
    # start the video stream thread
    print("[INFO] starting video stream thread...")
    playsound('Searching.wav')
    targetA = True
    print("[INFO] print q to quit...")
    
    
    if args['video'] == "camera":
        vs = VideoStream(src=0).start()
        fileStream = False
    else:
        vs = FileVideoStream(args["video"]).start()
        fileStream = True
   
    time.sleep(1.0)



    print("[INFO] enter loop")
    # loop over frames from the video stream
    while True:
        
        if keyboard.is_pressed('c'): 
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source)
                text = r.recognize_google(audio)
                print(text)
                if text == "goodbye":
                     print("DEVELOPED BY: SEOUL INC")
                     print("MADEBY ADAM-JJJ")
                     print("     _______  _______  _______           _      TM ")
                     print("    (  ____ |(  ____/ (  ___  )| |    /|( |        ")
                     print("    | (    ||| (      | (   ) || )   ( || (        ")
                     print("    | (_____ | (__    | |   | || |   | || |        ")
                     print("    (_____  )|  __)   | |   | || |   | || |        ")
                     print("          ) || (      | |   | || |   | || |        ")
                     print("     _____) || (______| (___) || (___) || (____/| ")
                     print("    \_______)(_______/(_______)(_______)(_______/  ")
                                             
                     playsound('end_credit.mp3')
                     break
                if text == "f*** you":
                    playsound('Turret_turret_collide_3.wav')
                if text == "I hate you":
                    playsound('Turret_turret_collide_3.wav')

        
       # if key == ord("T"):


        ##############################################
    	# if this is a file video stream, then we need to check if
    	# there any more frames left in the buffer to process
        #if fileStream and not vs.more():
         #   break
    
    	# grab the frame from the threaded video file stream, resize
    	# it, and convert it to grayscale
    	# channels)
        frame = vs.read()
        frame = imutils.resize(frame, width=450)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        if search == 60:
            playsound('TargetLost.wav')
            playsound('Searching.wav')
            targetA = True
            Face_mode = 0
            search = 0
            searchCount += 1 
        search += 1
        if searchCount == 5:
           playsound('Sleep.wav')
           searchCount = 0

    	# detect faces in the grayscale frame
        rects = detector(gray, 0)
        faces = detector(gray)
        #print(Face_mode)
    	# loop over the face detections
        for rect in rects:
            searchCount = 0
            if targetA == True:
                playsound('TargetA.wav')
                targetA = False
            search = 0
            
            if Face_mode == Face_modeLim:
                Face_modeKey = True
            if Face_modeKey == True:
                x, y = rect.left(), rect.top()
                x1, y1 = rect.right(), rect.bottom()
                cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
                if sentrymode == True:
                    playsound('sentry mode activated.wav')
                    sentrymode = False
               
             
    		# determine the facial landmarks for the face region, then
    		# convert the facial landmark (x, y)-coordinates to a NumPy
    		# array
            else:
                sentrymode = True
                shape = predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)
    
    		# extract the left and right eye coordinates, then use the
    		# coordinates to compute the eye aspect ratio for both eyes
                leftEye = shape[lStart:lEnd]
                rightEye = shape[rStart:rEnd]
                leftEAR = eye_aspect_ratio(leftEye)
                rightEAR = eye_aspect_ratio(rightEye)
    
    		# average the eye aspect ratio together for both eyes
                ear = (leftEAR + rightEAR) / 2.0
                if ear < ear_value:
                    Face_mode += 1
                if ear > ear_value:
                    Face_mode =0
    
    		# compute the convex hull for the left and right eye, then
    		# visualize each of the eyes
                leftEyeHull = cv2.convexHull(leftEye)
                rightEyeHull = cv2.convexHull(rightEye)
                cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
                cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
    
    		# check to see if the eye aspect ratio is below the blink
    		# threshold, and if so, increment the blink frame counter
                if ear < EYE_AR_THRESH:
                   COUNTER += 1
    
    		# otherwise, the eye aspect ratio is not below the blink
    		# threshold
                else:
    			# if the eyes were closed for a sufficient number of
    			# then increment the total number of blinks
                    if COUNTER >= EYE_AR_CONSEC_FRAMES:
                        TOTAL += 1
    
    			# reset the eye frame counter
                    COUNTER = 0
    
    		# draw the total number of blinks on the frame along with
    		# the computed eye aspect ratio for the frame
                cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
        			cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
               # print(ear)
     
    	# show the frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
     
    	# if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
    
    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()
if __name__ == '__main__' :
    main()