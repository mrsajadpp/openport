import socket
import argparse
import sys
import time
import threading

# ANSI escape code for yellow color
YELLOW = "\033[33m"
RESET = "\033[0m"  # Reset color to default


# Logo message that will be displayed on start
def print_logo():
    logo = """
░█▀█░█▀█░█▀▀░█▀█░█▀█░█▀█░█▀▄░▀█▀
░█░█░█▀▀░█▀▀░█░█░█▀▀░█░█░█▀▄░░█░
░▀▀▀░▀░░░▀▀▀░▀░▀░▀░░░▀▀▀░▀░▀░░▀░
    """
    text = ""
    print(YELLOW + logo + RESET)


# Credit message that will be displayed at the end
def print_credits():
    credits = """
Developed by: mrsajadpp
GitHub Repository: https://github.com/mrsajadpp/openport.git
    """
    print(credits)


def scan_ports(target_ip, start_port=1, end_port=1024):
    print(f"Scanning {target_ip} for open ports...\n")

    open_ports = []
    progress_animation = ['|', '/', '-', '\\']

    # Port scanning with animation
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        # Show scanning animation in terminal
        sys.stdout.write(f"\rScanning port {port} {progress_animation[port % 4]}")  # Updating the animation
        sys.stdout.flush()

        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

        # Adding a small delay for the animation to be visible
        time.sleep(0.1)

    sys.stdout.write("\rScan complete!                \n")  # Clear the last animation frame

    if open_ports:
        print(f"Open ports on {target_ip}: {open_ports}")
    else:
        print(f"No open ports found on {target_ip}.")


def main():
    # Print the logo when the script runs
    print_logo()
    print_credits()

    parser = argparse.ArgumentParser(description="OpenPort: A simple open port scanner")
    parser.add_argument("target_ip", help="Target IP address to scan")
    parser.add_argument(
        "--start-port", type=int, default=1, help="Start port (default: 1)"
    )
    parser.add_argument(
        "--end-port", type=int, default=1024, help="End port (default: 1024)"
    )

    args = parser.parse_args()

    # Run the port scanning in a separate thread to keep the UI responsive
    scanning_thread = threading.Thread(
        target=scan_ports, args=(args.target_ip, args.start_port, args.end_port)
    )
    scanning_thread.start()


if __name__ == "__main__":
    main()