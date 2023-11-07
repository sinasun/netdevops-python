from app.network_health import ping, check_port, speed_test, NetworkNotConnectedException

def test_ping_success():
    host = "google.com"
    try:
        assert ping(host) is True
    except NetworkNotConnectedException:
        pass  # pass the test if the network is not connected

def test_ping_failure():
    host = "non-exist-host.com"
    try:
        assert ping(host) is False
    except NetworkNotConnectedException:
        pass  # pass the test if the network is not connected

def test_check_open_port():
    host = "google.com"
    port = 80
    try:
        assert check_port(host, port) is True
    except NetworkNotConnectedException:
        pass  # pass the test if the network is not connected

def test_check_closed_port():
    host = "google.com"
    port = 8080
    try:
        assert check_port(host, port) is False
    except NetworkNotConnectedException:
        pass  # pass the test if the network is not connected

def test_speed_test():
    try:
        download_speed, upload_speed = speed_test()
        assert download_speed > 0
        assert upload_speed > 0
    except NetworkNotConnectedException:
        pass  # pass the test if the network is not connected
