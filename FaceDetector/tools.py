import cv2
from PIL import Image
from io import BytesIO
import base64

def is_number(s):
    return s.isdigit()


def str_to_int(s):
    return int(s)

def image2bytes(image):  
    image = Image.fromarray(image.astype('uint8'), "RGB")   
    with BytesIO() as output:
        image.save(output, format="JPEG")
        return output.getvalue()


def image2base64(image): 
        base64_face_image = base64.b64encode(image.tobytes())
        return base64_face_image.decode("utf-8")

def bytes2base64(bytes): 
        base64_face_image = base64.b64encode(bytes)
        return base64_face_image.decode("utf-8")