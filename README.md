[README.md](https://github.com/user-attachments/files/32507354/README.md)

# Simple TCP Port Scanner

A small Python script that scans a target host for open TCP ports within a given range. Built as a self-directed project to better understand how port scanning tools work under the hood.

## What it does

- Resolves a hostname or IP address
- Attempts a TCP connection to every port in a user-defined range
- Reports which ports respond as open
- Times the scan and prints start time for reference

## How to run

Requires Python 3 (no external libraries — uses only the standard library).

```bash
python port_scanner.py
```

You'll be prompted for:

1. **Host** — an IP address or domain name (e.g. `127.0.0.1` or `scanme.nmap.org`)
2. **Start port** — first port in the range (e.g. `1`)
3. **End port** — last port in the range (e.g. `1024`)

## Example

```
Enter the host IP address or domain: 127.0.0.1
Enter the starting port (e.g., 1): 1
Enter the ending port (e.g., 1024): 1024
--------------------------------------------------
Scanning target: 127.0.0.1
Time started: 2026-09-22 14:32:01.123456
--------------------------------------------------
Port 22: OPEN
Port 80: OPEN
```

## How it works

For each port in the range, the script opens a TCP socket and calls `connect_ex()`, which returns `0` if the connection succeeds. A short timeout (1 second) keeps the scan from hanging on closed or filtered ports.

## Notes / possible improvements

- Currently single-threaded, so large port ranges take a while — multithreading would speed this up
- No banner grabbing yet (identifying the service running on an open port)
- No input validation on the port range

##  Ethical use

This tool is for educational purposes only. Only scan hosts and networks you own or have explicit permission to test (e.g. `localhost`, your own home network, or a legal test target like `scanme.nmap.org`). Scanning systems without authorization may be illegal in your jurisdiction.
