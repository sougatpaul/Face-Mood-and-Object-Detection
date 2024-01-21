import cv2
import f_Face_info
import time

def rtfec():
    face_cascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
    
    video_capture = cv2.VideoCapture(1)
    
    while True:
        # Capture frame-by-frame
        star_time = time.time()
        ret, frame = video_capture.read()
    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            out = f_Face_info.get_face_info(frame)
            
     
            out = f_Face_info.get_face_info(frame)
            # pintar imagen
            res_img = f_Face_info.bounding_box(out,frame)
            
            end_time = time.time() - star_time    
            FPS = 1/end_time
            cv2.putText(res_img,f"FPS: {round(FPS,3)}",(10,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        # Display the resulting frame
        cv2.imshow('Video', frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
	rtfec()