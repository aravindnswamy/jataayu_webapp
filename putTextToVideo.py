import cv2

def putTextToVideo(frame,text,x_coordinate,y_coordinate,fontName,fontScale,b_component,g_component,r_component,thickness,lineType):
    cv2.putText(frame, text, (x_coordinate,y_coordinate), fontName, fontScale, (b_component, g_component,r_component),thickness, lineType)
