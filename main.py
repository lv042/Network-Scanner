import socket
from pythonping import ping
import time
import concurrent.futures

ScanClassB = False
timeout = 0.25
packet_loss_threshold = 1
count = 3
num_threads = 100


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    


    ip = s.getsockname()[0]
    hostname = s.getsockname()

    
    socket.getaddrinfo('192.168.178.4', 80)
    #s.close()
    print("Own IP: " + ip + "\n")

    #add hosts to hosts list
    #take your own ip and add it to the list

    split = ip.split('.')
    
    if not ScanClassB:
        for j in range(1, 255):
            new_ip = split[0] + '.' + split[1] + '.' + split[2] + '.' + str(j)
            hosts.append(new_ip)
    else:
        for i in range(1, 256):
            for j in range(1, 255):
                new_ip = split[0] + '.' + split[1] + '.' + str(i) + '.' + str(j)
                hosts.append(new_ip)

    # print(hosts)
    ping_hosts_in_parallel(hosts, timeout, packet_loss_threshold, count)
    print("Responders: " + str(responders) + "\n")






def ping_host(host, timeout, packet_loss_threshold, count):
    try:
        #ping the host with the specified timeout and packet loss threshold
        ping_result = ping(target=host, count=count, timeout=timeout)
        print("Pinging: " + host + "\n")
        #print all attributes of the ping result
        print(ping_result.__dict__)

        #add host to responders list if packet loss is below the specified threshold
        if ping_result.packet_loss < packet_loss_threshold:
            print("Host is up: " + host + "\n")
            responders.append(host)
        else:
            print("Host is down: " + host + "\n")
    except Exception as e:
        print("Error: " + str(e) + "\n")


    

def ping_hosts_in_parallel(hosts, timeout, packet_loss_threshold, count):
      with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Start the ping processes (in this case, using a thread pool)
        results = [executor.submit(ping_host, host, timeout, packet_loss_threshold, count) for host in hosts]

        for future in concurrent.futures.as_completed(results):
            result = future.result()

hosts = [
    '127.0.0.1'
]

responders = []

if __name__ == '__main__':
    main()

