import cv2
import mediapipe as mp


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
np_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    frame_rgb= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            np_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        x,y = int(index_finger_tip.x * frame.shape[1]), int(index_finger_tip.y * frame.shape[0])

        thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]

        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        if thumb_tip.y < thumb_ip.y and index_tip.y < index_tip.x:
            cv2.putText(frame, "Thumbs up!", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        elif thumb_tip.y > thumb_ip.y and index_tip.y > index_tip.x:
            cv2.putText(frame, "Thumbs down!", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 10, (0,0,255),2)

    cv2.imshow("hand Trackling", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()