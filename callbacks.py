import cv2

def mouseCallback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        exit(0)