import pytest
from ftp_connection import connect_ftp, close_ftp


@pytest.fixture
def ftp_connection():
    print("Connecting to FTP server")

    ftp = connect_ftp()

    yield ftp

    print("Closing FTP connection")
    close_ftp(ftp)


def test_ftp_connection(ftp_connection):
    assert ftp_connection.sock is not None
    