import cv2
import main
camera = cv2.VideoCapture("challenge.mp4")

# Output 'video file may be with another extension, but I didn't try
# output_file = 'Your path to output video file' + '.avi'
output_file = "out.avi"

# 4-byte code of the video codec may be another, but I did not try
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

is_begin = True
while camera.isOpened():
    _, frame = camera.read()
    if frame is None:
        break
    frame = cv2.resize(frame, (800, 600))

    # Your code
    processed = main.run(frame)

    if is_begin:
        # Right values of high and width
        h, w, _ = processed.shape
        out = cv2.VideoWriter(output_file, fourcc, 30, (w, h), True)
        print(out.isOpened()) # To check that you opened VideoWriter
        is_begin = False

    out.write(processed)
    cv2.imshow('', processed)
    choice = cv2.waitKey(1)
    if choice == 27:
        break
