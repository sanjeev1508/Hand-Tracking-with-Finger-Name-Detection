import cv2
import mediapipe as mp

# Initialize Mediapipe Hand Module
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils  # Utility to draw landmarks
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Finger names corresponding to Mediapipe landmark indices
finger_names = {4: "Thumb", 8: "Index", 12: "Middle", 16: "Ring", 20: "Pinky"}

# Open Webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip image to avoid mirror effect
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape  # Get frame dimensions
    
    # Convert to RGB for Mediapipe processing
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw landmarks and connections
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            detected_fingers = []
            for id in finger_names.keys():  # Check only fingertip landmarks
                lm = hand_landmarks.landmark[id]
                cx, cy = int(lm.x * w), int(lm.y * h)
                detected_fingers.append(finger_names[id])
                cv2.circle(frame, (cx, cy), 8, (0, 255, 0), -1)
                cv2.putText(frame, finger_names[id], (cx - 30, cy - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                            0.6, (255, 0, 0), 2)
            
            # Ensure even a single finger is detected and labeled
            if not detected_fingers:
                cv2.putText(frame, "No fingers detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                            0.8, (0, 0, 255), 2)
    else:
        cv2.putText(frame, "No hand detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.8, (0, 0, 255), 2)
    
    # Display Output
    cv2.imshow("Hand Tracking with Finger Names", frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()