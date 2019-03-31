#!/usr/bin/python3

import sys
import pigpio
from dy01 import DY01

def main():
    if len(sys.argv) < 3:
        print("Error: insufficient number of arguments", file=sys.stderr)
        print("Usage: dy01 ADDRESS on|off", file=sys.stderr)
        sys.exit(1)

    address = int(sys.argv[1])

    if address < 0 or address > 1023:
        print("Invalid address. Valid addresses are 0-1023 (inclusive)", file=sys.stderr)
        sys.exit(1)

    if sys.argv[2] == "on":
        action = 1
    elif sys.argv[2] == "off":
        action = 0
    else:
        print("Invalid action. Valid actions are \"on\" and \"off\".", file=sys.stderr)
        sys.exit(1)

    dy01 = DY01(pigpio.pi(), 17)

    dy01.send(address, action)

if __name__ == "__main__":
    main()
