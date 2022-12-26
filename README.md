# Network Scanner
This script is a tool that allows you to scan a network and identify which hosts are online. It uses the pythonping library to ping hosts and the concurrent.futures module to run the pings in parallel, using a thread pool with a configurable number of threads.

## Dependencies
In order to run this script, you will need to install the following dependencies:

pythonping: a library that provides a simple way to send ICMP echo request packets and process the responses in Python. You can install it using pip install pythonping.

concurrent.futures: a module that provides a high-level interface for asynchronously executing callables, using threads or processes. This module is part of the Python Standard Library, so you don't need to install anything.

## Configuration
You can configure the following parameters at the beginning of the script:

ScanClassB: a boolean that indicates whether to scan the whole Class B network (True) or just the current subnet (False). By default, it is set to False.

timeout: a float that specifies the maximum time, in seconds, that the script should wait for a response from each host. If the host doesn't respond within this time, it will be considered as unreachable. The default value is 0.25.

packet_loss_threshold: an integer that specifies the maximum packet loss that a host can have and still be considered as reachable. The default value is 1.

count: an integer that specifies the number of ICMP echo request packets that should be sent to each host. The default value is 3.

num_threads: an integer that specifies the maximum number of threads that the script should use to run the pings in parallel. The default value is 100.

## Usage
1. Clone the repository: git clone https://github.com/lv042/network-scanner.git
2. Install the required library: pip install pythonping
3. Run the script: python main.py

The script will start by printing out the local machine's IP address and then proceed to ping all the hosts within the specified range. It will print out the ping results for each host and classify them as either up or down. The list of responding hosts will be stored in the responders list.

You can modify the list of hosts to be pinged by adding or removing entries from the hosts list at the beginning of the script. The default list contains only the localhost.
The scanner will add all class B and class C addresses.

## Contributions
If you find any bugs or have suggestions for improvements, feel free to open an issue or a pull request.
