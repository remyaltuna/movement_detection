import cv2
import time
import os

file1 = open("results.txt", "a")  # append mode
file1.write("Results \n")

video_folder = os.path.join(os.getcwd(), "Segmented_Video")
subject_dirs = os.listdir(video_folder)
for subject_dir in subject_dirs:
    subject_dir_path = os.path.join(video_folder, subject_dir)
    if os.path.isdir(subject_dir_path):
        for vid in os.listdir(subject_dir_path):
            if 'clip' in vid.lower() and vid.endswith('mp4'):
                full_path = os.path.join(subject_dir_path, vid)

                starttime = time.time()
                totaltime = 0.0

                start = time.time()
                end = time.time()
                temp = time.time()
                magnitude = 0.0

                capture = cv2.VideoCapture(full_path)
                #capture = cv2.VideoCapture('Practice_vid_5.mp4')
                frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))

                frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

                fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

                out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1280, 720))

                ret, frame1 = capture.read()
                ret, frame2 = capture.read()
                print(frame1.shape)

                while capture.isOpened():
                    start = time.time()
                    temp = time.time()
                    diff = cv2.absdiff(frame1, frame2)
                    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
                    blur = cv2.GaussianBlur(gray, (5, 5), 0)
                    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
                    dilated = cv2.dilate(thresh, None, iterations=3)
                    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                    for contour in contours:
                        (x, y, w, h) = cv2.boundingRect(contour)
                        test = time.time()
                        if cv2.contourArea(contour) < 100:  #this number represents the threshold for movement
                            continue                        #less means it is more sensitive
                        if (temp - end) >= 1:
                            print("Movement Started at " + str(time.time() - starttime))
                        end = time.time()
                        magnitude += (x*y)/10000 #arbitrary number just to compare magnitude between videos
                        totaltime += ((end - start) * 125)
                        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)


                    cv2.putText(frame1, "MovementTime: " + str(totaltime), (0, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 225), 3)
                    cv2.putText(frame1, "MovementMagnitude: " + str(magnitude), (0, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 225), 3)

                    image = cv2.resize(frame1, (1280,720))
                    out.write(image)
                    cv2.imshow(full_path, frame1)
                    frame1 = frame2
                    ret, frame2 = capture.read()

                    if frame2 is None:
                        break

                    if cv2.waitKey(40) == 27:
                        break

                cv2.destroyAllWindows()
                file1.write("----------------------------------------\n")
                file1.write(f"Video path: {str(full_path)}\n")
                print(f"Video path: {str(full_path)}\n")
                file1.write(f"Total Movement Time: {str(totaltime)}\n")
                print(f"Total Movement Time: {str(totaltime)}\n")
                file1.write(f"Total Magnitude of Movement: {str(magnitude)}\n")
                print(f"Total Magnitude of Movement: {str(magnitude)}\n")
                file1.write("----------------------------------------\n")
                capture.release()
                out.release()

file1.close()
