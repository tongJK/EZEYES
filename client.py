import asyncio
import websockets

description = """

-----------------------------------------------------------
-----------------------------------------------------------

    >>> Process Mode Number Description <<<

    1 : take_photo      : take a new photo
    2 ; replace_photo   : re take a photo
    3 : show_photo      : Show current photo
    4 : remove_photo    : Remove current photo
    5 : move_camera     : Move camera 90 degree

-----------------------------------------------------------

"""
print(description)


async def client_process():

    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as websocket:
        name = input("Please Select Process Mode : ")

        if name is '0':
            print(description)

        await websocket.send(name)

        greeting = await websocket.recv()
        print(f"{greeting}")


while True:
    asyncio.get_event_loop().run_until_complete(client_process())

