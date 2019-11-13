
import os
import base64
import time
import smbus
from time import sleep
from datetime import datetime
from picamera import PiCamera


bus = smbus.SMBus(1)
address = 0x04
camera = PiCamera()


def img_encode(img_path):
    with open(img_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

        return encoded_string


def take_photo():

    if not os.path.exists('result'):
        os.makedirs('result')

    filename = datetime.now().strftime('%Y-%m-%d %H:%M:%S.jpg')
    camera.start_preview(alpha=190)
    sleep(1)
    camera.capture(f"result/{filename}")
    camera.stop_preview()

    encoded_img = img_encode(f"result/{filename}").decode('utf-8')

    return encoded_img


def replace_photo():

    if not os.path.exists('result'):
        print('No Photo in Result Directory!!!')

    filename = [file_list for file_list in os.listdir('result') if file_list.endswith('.jpg')][-1]
    camera.start_preview(alpha=190)
    sleep(1)
    camera.capture(f"result/{filename}")
    camera.stop_preview()


def show_photo():

    if not os.path.exists('result'):
        print('No Photo in Result Directory!!!')

    filename = [file_list for file_list in os.listdir('result') if file_list.endswith('.jpg')][-1]
    encoded_img = img_encode(f"result/{filename}").decode('utf-8')

    return encoded_img, filename


def del_photo():

    if not os.path.exists('result'):
        print('No Photo in Result Directory!!!')

    filename = [file_list for file_list in os.listdir('result') if file_list.endswith('.jpg')][-1]
    os.remove(os.path.join('result', filename))


def write_number(value):

    bus.write_byte(address, value)
    return -1


def move_camera():

    write_number(ord('1'))
    time.sleep(.1)

