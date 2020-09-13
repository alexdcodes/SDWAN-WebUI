import paramiko
import time


def do_calculation(number1, number2):
    return number1 + number2


def ssh_connection(ip1, username, password):
    pre_ssh_conn = paramiko.SSHClient()
    pre_ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pre_ssh_conn.connect(ip1, port=22, username=username,
                        password=password,
                        look_for_keys=False, allow_agent=False)

    ssh_conn = pre_ssh_conn.invoke_shell()
    banner_output = ssh_conn.recv(99535)
    ssh_conn.send("terminal length 0\n")
    time.sleep(1)
    ssh_conn.send("uname -a \n")
    time.sleep(1)
    output_lr = ssh_conn.recv(65535)
    print(output_lr.decode('utf-8'))
    return ip1, username, password, banner_output
