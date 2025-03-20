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



