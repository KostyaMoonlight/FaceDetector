from tools import *
from concurrent.futures import Future
from requests_futures.sessions import FuturesSession


class ServerTransfer:
        
    def prepare_image(self, image):
        bytes_image = image2bytes(image)
        encoded_image = bytes2base64(bytes_image)
        return encoded_image
    

    def to_json(self, image):
        return "{\"image\":\"" + image + "\"}"


    def __init__(self, destination):
        self.destination = destination
        self._future_session = FuturesSession(max_workers=5)


    def transfer(self,image):
        data = self.prepare_image(image)

        response = self._future_session.post(self.destination, headers={'Content-Type':  'application/json'}, json={
            'image': data})

        return response.result().text
    