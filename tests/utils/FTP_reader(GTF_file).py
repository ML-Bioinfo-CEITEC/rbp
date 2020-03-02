import ftplib

# Username and password are optional.
def ftp_reader(server_address, user, password, path, filename):
  # Connect to server.
  ftp = ftplib.FTP(server_address) 
  # Provide user, password (or "", "").
  ftp.login(user, password) 
  # Move to path.
  ftp.cwd(path)
  # Retrive file and save it in local file.
  ftp.retrbinary("RETR " + filename, open(filename, "wb").write)
  # Quit server.
  ftp.quit()
  return filename

# The filename is not arbitrary.
ftp_reader(server_address, user, password, path, filename)
