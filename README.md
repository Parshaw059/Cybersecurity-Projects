# Password Strength Checker

A Python-based tool to evaluate password strength using different security checks.

## Project Versions

### Version 1
Basic password strength checker based mainly on password length.

File:
```
password_checker_v1.py
```

### Version 2
Enhanced password strength checker that validates:

- Minimum password length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

File:
```
password_checker_v2.py
```

## Features

- Password validation
- Security-focused checks
- Beginner-friendly Python implementation

## How to Run

Version 1:

```bash
python password_checker_v1.py
```

Version 2:

```bash
python password_checker_v2.py
```

## Future Improvements

- Password strength score (0–100)
- GUI using Tkinter
- Common password detection
- Password suggestions

# TCP Port Scanner

A Python-based TCP Port Scanner that scans a target IP address and identifies open and closed ports within a specified range.

## Features

* Scan a custom IP address
* Scan a user-defined port range
* Detect open ports
* Detect closed ports
* Uses TCP socket connections
* Configurable timeout for faster scanning

## Technologies Used

* Python 3
* Socket Programming

## How It Works

The scanner attempts to establish a TCP connection with each port in the specified range.

* If the connection succeeds, the port is marked as **Open**.
* If the connection fails or times out, the port is marked as **Closed**.

## Example

Input:

IP Address: scanme.nmap.org
Start Port: 20
End Port: 25

Output:

Port 20 is closed
Port 21 is closed
Port 22 is open
Port 23 is closed
Port 24 is closed
Port 25 is closed

## Concepts Learned

* IP Addressing
* TCP Protocol
* Socket Programming
* Port Scanning
* Network Reconnaissance
* Timeout Handling

## Future Improvements

* Service Detection (HTTP, SSH, HTTPS, etc.)
* Multi-threaded Scanning
* Export Results to File
* GUI Interface
* Scan Statistics Dashboard

## Author

Parshaw Shah
Cybersecurity Student || Python Developer (Basics)
