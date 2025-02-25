import cv2

video_part = "videokj.mp4"
output_folder = "frames_output"

def get_properties(video_part):
    video_capture = cv2.VideoCapture(video_part)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS): {0}".format(fps))
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print("Frame width: {0}, frame height: {1}".format(width, height))


get_properties(video_part)

def get_frames(video_part, output_folder):
    video_capture =  cv2.VideoCapture(video_part)
    frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    print("frame count: {0}".format(frame_count))
    counter = 0
    success = True

    while success:
        success, frame = video_capture.read()
        if success:
            cv2.imwrite("{}/frame{:d}.jpg".format(output_folder, counter), frame)
            counter += 1
def video_lag(video_part):
    output_video_part =  "slow_video.mp4"
    video_capture = cv2.VideoCapture(video_part)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    output_video = cv2.VideoWriter(output_video_part, cv2.VideoWriter_fourcc(*'mp4v'), 20,(width,height))
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        output_video.write(frame)
    video_capture.release()
    output_video.release()

video_lag(video_part)











#get_frames(video_part, output_folder)