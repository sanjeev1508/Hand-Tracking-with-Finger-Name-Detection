# Hand Tracking with Finger Name Detection

## Description
This Python project uses OpenCV and MediaPipe to track hands in real-time and label individual fingers. It detects and identifies the thumb, index, middle, ring, and pinky fingers while displaying the hand landmarks on the webcam feed. The program continuously processes frames from the webcam and overlays finger names on detected fingertips.

## Features
- Real-time hand tracking using MediaPipe
- Labels fingers with their corresponding names
- Draws hand landmarks and connections
- Provides feedback when no hand or fingers are detected
- Uses OpenCV for video processing

## Requirements
Ensure you have the following dependencies installed:

```sh
pip install opencv-python mediapipe
```

## Usage
1. Run the script:
   ```sh
   python hand_tracking.py
   ```
2. Allow access to your webcam.
3. Move your hand in front of the camera to see labeled fingers.
4. Press 'q' to exit the program.

## How It Works
- The script captures video from the webcam.
- Converts the frames to RGB and processes them with MediaPipe's Hand module.
- Identifies the fingertips based on MediaPipe landmark indices.
- Draws circles and labels on detected fingertips.
- Displays real-time video with detected hands and fingers.

## Example Output
The program will display a window with a real-time webcam feed showing:
- A tracked hand with finger landmarks.
- Labels for the detected fingers.
- A message if no hands are detected.

## License
This project is open-source and available under the MIT License.

## Code
```python
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
```

