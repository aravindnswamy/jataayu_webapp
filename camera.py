import cv2

import putTextToVideo as ptv
import callbacks as cb

class VideoCamera(object):

    width = 480
    height = 640

    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video_cap = cv2.VideoCapture(1)

        # Creation of Video Capture Codec
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')

        # Creation of Video Capture Object
        self.video_rec = cv2.VideoWriter('op.avi',fourcc, 20.0, (640,480))

        self.video_cap.set(3, VideoCamera.width)
        self.video_cap.set(4, VideoCamera.height)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video_cap.release()

    def get_frame(self):

        # Frame-by-frame capture
        ret,frame = self.video_cap.read()

        #Flip the inverted frame
        #frame = cv2.flip(frame,1)

        #Write to the file using VideoWriter Object
        #self.video_rec.write(frame)

        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        fail_text = 'Error! Cannot recieve the Video! Please check the correctness of Camera!'
        succ_text = 'Success! Receiving the Video Feed.'

        if not ret:

            cv2.putText(frame, fail_text, (0, 50), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
            #cv2.imshow('Video Window',frame)
            exit(0)

        self.f_width = self.video_cap.get(3)
        self.f_height = self.video_cap.get(4)

        ptv.putTextToVideo(frame, succ_text,0,50,font,1,255, 255, 255, 1, cv2.LINE_AA)
        ptv.putTextToVideo(frame,'Frame Width:' + str(self.f_width),10,470,font,1,255,255,255,1,cv2.LINE_AA)
        ptv.putTextToVideo(frame, 'Frame Height:' + str(self.f_height), 350, 470, font, 1, 255, 255, 255, 1, cv2.LINE_AA)

        #videoWindow = cv2.namedWindow('Video Window',cv2.WINDOW_NORMAL)
        #cv2.setWindowProperty(videoWindow,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_KEEPRATIO)
        #cv2.imshow('Video Window',frame)
        key = cv2.waitKey(1)
        if ((key & 0xFF == ord('q')) or (key == 27)):
            exit(0)

        cv2.setMouseCallback('Video Window',cb.mouseCallback)
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()


    def saveget_frame(self):

        # Frame-by-frame capture
        ret,frame = self.video_cap.read()

        #Flip the inverted frame
        #frame = cv2.flip(frame,1)

        #Write to the file using VideoWriter Object
        self.video_rec.write(frame)

        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        fail_text = 'Error! Cannot recieve the Video! Please check the correctness of Camera!'
        succ_text = 'Success! Receiving the Video Feed.'

        if not ret:

            cv2.putText(frame, fail_text, (0, 50), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
            #cv2.imshow('Video Window',frame)
            exit(0)

        self.f_width = self.video_cap.get(3)
        self.f_height = self.video_cap.get(4)

        ptv.putTextToVideo(frame, succ_text,0,50,font,1,255, 255, 255, 1, cv2.LINE_AA)
        ptv.putTextToVideo(frame,'Frame Width:' + str(self.f_width),10,470,font,1,255,255,255,1,cv2.LINE_AA)
        ptv.putTextToVideo(frame, 'Frame Height:' + str(self.f_height), 350, 470, font, 1, 255, 255, 255, 1, cv2.LINE_AA)

        #videoWindow = cv2.namedWindow('Video Window',cv2.WINDOW_NORMAL)
        #cv2.setWindowProperty(videoWindow,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_KEEPRATIO)
        #cv2.imshow('Video Window',frame)
        key = cv2.waitKey(1)
        if ((key & 0xFF == ord('q')) or (key == 27)):
            exit(0)

        cv2.setMouseCallback('Video Window',cb.mouseCallback)
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
