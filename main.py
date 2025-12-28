import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import random

# Initialize camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Initialize hand detector
detector = HandDetector(maxHands=1, detectionCon=0.8)

# Game variables
timer = 0
stateResult = False
startGame = False
scores = [0, 0]  # [AI, Player]
initialTime = 0
playerMove = None
aiMove = None

while True:
   
    # to load and resize background
    imgBG = cv2.imread("data/bg.png")
    if imgBG is None:
        print("Error: bg.png not found in data folder!")
        break
    imgBG = cv2.resize(imgBG, (1280, 720))


    cv2.putText(imgBG, "Press 'Q' to Quit", (400, 150), 
                cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), 5)
    
    # webcam
    success, img = cap.read()
    if not success:
        print("Error: Cannot read from camera!")
        break
    
    #  mirror effect
    img = cv2.flip(img, 1)
    
    # crop center of webcam
    h, w, _ = img.shape
    imgCrop = img[:, int(w*0.2):int(w*0.8)]
    
    # resize to PLAYER box size
    imgScaled = cv2.resize(imgCrop, (450, 380))
    
    # to find Hands
    hands, imgScaled = detector.findHands(imgScaled, draw=True, flipType=False)
    
    #  logic
    if startGame:
        if not stateResult:
            # countdown 
            timer = time.time() - initialTime
            
            # Display countdown
            if timer < 3:
                countdown = 3 - int(timer)
                cv2.putText(imgBG, str(countdown), (600, 390), 
                           cv2.FONT_HERSHEY_PLAIN, 6, (0, 255, 255), 10)
            else:
                cv2.putText(imgBG, "SHOW!", (520, 450), 
                           cv2.FONT_HERSHEY_PLAIN, 6, (0, 255, 0), 8)
            
            # After 3 seconds, capture the move
            if timer > 3.5:
                stateResult = True
                timer = 0
                
                # Detect player move
                if hands:
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    print(f"Fingers detected: {fingers}")
                    
                    # Rock = fist (all fingers down)
                    if fingers == [0, 0, 0, 0, 0] or fingers == [1, 0, 0, 0, 0]:
                        playerMove = 1
                    # Paper = all fingers up
                    elif fingers == [1, 1, 1, 1, 1] or sum(fingers) >= 4:
                        playerMove = 2
                    # Scissor = index and middle finger up
                    elif fingers == [0, 1, 1, 0, 0] or fingers == [1, 1, 1, 0, 0]:
                        playerMove = 3
                    else:
                        playerMove = None
                else:
                    playerMove = None
                
                # Generate AI move
                aiMove = random.randint(1, 3)
                print(f"Player: {playerMove}, AI: {aiMove}")
                
                # Calculate winner
                if playerMove is not None:
                    # Player wins
                    if (playerMove == 1 and aiMove == 3) or \
                       (playerMove == 2 and aiMove == 1) or \
                       (playerMove == 3 and aiMove == 2):
                        scores[1] += 1
                    # AI wins
                    elif (playerMove == 3 and aiMove == 1) or \
                         (playerMove == 1 and aiMove == 2) or \
                         (playerMove == 2 and aiMove == 3):
                        scores[0] += 1
                    # Tie - no score change
    
    # Display AI move
    if stateResult and aiMove is not None:
        try:
            # Map moves: 1=Rock, 2=Paper, 3=Scissor
            move_names = {1: 'rock', 2: 'paper', 3: 'scissor'}
            imgAI = cv2.imread(f'data/{move_names[aiMove]}.png', cv2.IMREAD_UNCHANGED)
            
            if imgAI is not None:
                # Resize AI image to fit the box
                imgAI = cv2.resize(imgAI, (300, 300))
                imgBG = cvzone.overlayPNG(imgBG, imgAI, (129, 250))
            else:
                # Fallback: display text if image not found
                cv2.putText(imgBG, move_names[aiMove].upper(), (180, 450), 
                           cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5)
        except Exception as e:
            print(f"Error loading AI image: {e}")
            cv2.putText(imgBG, "AI", (250, 450), 
                       cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5)
    
    imgBG[220:220+380, 776:776+450] = imgScaled
    
    cv2.putText(imgBG, str(scores[0]), (440, 215), 
               cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 8)
    cv2.putText(imgBG, str(scores[1]), (1150, 215), 
               cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 8)
    
    if not startGame:
        cv2.putText(imgBG, "Press 'S' to Start", (400, 650), 
                   cv2.FONT_HERSHEY_PLAIN, 4, (0, 255, 0), 5)
    elif stateResult:
        cv2.putText(imgBG, "Press 'S' for Next Round", (350, 650), 
                   cv2.FONT_HERSHEY_PLAIN, 4, (0, 255, 0), 5)
    
    cv2.imshow("Rock Paper Scissor", imgBG)
    
    # key controls
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
    elif key == ord('s'):
        startGame = True
        initialTime = time.time()
        stateResult = False
        playerMove = None
        aiMove = None
    elif key == ord('r'):
        # Reset scores
        scores = [0, 0]
        startGame = False
        stateResult = False

cap.release()
cv2.destroyAllWindows()