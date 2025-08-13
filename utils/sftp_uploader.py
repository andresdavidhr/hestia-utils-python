import paramiko

def upload_file(local_path, sftp_config):
    transport = paramiko.Transport((sftp_config["host"], sftp_config["port"]))
    transport.connect(username=sftp_config["user"], password=sftp_config["password"])
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(local_path, sftp_config["remote_path"])
    sftp.close()
    transport.close()