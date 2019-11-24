import cv2
from PIL import Image
from io import BytesIO
import base64
import numpy as np


def bytes2image(bytes):
    return Image.open(BytesIO(bytes))  



def base64_to_bytes(base64_face_image): 
    base64_face_image = base64_face_image.encode("utf-8")
    return base64.b64decode(base64_face_image)

def restore_image(image):
    return np.array(bytes2image(base64_to_bytes(image)))