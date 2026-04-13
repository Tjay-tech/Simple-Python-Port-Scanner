# Simple-Python-Port-Scanner
A lightweight Python tool for scanning TCP ports on a target host.

**Python Port Scanner**

A lightweight, fast TCP port scanner built with Python.
It is designed for learning networking fundamentals, socket programming, and basic concurrency using threading.

**Features**
Current Features:
TCP port scanning using Python sockets
Custom port range input
Detection of open ports
Threaded scanning for improved speed
Adjustable timeout for faster or more accurate scans

🚀 **Planned Features (Roadmap)**
Service detection (banner grabbing for SSH, HTTP, FTP, etc.)
Export scan results to .txt and .csv
Open port sensitivity rating 
GUI version (Tkinter or PyQt)
Async scanning (further performance improvements)
Host discovery (check if target is online before scanning)
Better scan modes (quick / normal / deep scan)
JSON output for automation use

⚙️ **Requirements**
Python 3.x
No external libraries required (uses built-in modules only).

**How to Use**
Run the script:
python scanner.py

Then input:
enter ip: 127.0.0.1
enter start port no: 1
enter end port number: 1000

Example Output
[+] port 22 is open on 127.0.0.1
[+] port 80 is open on 127.0.0.1
[+] port 9999 is open on 127.0.0.1

🧠 **How It Works**
This tool uses Python’s socket module to attempt TCP connections to a target IP and port range.

If the connection succeeds → port is OPEN
If it fails → port is CLOSED or FILTERED

Threading is used to scan multiple ports simultaneously, significantly improving scan speed compared to sequential scanning.

⚠️**Disclaimer**
This tool is intended for educational purposes only.
Do not use it to scan systems, networks, or devices you do not own or do not have explicit permission to test. Unauthorized scanning may be illegal.

Future Improvements
This project will evolve into a mini network reconnaissance tool inspired by tools like Nmap, with additional features such as service detection, asynchronous scanning, and reporting capabilities.
