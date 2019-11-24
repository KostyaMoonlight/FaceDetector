import cv2
from config import Config
from tools import *
from transfers import TransferStatus
import numpy as np
class StreamReader:

    def init(self):
        self.cascade = cv2.CascadeClassifier()
        self.cascade.load(Config.models[Config.model])


    def extend_rect(self,r):

        width_extra = (r[3]*Config.roi_extra - r[3]) / 2
        height_extra = (r[2]*Config.roi_extra - r[2]) / 2
        x = r[1] - width_extra if r[1] - width_extra > 0  else 0
        y = r[0] - height_extra  if r[2] - height_extra> 0 else 0

        width = r[3]*Config.roi_extra
        height = r[2]*Config.roi_extra 
        return int(x),int(y),int(width),int(height)
    

    def transfer(self,images):
    
        status = TransferStatus.NO_FACE
        for image in images:
            status = self.destination.transfer(image)
            if (status != TransferStatus.OK):
                break
            
        
        return status
    



    def detect(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        gray = cv2.equalizeHist(gray.astype(np.uint8))

        faces=self.cascade.detectMultiScale(gray)

        cropped_faces = []
        for face in faces:
            x,y,w,h = self.extend_rect(face)

            cropped_face =img[x:x+w,y:y+h]
            cropped_faces.append(cropped_face)
        return cropped_faces

    

    def __init__(self, source, destination):   
        self.source = source
        self.destination = destination
        self.init()
    



    def analize_stream(self):  
        if is_number(self.source):
             cap = cv2.VideoCapture(int(self.source)) 
        else:
             cap = cv2.VideoCapture(self.source)
        try:
            while 1:
                try:
                    _, frame = cap.read()
                    faces = self.detect(frame)
                    status = self.transfer(faces)
                    print(status)
                    if (int(status) == TransferStatus.ERROR):
                        break
                except KeyboardInterrupt:
                    break
                except Exception:
                    pass
        finally:
            cap.release()
            cv2.destroyAllWindows()


    
    # def analize_stream(self):  
    #     if is_number(self.source):
    #          cap = cv2.VideoCapture(int(self.source)) 
    #     else:
    #          cap = cv2.VideoCapture(self.source)
    #     try:
    #         while 1:
    #             _, frame = cap.read()
    #             faces = self.detect(frame)
    #             status = self.transfer(faces)
    #             try:
    #                 if (int(status) == TransferStatus.BREAK):
    #                     break
    #             except:
    #                 pass

    #     finally:
    #         cap.release()
    #         cv2.destroyAllWindows()