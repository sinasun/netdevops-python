from app.network_health import ping, check_port, speed_test, NetworkNotConnectedException

def test_ping_success():
    host = "google.com"
    network_connected = True
    result = False
    try:
        result = ping(host)
    except NetworkNotConnectedException:
        network_connected = False

    if network_connected is True:
        assert result is True

def test_ping_failure():
    host = "non-exist-host.com"
    network_connected = True
    result = True
    try:
        result = ping(host)
    except NetworkNotConnectedException:
        network_connected = False

    if network_connected is True:
        assert result is False

def test_check_open_port():
    host = "google.com"
    port = 80
    result = False
    network_connected = True
    try:
        result = check_port(host, port)
    except NetworkNotConnectedException:
        network_connected = False
    
    if network_connected is True:
        assert result is True

def test_check_closed_port():
    host = "google.com"
    port = 8080
    network_connected = True
    result = True
    try:
        result = check_port(host, port)
    except NetworkNotConnectedException:
        network_connected = False

    if network_connected is True:
        assert result is False

def test_speed_test():
    download_speed = 0
    upload_speed = 0
    network_connected = True;
    try:
        download_speed, upload_speed = speed_test()
    except NetworkNotConnectedException:
        network_connected = False

    if network_connected is True:
        assert download_speed > 0
        assert upload_speed > 0
