#!/usr/bin/python

''' Cardinal - An Open Source Cisco Wireless Access Point Controller

MIT License

Copyright © 2017 falcon78921

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

import paramiko
import time
import sys

queryIP = sys.argv[1]
queryUser = sys.argv[2]
queryPass = sys.argv[3]
querySSID = sys.argv[4]
queryVlan = sys.argv[5]
queryRadioSub = sys.argv[6]
queryGigaSub = sys.argv[7]

ip = queryIP
username = queryUser
password = queryPass
ssid = querySSID
vlan = queryVlan
radiosub = queryRadioSub
gigasub = queryGigaSub

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, port=22, username=username,
                        password=password,
                        look_for_keys=False, allow_agent=False)

remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(65535)


remote_conn.send("enable\n")
time.sleep(.10)
output = remote_conn.recv(65535)


remote_conn.send('%s\n' % password)
time.sleep(.15)
output = remote_conn.recv(65535)


remote_conn.send("conf t\n")
time.sleep(.10)
output = remote_conn.recv(65535)


remote_conn.send('no dot11 ssid %s\n' % ssid)
time.sleep(.10)
output = remote_conn.recv(65535)


remote_conn.send('no int d0.%s\n' % radiosub)
time.sleep(.10)
output = remote_conn.recv(65535)


remote_conn.send('no int gi0.%s\n' % gigasub)
time.sleep(.10)
output = remote_conn.recv(65535)


remote_conn.send("int d0\n")
time.sleep(.10)
output = remote_conn.recv(65535)


remote_conn.send('no encryption vlan %s mode ciphers aes-ccm\n' % vlan)
time.sleep(.10)
output = remote_conn.recv(65535)


remote_conn.send("do wr\n")
time.sleep(.10)
output = remote_conn.recv(65535)


exit()

