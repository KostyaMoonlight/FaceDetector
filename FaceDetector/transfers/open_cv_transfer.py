import cv2

class OpenCvTransfer:
    def transfer(self, image):
        cv2.imshow("Face Detection", image)
        cv2.waitKey(delay=1)

    