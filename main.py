import socket
from pythonping import ping
import time


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    


    ip = s.getsockname()[0]
    hostname = s.getsockname()

    s.close()
    print("Own IP: " + ip + "\n")

    #add hosts to hosts list
    #take your own ip and add it to the list

    split = ip.split('.')
    
    for i in range(1, 256):
        for j in range(1, 256):
            new_ip = split[0] + '.' + split[1] + '.' + str(i) + '.' + str(j)
            hosts.append(new_ip)

    # print(hosts)
    for host in hosts:
        ping_host(host)






def ping_host(host):
    ping_result = ping(target=host, count=10, timeout=1)
    print("Pinging: " + host + "\n")
    print(ping_result)
   

    if ping_result.packet_loss == 0:
        print("Host is up: " + host + "\n")
        #add host to responders list
        responders.append(host)
    else:
        print("Host is down: " + host + "\n")

hosts = [
    '127.0.0.1'
]

responders = []

# for host in hosts:
#     print(ping_host(host))


if __name__ == '__main__':
    main()

