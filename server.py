
import cv2
import asyncio
import websockets
from microcon_process import *


def img_decode(img_string, filename):

    img_data = base64.b64decode(img_string)
    filename = os.path.join('result/', filename)
    with open(filename, 'wb') as f:
        f.write(img_data)

    return filename


def licence_plate_detection(encoded_img):

    filename = datetime.now().strftime('%Y-%m-%d %H:%M:%S.jpg')
    img_decoded_path = img_decode(encoded_img, filename)

    img = cv2.imread(img_decoded_path)
    cv2.imshow('org_img', img)

    # use img to detect licence  plate.

    cv2.imwrite(f'detected-{filename}', img)


async def server_process(websocket, path):

    mode_num = int(await websocket.recv())

    if mode_num is 1:
        mode_name = 'take_photo'
        print(f"Your Process {mode_name!r} is processing!\n")
        encoded_img = take_photo()
        licence_plate_detection(encoded_img)

    elif mode_num is 2:
        mode_name = 'replace_photo'
        print(f"Your Process {mode_name!r} is processing!\n")
        replace_photo()

    elif mode_num is 3:
        mode_name = 'show_photo'
        print(f"Your Process {mode_name!r} is processing!\n")
        encoded_img, filename = show_photo()
        img_decoded_path = img_decode(encoded_img, filename)

        img = cv2.imread(img_decoded_path)
        cv2.imshow('org_img', img)

    elif mode_num is 4:
        mode_name = 'remove_photo'
        print(f"Your Process {mode_name!r} is processing!\n")
        del_photo()

    elif mode_num is 5:
        mode_name = 'move_camera'
        print(f"Your Process {mode_name!r} is processing!\n")
        move_camera()

    else:
        mode_name = 'Please Select Process Mode!!!\n'

    greeting = f"Your Process {mode_name!r} is processed!\n\n" if 6 > mode_num > 0 else f"{mode_name}\n\n"

    await websocket.send(greeting)
    print(f"{greeting}")

start_server = websockets.serve(server_process, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
