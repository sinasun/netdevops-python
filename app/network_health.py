import socket
import speedtest
import os
from urllib import request

class NetworkNotConnectedException(Exception):
    pass

def internet_connected():
    try:
        request.urlopen('http://8.8.8.8', timeout=1)
        return True
    except Exception: 
        return False

def ping(host):
    if internet_connected is True: 
        print("ping running")
        response = os.system(f"ping -c 1 {host}")
        if response == 0:
            return True  # Network is connected and ping is working
        else:
            return False # Network is connected but ping is not working
    raise NetworkNotConnectedException("No network connectivity")

def check_port(host, port):
    if internet_connected is True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((host, port))
            return True
        except (socket.timeout, ConnectionRefusedError):
            return False
    raise NetworkNotConnectedException("No network connectivity")

def speed_test():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000 # Convert to Mbps
        upload_speed = st.upload() / 1_000_000 # Convert to Mbps
    except (speedtest.ConfigRetrievalError, speedtest.NoMatchedServers):
        # No network connection 
        raise NetworkNotConnectedException("No network connectivity")

    return download_speed, upload_speed
