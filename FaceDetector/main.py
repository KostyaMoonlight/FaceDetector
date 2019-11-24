from transfers import OpenCvTransfer,ServerTransfer
from stream_reader import StreamReader
from config import Config

if __name__=="__main__":
    cv_transfer = OpenCvTransfer()
    server_transfer = ServerTransfer(Config.adress)
    reader = StreamReader('0', server_transfer)
    reader.analize_stream()
    print('end')

