import cv2
from ultralytics import YOLO

VIDEO_FILE = "istockphoto-1167282548-640_adpp_is.mp4"
VIDEO_WIDTH = 845
VIDEO_HEIGHT = 480
MIN_CONFIDENCE = 0.5
MIN_CLASS = 0
PEOPLE_COUNT_TEXT_POSITION = (0, VIDEO_HEIGHT - 10)
PEOPLE_COUNT_TEXT_COLOR = (0, 128, 0)
PEOPLE_COUNT_TEXT_FONT_SCALE = 1
PEOPLE_COUNT_TEXT_THICKNESS = 2

def read_frame(video_capture):
    ret, frame = video_capture.read()
    if not ret:
        return None
    frame=cv2.resize(frame,(VIDEO_WIDTH,VIDEO_HEIGHT))
    return frame

def track_objects(model, frame):
    rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model.track(rgb_img, persist=True, verbose = False)
    return results

def display_results(frame, people_count):
    people_count_text = f"People Count: {len(people_count)}"
    cv2.putText(frame, people_count_text, PEOPLE_COUNT_TEXT_POSITION, cv2.FONT_HERSHEY_SIMPLEX, PEOPLE_COUNT_TEXT_FONT_SCALE,
                PEOPLE_COUNT_TEXT_COLOR, PEOPLE_COUNT_TEXT_THICKNESS)

    cv2.imshow("frame", frame)

def count_people(video_file, model):
    people_count = set()
    video_capture = cv2.VideoCapture(video_file)
    if not video_capture.isOpened():
        print("Error opening video file")
        return

    while True:
        frame = read_frame(video_capture)
        if frame is None:
            break

        results = track_objects(model, frame)
        if results is None or len(results) == 0:
            continue

        if results[0].boxes is not None:
            for i in range(len(results[0].boxes)):
                box = results[0].boxes.xyxy[i]
                score = results[0].boxes.conf[i]
                cls = results[0].boxes.cls[i]
                if score > MIN_CONFIDENCE and cls == 0:
                    people_count.add(i)

        display_results(frame, people_count)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()