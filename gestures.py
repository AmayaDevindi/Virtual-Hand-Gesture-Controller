import mediapipe as m

def detect_gesture(landmarks):
    """
    Detects gestures based on hand landmarks.

    :param landmarks: List of hand landmarks from mediapipe
    :return: Gesture string: "scroll_up", "scroll_down", "thumbs_up", "thumbs_down", "ring", "previous_slide", "next_slide", or "none"
    """

    try:
        thumb_tip = landmarks[m.solutions.hands.HandLandmark.THUMB_TIP]
        thumb_mcp = landmarks[m.solutions.hands.HandLandmark.THUMB_MCP]
        middle_tip = landmarks[m.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP]
        middle_mcp = landmarks[m.solutions.hands.HandLandmark.MIDDLE_FINGER_MCP]
    except (KeyError, IndexError):
        return "none"

    thumb_horizontal = abs(thumb_tip.y - thumb_mcp.y)
    min_thumb_horizontal = 0.04

    if thumb_tip.x < thumb_mcp.x and thumb_horizontal < min_thumb_horizontal:
        return "previous_slide"
    if thumb_tip.x > thumb_mcp.x and thumb_horizontal < min_thumb_horizontal:
        return "next_slide"

    middle_vertical = middle_tip.y - middle_mcp.y

    if middle_vertical < -0.1:
        return "scroll_up"
    if middle_vertical > 0.1:
        return "scroll_down"

    thumb_vertical = abs(thumb_tip.x - thumb_mcp.x)
    min_thumb_vertical = 0.08
    hand_horizontal = abs(middle_tip.y - middle_mcp.y)

    if thumb_tip.y > thumb_mcp.y and thumb_vertical < min_thumb_vertical and hand_horizontal < 0.03:
        return "thumbs_down"
    if thumb_tip.y < thumb_mcp.y and thumb_vertical < min_thumb_vertical and hand_horizontal < 0.02:
        return "thumbs_up"

    return "none"
