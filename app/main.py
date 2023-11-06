from network_health import ping, check_port, speed_test

def main():
    host_to_ping = "google.com"
    port_to_check = 80

    # Perform network health checks
    ping_result = ping(host_to_ping)
    port_check_result = check_port(host_to_ping, port_to_check)
    download_speed, upload_speed = speed_test()

    print("Network Health Check Results:")
    print(f"Ping to {host_to_ping}: {'OK' if ping_result else 'Failed'}")
    print(f"Port {port_to_check} on {host_to_ping} is {'open' if port_check_result else 'closed'}")
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    main()
