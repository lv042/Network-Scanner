
# Network Scanner
This script is a simple network scanner that pings all the hosts within a specified range of IP addresses to check if they are up or down. It utilizes the pythonping library to send ping requests to the hosts and the socket library to retrieve the local machine's IP address.

## Requirements
- Python 3
- pythonping library

## Usage
1. Clone the repository: git clone https://github.com/[USERNAME]/network-scanner.git
2. Install the required library: pip install pythonping
3. Run the script: python main.py

The script will start by printing out the local machine's IP address and then proceed to ping all the hosts within the specified range. It will print out the ping results for each host and classify them as either up or down. The list of responding hosts will be stored in the responders list.

You can modify the list of hosts to be pinged by adding or removing entries from the hosts list at the beginning of the script. The default list contains only the localhost.
The scanner will add all class B and class C addresses.

## Contributions
If you find any bugs or have suggestions for improvements, feel free to open an issue or a pull request.
