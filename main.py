import socket
from pythonping import ping
import time
import concurrent.futures
import typer
import getpass 

#versioning
version = 0.1

#Change these as you like
_scan_class_b = False
_timeout = 0.25
_packet_loss_threshold = 1
_count = 3
_num_threads = 100


########## DO NOT CHANGE ANYTHING BELOW THIS LINE ##########
start_time = time.time()

#Colouring
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)



def main():
    

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    


    ip = s.getsockname()[0]
    hostname = s.getsockname()
  
    print("Own IP: " + ip + "\n")

    #add hosts to hosts list
    #take your own ip and add it to the list

    split = ip.split('.')
    
    print(_scan_class_b)
    if _scan_class_b is False:
        for j in range(1, 255):
            new_ip = split[0] + '.' + split[1] + '.' + split[2] + '.' + str(j)
            hosts.append(new_ip)
    else:
        for i in range(1, 256):
            for j in range(1, 255):
                new_ip = split[0] + '.' + split[1] + '.' + str(i) + '.' + str(j)
                hosts.append(new_ip)

    # print(hosts)
    ping_hosts_in_parallel(hosts, _timeout, _packet_loss_threshold, _count)
    
    resolved_hosts()

    #close the socket
    s.close()






def ping_host(host, timeout, packet_loss_threshold, count):
    try:
        #ping the host with the specified timeout and packet loss threshold
        ping_result = ping(target=host, count=count, timeout=timeout)

       

        #print all attributes of the ping result
        print("Pinging: " + host + "\n")
        print(ping_result.__dict__)
        

        #add host to responders list if packet loss is below the specified threshold
        if ping_result.packet_loss < packet_loss_threshold:
            print(colored(0, 255, 0, "Host is up: " + host + "\n"))
            responders.append(host)
        else:
          print(colored(255, 0, 0, "Host is down: " + host + "\n"))
    except Exception as e:
            print(colored(255, 0, 0, "Error: " + str(e) + "\n"))

    

def ping_hosts_in_parallel(hosts, timeout, packet_loss_threshold, count):
      with concurrent.futures.ThreadPoolExecutor(max_workers=_num_threads) as executor:
        # Start the ping processes (in this case, using a thread pool)
        results = [executor.submit(ping_host, host, timeout, packet_loss_threshold, count) for host in hosts]

        for future in concurrent.futures.as_completed(results):
            # Wait for the ping process to complete and get the result
            result = future.result()

def resolved_hosts():
    print("Responders: " + str(responders) + "\n")

    #Resolve hostnames
    for host in responders:
        try:
            hostname = socket.gethostbyaddr(host)
            print(colored(0, 255, 0, "Resolving hostname: " + str(hostname) + "\n"))
        except Exception as e:
            print(colored(255, 0, 0, "Error: " + str(e) + "\n"))
    
    #print the time it took to scan the network
    print("Time elapsed: " + str(time.time() - start_time) + " seconds\n")



hosts = [
    '127.0.0.1'
]
responders = []


def print_settings():
    print("\nSettings: \n")
    print("Scan Class B: " + str(_scan_class_b))
    print("Timeout: " + str(_timeout))
    print("Packet loss threshold: " + str(_packet_loss_threshold))
    print("Count: " + str(_count))
    print("Number of threads: " + str(_num_threads) + "\n")

    #wait for user input
    input("Press enter to start or ctrl+c to exit...")

def check_sudo():
    #check if user is root
    try:
        if getpass.getuser() != "root":
            print("Please run as root...")
            exit()
        else:
            print("Running as root")
    except Exception as e:
        print("Error: " + str(e))
        print("Please run as root... Root detection only works on unix systems")
        input("Press enter to continue anyway or ctrl+c to exit...")

    
    


###CLI###
app = typer.Typer()

#test command 
@app.command()
def typer_main(classb: bool = typer.Option("False", help="Scan Class B network"), timeout: float = typer.Option(0.25, help="Timeout for ping"), packet_loss_threshold: int = typer.Option(1, help="Packet loss threshold"), count: int = typer.Option(3, help="Number of packets to send"), num_threads: int = typer.Option(100, help="Number of threads to use")):
    global _scan_class_b
    global _timeout
    global _packet_loss_threshold
    global _count
    global _num_threads

    
    _scan_class_b = classb
    _timeout = timeout
    _packet_loss_threshold = packet_loss_threshold
    _count = count
    _num_threads = num_threads

    check_sudo()
    print_settings()
    main()



if __name__ == '__main__':
    #main()
    app()




