from app.network_health import ping, check_port, speed_test, NetworkNotConnectedException
import pytest

def test_ping_success():
    host = "google.com"
    network_connected = False 
    result = False
    try:
        result = ping(host)
        network_connected = True
    except NetworkNotConnectedException:
        network_connected = False
    if network_connected is True:
        assert result is True

def test_ping_failure():
    host = "non-exist-host.com"
    with pytest.raises(NetworkNotConnectedException):
        ping(host)

def test_check_open_port():
    host = "google.com"
    port = 80
    try:
        result = check_port(host, port)
        assert result is True
    except NetworkNotConnectedException:
        pass

def test_check_closed_port():
    host = "google.com"
    port = 8080
    with pytest.raises(NetworkNotConnectedException):
        check_port(host, port)

def test_speed_test():
    try:
        download_speed, upload_speed = speed_test()
        assert download_speed > 0
        assert upload_speed > 0
    except NetworkNotConnectedException:
        pass
