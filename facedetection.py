import cv2

def face_detection():
    image_path = 'images(5).jpg'

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    if face_cascade.empty():
        print("Error: Could not load face cascade")
        return

    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image")
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_image, 1.1, 5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0), 2)

    cv2.imshow('Detected image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def face_detection_on_cam():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5,  minSize=(30,30))
        for (x,y,m,h) in faces:
            cv2.rectangle(frame,(x,y), (x+m, y+h), (0,255,0), 2)
        cv2.imshow('Face video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()

face_detection_on_cam()

