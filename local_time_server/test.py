#!/usr/bin/env python3

"""
This is a simple time server to broadcast local time (number of seconds passed today) via UDP.
NTP internet servers only show UTC time and I want the local time for my custom made wall clock.
An alternative is to install a local NTP server, but running this python script is much simpler
both for setup and access.
"""

import time
import socket

WEB_PORT = 60000

m = 30
s = 0
h = 0


total_seconds = h * 3600 + m * 60 + s
message = "{}".format(total_seconds).encode('utf-8')

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# UDP is not guaranteed to arrive so broadcast few times
server.sendto(message, ("255.255.255.255", WEB_PORT))
time.sleep(0.1)
server.sendto(message, ("255.255.255.255", WEB_PORT))
time.sleep(0.1)
server.sendto(message, ("255.255.255.255", WEB_PORT))

print("Sent: {}".format(message), flush=True)

server.close()