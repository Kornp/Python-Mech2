#640 x 480 = 307200

# 640/2 & 480/2 = 240 x 320

#PLEASE CHANGE IMAGE_NAME TO ACTUAL IMAGE NAME
import cv2
import numpy as np
import serial
import time
import serial.tools.list_ports
import Serial2

cap = cv2.VideoCapture(0)

serial_baud_rate = 115200
serial_port = "/dev/ttyUSB0"
serial_byte_size = 8
serial_stop_bits = 1
serial_time_out = 2
serial_xxonxoff = False
serial_rtscts = True
serial_write_timeout = 2
serial_dstdtr = False
serial_intercharttimeout = None
serial_usingSerial = True

seri = Serial2.Serial2(port=serial_port,
                           baud=serial_baud_rate,
                           bytesize=serial_byte_size,
                           parity=serial.PARITY_NONE,
                           stopbits=serial_stop_bits,
                           timeout=serial_time_out,
                           xonxoff=serial_xxonxoff,
                           rtscts=serial_rtscts,
                           writetimeout=serial_write_timeout,
                           dstdtr=serial_dstdtr,
                           intercharttimeout=serial_intercharttimeout,
                           usingSerial=serial_usingSerial)


while(True):
    ret, frame = cap.read()
    frame[int (frame.shape[0] / 2), int (frame.shape[1] / 2)]=[255,0,255]
    center = frame[int (frame.shape[0] / 2), int (frame.shape[1] / 2)]
    #frame.center = [255,0,255]
    #center = 240, 320
    frame[210, 400] = [255,0,255]
    test = frame[210, 400]

    test = [0, 640]

    North = '0'
    East = '1'
    South = '2'
    West = '3'
    Unknown = '4'

    if test[0] < 240 and test[0] >= 0:
       if test[1] < 320 and test[1] >= 0:
           print ('Target South East\n')
           message = ("{\"South East\"  : \"" + South + "\"}")
       elif test[1] <= 640 and test[1] > 320:
           print ('Target South West\n')
           message = ("{\"South West\"  : \"" + South + "\"}")
       elif test[1] == 320:
           print ('Target South\n')
           message = ("{\"South\"  : \"" + South + "\"}")
       else:
           print ("Error on 1st")

    elif test[0] < 480 and test[0] > 240:
        if test[1] < 320 and test[1] >= 0:
            print ('Target North East\n')
            message = ("{\"North East\"  : \"" + North + "\"}")
        elif test[1] <= 640 and test[1] > 320:
            print ('Target North West\n')
            message = ("{\"North West\"  : \"" + North + "\"}")
        elif test[1] == 320:
            print ('Target North\n')
            message = ("{\"North\"  : \"" + North + "\"}")
        else:
            print ("Error on 2nd")

    elif test[0] == 240:
        if test[1] < 320 and test[1] >= 0:
            print ('Target East\n')
            message = ("{\"East\"  : \"" + East + "\"}")
        elif test[1] <= 640 and test[1] > 320:
            print ('Target West\n')
            message = ("{\"West\"  : \"" + West + "\"}")
        elif test[1] == 320:
            print ('Target Reached\n')
        else:
            print ('Error on 3rd')

    else:
        print ('Unknown Location\n')
        message = ("{\"None\"  : \"" + Unknown + "\"}")
    seri.sendMessage(message=message, length=len(message))

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
