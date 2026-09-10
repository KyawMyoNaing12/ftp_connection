# from ftplib import FTP


# def connect_ftp():
    
#     ftp = FTP("127.0.0.1")
#     ftp.login("kmn", "123")
#     return ftp


# def close_ftp(ftp):
#       ftp.quit()


# ftp = connect_ftp()
# print("FTP connection successful!")
# close_ftp(ftp)
# print("FTP connection closed.")


from ftplib import FTP


def connect_ftp():
    """Connect to the FTP server."""
    ftp = FTP("127.0.0.1")
    ftp.login("kmn", "123")
    return ftp


def close_ftp(ftp):
    """Close the FTP connection."""
    ftp.quit()


if __name__ == "__main__":
    ftp = connect_ftp()

    print("FTP connection successful!")

    close_ftp(ftp)
    print("FTP connection closed.")