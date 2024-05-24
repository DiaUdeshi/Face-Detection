import cv2
    
def detect_bounding_box(vid,face_classifier):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

def perform(input_video):
    video_capture = cv2.VideoCapture(input_video)
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    width=int(video_capture.get(3))
    height=int(video_capture.get(4))
    size=(width,height)
    result1=cv2.VideoWriter("detected/detected"+input_video,cv2.VideoWriter_fourcc(*'X264'),30,size)
    while True:
        result, video_frame = video_capture.read()
        if result is False:
            break
        faces = detect_bounding_box(video_frame,face_classifier)
        result1.write(video_frame)
    print("Done")
        


#input_video="video.mp4"
#perform(input_video)
