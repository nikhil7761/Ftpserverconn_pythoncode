import ftplib

# FTP server credentials
ftp_server = "172.30.1.22"  # Replace with your FTP server IP or domain
ftp_username = "sftpuser"      # FTP username
ftp_password = "Ssl@123"        # FTP password

# Establish connection to the FTP server
ftp = ftplib.FTP(ftp_server)

try:
    # Login to the server
    ftp.login(user=ftp_username, passwd=ftp_password)
    print(f"Successfully connected to FTP server: {ftp_server}")
    
    # List the files in the current directory
    print("Directory listing:")
    ftp.retrlines('LIST')
    
except ftplib.all_errors as e:
    print(f"Error: {e}")

# Close the connection to the FTP server
ftp.quit()
