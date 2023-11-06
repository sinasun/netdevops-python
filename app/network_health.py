import socket
import subprocess
import speedtest

def ping(host, count=4):
    try:
        subprocess.check_output(["ping", "-c", str(count), host])
        return True
    except subprocess.CalledProcessError:
        return False

def check_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((host, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False

def speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000
    return download_speed, upload_speed
