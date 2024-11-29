# OpenPort - A Simple Open Port Scanner

OpenPort is a lightweight and easy-to-use port scanner written in Python. It scans the specified target IP address for open ports and displays the results. The tool supports scanning a range of ports and is designed to help you discover potential open services on a remote machine.

## Features

- Scan a specified range of ports (default is 1 to 1024).
- Display open ports on the target IP.
- Simple command-line interface with clear output.
- The logo and credits are displayed on startup.
- Developed by [mrsajadpp](https://github.com/mrsajadpp).

## Installation

### Requirements

- Python 3.x
- `socket` and `argparse` libraries (these are included in the standard Python library).

### Steps to Run

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/mrsajadpp/openport.git
   cd openport
   ```

2. Run the script using Python:
   ```bash
   python openport.py <TARGET_IP> --start-port <START_PORT> --end-port <END_PORT>
   ```

   Example:
   ```bash
   python openport.py 192.168.1.1 --start-port 1 --end-port 1024
   ```

   This will scan the IP `192.168.1.1` for open ports in the range from 1 to 1024.

## Usage

### Command-line Arguments

- `TARGET_IP` (required): The target IP address you want to scan.
- `--start-port`: The starting port for the scan (default is 1).
- `--end-port`: The ending port for the scan (default is 1024).

Example:

```bash
python openport.py 192.168.1.1 --start-port 100 --end-port 200
```

This will scan ports 100 to 200 on the IP address `192.168.1.1`.

## Logo

Upon running the script, you will see the following logo printed in yellow:

```
░█▀█░█▀█░█▀▀░█▀█░█▀█░█▀█░█▀▄░▀█▀
░█░█░█▀▀░█▀▀░█░█░█▀▀░█░█░█▀▄░░█░
░▀▀▀░▀░░░▀▀▀░▀░▀░▀░░░▀▀▀░▀░▀░░▀░
```

## Credit

This tool was developed by [mrsajadpp](https://github.com/mrsajadpp).

GitHub Repository: [https://github.com/mrsajadpp/openport.git](https://github.com/mrsajadpp/openport.git)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.