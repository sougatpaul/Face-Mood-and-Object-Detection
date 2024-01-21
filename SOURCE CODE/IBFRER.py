import cv2
import f_Face_inform

def imgdis(frame):
    scale_percent = 60 # percent of original size
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    
    dim = (width, height)
    # resize image
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    # obtenego info del frame
    out = f_Face_inform.get_face_info(frame)
    # pintar imagen
    res_img = f_Face_inform.bounding_box(out,frame)
    cv2.imshow('Face info',res_img)
    cv2.waitKey(0)

     