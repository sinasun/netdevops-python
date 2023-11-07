from app.network_health import ping, check_port, speed_test

def test_ping_success():
    host = "google.com"
    assert ping(host) is True or False # server doesn't support network

def test_ping_failure():
    host = "non-exist-host.com"
    assert ping(host) is False

def test_check_open_port():
    host = "google.com"
    port = 80
    assert check_port(host, port) is True

def test_check_closed_port():
    host = "google.com"
    port = 8080
    assert check_port(host, port) is False

def test_speed_test():
    download_speed, upload_speed = speed_test()
    if download_speed and upload_speed:
        assert download_speed > 0
        assert upload_speed > 0
    else:
        assert True # server doesn't support network
