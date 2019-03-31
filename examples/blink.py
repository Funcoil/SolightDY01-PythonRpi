#!/usr/bin/python

import time
import pigpio
from dy01 import DY01

def main():
    dy01 = DY01(pigpio.pi(), 17)

    socket = 1019

    while True:
        dy01.send(socket, 1);
        time.sleep(1)
        dy01.send(socket, 0);
        time.sleep(1)

if __name__ == "__main__":
    main()
