import cv2 as cv
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as drawing
import mediapipe.python.solutions.drawing_styles as drawing_styles
import pyautogui as gui
import time
from gestures import detect_gesture

hands = mp_hands.Hands(
    static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7
)

cam = cv.VideoCapture(0)


active = True
last_gesture_time = 0
GESTURE_COOLDOWN = 2  # cooldown period in seconds

while cam.isOpened():
    success, frame = cam.read()
    if not success:
        print("Camera Frame not available")
        break

    frame = cv.flip(frame, 1)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            gesture = detect_gesture(hand_landmarks.landmark)

            if gesture == "thumbs_down" and active:
                active = False
                print("Process on hold!")

            if gesture == "thumbs_up" and not active:
                active = True
                print("Process active!")

            if active:
                if gesture == "scroll_down":
                    gui.scroll(-40)
                    print("Scroll down!")
                elif gesture == "scroll_up":
                    gui.scroll(40)
                    print("Scroll up!")
                if time.time() - last_gesture_time > GESTURE_COOLDOWN:
                    if gesture == "next_slide":
                        gui.press("right")
                        print("Next Slide!")
                        last_gesture_time = time.time()
                    elif gesture == "previous_slide":
                        gui.press("left")
                        print("Previous Slide!")
                        last_gesture_time = time.time()

            drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                drawing_styles.get_default_hand_landmarks_style(),
                drawing_styles.get_default_hand_connections_style(),
            )

    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    status_text = "Process Active" if active else "Process Hold"
    status_color = (0, 255, 0) if active else (0, 0, 255)
    cv.putText(
        frame, status_text, (20, 40), cv.FONT_HERSHEY_SIMPLEX, 1, status_color, 3
    )

    cv.imshow("VHGC", frame)

    if cv.waitKey(1) == 27:
        break

cam.release()
cv.destroyAllWindows()


