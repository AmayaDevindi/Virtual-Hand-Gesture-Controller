# Virtual Hand Gesture Controller

#### Video Demo: https://youtu.be/9WjxP2HL_PY

#### Description:
This project lets you use your hand gestures to control things on your computer, like scrolling through pages or moving through presentation slides. You can interact with your computer without touching it, using a webcam to track your hand movements.

This project uses **OpenCV** for webcam input, **MediaPipe** for real-time hand gesture detection, and **PyAutoGUI** to map hand gestures to computer actions. It’s ideal for hands-free control during presentations or when avoiding direct contact with a keyboard or mouse.

## Project Files  
### `project.py`  
This is the main program. It connects to the webcam, detects gestures, and uses **PyAutoGUI** to perform actions based on the gestures.  

### `gestures.py`  
This file detects specific hand gestures. It identifies custom gestures and sends the results to `project.py` to execute actions.  

## Design Choices  
### Custom Gestures  
I chose custom gestures because they are easy to detect and don’t look like normal hand movements. This helps the program avoid mistaking regular hand movements for commands.  

## **What It Can Do**
1. **Hand Tracking**:
   - It can detect and track one of your hands at a time using your webcam.

2. **Gestures You Can Use**:
   - **Thumbs Down**: Pause the program.
   - **Thumbs Up**: Resume the program.
   - **Thumb Up (Fingers Up/Down)**: Scroll through pages or content vertically (up or down).
   - **Thumb to the Right/Left**: Navigate slides in a presentation, moving to the next slide (right) or the previous slide (left).

3. **Process Indicator**:
   - Shows if the program is active or paused in the video feed (green means active, red means paused).

## **How It Works**
1. The program activates your webcam, detects your hands, and selects one hand to track and interpret gestures.
2. It figures out what gesture you’re doing using the positions of your fingers.
3. Based on your gesture, it controls your computer (like scrolling or switching slides).

## **How to Use**
- Make sure your webcam is working.
- Install Python libraries: `pip install opencv-python mediapipe pyautogui
`
- Run the program: `python project.py`.
- Use these gestures.

## **What You Need**
- Python 3.x installed.
- A webcam for the hand tracking to work.

## **Things to Keep in Mind**
- It works best in good lighting.
- Sometimes it might not detect the gesture correctly if your hand isn’t positioned well.
- If your hand is too far from the camera, it may not be detected.

## **What I’d Like to Add Later**
- More gestures for other computer actions.
- Make it work better in low-light situations and at far distances from the camera.
