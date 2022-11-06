import time

import paramiko


HOST = '192.168.1.102'
USER = 'andrey'
password = 'Qwer1234'
command1 = 'docker start dev_postgres'
command2 = 'docker start dev_pgadmin'

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(HOST, 22, USER, password)
    stdin, stdout, stderr = ssh.exec_command(command1)
    stdin, stdout, stderr = ssh.exec_command(command2)
    lines = stdout.readlines()
    print("Done!")
except Exception as e:
    print("Doesn't start containers!\n {}".format(e))