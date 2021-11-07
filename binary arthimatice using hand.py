import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
# For webcam input:
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
    print('press any key to make input number1:')
    n=input()
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image_height, image_width, _ = image.shape
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                
                fin=''
                if hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y:
                    val1 = 0
                    b1=0
                else:
                    val1 = 1
                    fin ='Index '
                    b1=2**0
                if hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y:
                    val2 = 0
                    b2=0
                else:
                    val2 = 1
                    fin += 'Middle '
                    b2=2**1

                if hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y:
                    val3 = 0
                    b3=0
                else:
                    val3 = 1
                    b3=2**2
                    fin += 'Ring '
                if hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y:
                    val4 = 0
                    b4=0
                else:
                    val4 = 1
                    fin += 'PINKY '
                    b4=2**3
                b0=b1+b2+b3+b4
                val=val1 +val2+val3+val4
                print(val)
                fps= str(val)+' fingers'
                
                cv2.putText(image, (fin), (0, 60), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)








        cv2.imshow('MediaPipe Hands', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break
    print('press any key to make input number2:')
    n=input()
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image_height, image_width, _ = image.shape
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                
                fin=''
                if hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y:
                    val1 = 0
                    b1=0
                else:
                    val1 = 1
                    fin ='Index '
                    b1=2**0
                if hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y:
                    val2 = 0
                    b2=0
                else:
                    val2 = 1
                    fin += 'Middle '
                    b2=2**1

                if hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y:
                    val3 = 0
                    b3=0
                else:
                    val3 = 1
                    b3=2**2
                    fin += 'Ring '
                if hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y:
                    val4 = 0
                    b4=0
                else:
                    val4 = 1
                    fin += 'PINKY '
                    b4=2**3
                b=b1+b2+b3+b4
                val=val1 +val2+val3+val4
                print(val)
                fps= str(val)+' fingers'
                
                cv2.putText(image, (fin), (0, 60), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)








        cv2.imshow('MediaPipe Hands', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break
    print(b0,b)
    inp=input('enter an arthematic operation like 1.sum,2.mul,3.div,4.mod,5.sub  of binary numbers:')
    if inp=="sum":
        print('sum of the numbers :',b0+b)
    if inp=="mul":
        print('mul of the numbers :',b0*b)
    if inp=="div":
        print('div of the numbers :',b0/b)
    if inp=="mod":
        print('mod of the numbers :',b0%b)
    if inp=="sub":
        print('sub of the numbers :',b0-b)
    
cap.release()