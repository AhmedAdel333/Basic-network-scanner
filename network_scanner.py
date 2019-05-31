import subprocess as sp
import socket
from socket import AF_INET, SOCK_STREAM

def ip_check(host):
    stat, res = sp.getstatusoutput("ping -c1 -w2 " + str(host))
    if stat == 0:
        print("host " + str(host) + " is alive")
    else:
        print("host " + str(host) + " is down")

def port_scan(host):
	port_list = range(134, 140)
	for port in port_list:
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		conn.settimeout(2)
		try:
			conn.connect((host, port))
			while True:
				print ("[+] port ", port, "is open")
				break;
		except socket.error:
			print ("[-] port ", port, "is closed")


start_range = 1
end_range = 255
for ip in range(start_range, end_range):
    host = "192.168.1." + str(ip)
    ip_check(host)
    port_scan(host)




