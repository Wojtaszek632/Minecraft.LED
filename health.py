from PIL import ImageGrab
from PIL import Image
import time
import serial

halfs = ((14, 14), (20, 14),
         (47, 14), (54, 14),
         (79, 14), (86, 14),
         (111, 14), (118, 14),
         (143, 14), (150, 14),
         (175, 14), (182, 14),
         (208, 14), (213, 14),
         (239, 14), (247, 14),
         (271, 14), (278, 14),
         (303, 14), (311, 14))


ser = serial.Serial(
    port='COM10',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)


ser.close()
ser.open()
time.sleep(3)


while True:
    # If full screen im = ImageGrab.grab(bbox=(596, 923, 920, 960))  # X1,Y1,X2,Y2
    screen_shot = ImageGrab.grab(bbox=(597, 887, 922, 923),
                                 all_screens=False, xdisplay=None)

    screen_shot.save("hearts.png")
    screen_shot_saved = Image.open("hearts.png")
    halfs_tosend = 0
    for x in halfs:
        if screen_shot_saved.getpixel(x)[0] > 100:
            halfs_tosend += 1

    ser.write((str(halfs_tosend)+"\n").encode())
    time.sleep(0.05)
