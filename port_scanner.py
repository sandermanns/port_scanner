import socket
import sys
from datetime import datetime

# Define target (can be a hostname or IP address)
target_host = input("Enter the host IP address or domain: ")

try:
    target_ip = socket.gethostbyname(target_host)
except socket.gaierror:
    print("\n Hostname could not be resolved.")
    sys.exit()

start_port = int(input("Enter the starting port (e.g., 1): "))
end_port = int(input("Enter the ending port (e.g., 1024): "))

print("-" * 50)
print(f"Scanning target: {target_ip}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

try:
    for port in range(start_port, end_port + 1):
        # AF_INET specifies IPv4, SOCK_STREAM specifies TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a short timeout so the script doesn't hang on closed ports
        sock.settimeout(1.0)

        # connect_ex returns 0 if the connection was successful
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port}: OPEN")

        sock.close()

except KeyboardInterrupt:
    print("\nExiting script.")
    sys.exit()

except socket.error:
    print("\nCould not connect to server.")
    sys.exit()
