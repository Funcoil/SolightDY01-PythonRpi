Python Solight DY01 library for Raspberry Pi
============================================

This library allows you to control [Solight DY01](https://www.nay.sk/solid-dy01-dialkovo-ovladane-zasuvky-set-3-1) sockets from Raspberry Pi.

How to use it
-------------

Connect cheap [433 MHz transmitter](https://www.robotshop.com/en/seeedstudio-433mhz-low-cost-transmitter-receiver-pair.html) to any GPIO pin (e.g. 17)

```
sudo apt-get install pigpio-python
sudo pigpiod
```

```python
import time
import pigpio
from dy01 import DY01

pi = pigpio.pi()
dy01 = DY01(pi, 17)

while True:
	dy01.send(42, 1)
	time.sleep(1)
	dy01.send(42, 0)
	time.sleep(1)
```

...

Profit! :D

License
-------

MITNFA
