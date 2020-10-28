import paramiko
import os
import sys
import argparse


def updateTik(host, user, passw, commun):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"[*] Connecting to {host}")
    client.connect(host, username=user, password=passw)
    print("[*] Adding Community")
    stdin, stdout, stderr = client.exec_command(f'snmp community add addresses=0.0.0.0 read-access=yes authentication-protocol=MD5 encryption-protocol=DES name={commun}')
    print("[*] Enabling")
    stdin, stdout, stderr = client.exec_command('snmp set enable=yes')
    stdin, stdout, stderr = client.exec_command('snmp set trap-version=2')
    stdin, stdout, stderr = client.exec_command(f'snmp set trap-community={commun}')
    print("[*] Closing connection")
    stdin.close()
    stdout.close()
    stderr.close()
    
def openFile(infile, user, passw, commun):
    with open(infile, 'r') as dafile:
        hosts = dafile.readlines()
        for i in hosts:
            i = i.rstrip()
            updateTik(i, user, passw, commun)
    
def main():
    parser = argparse.ArgumentParser(description='Mass update snmp settings on a compiled list of Mikrotik devices')
    parser.add_argument('-u', help='Username of device', dest='username')
    parser.add_argument('-p', help='Password of device', dest='password')
    parser.add_argument('-f', help='Text file of devices, one per line', dest='file')
    parser.add_argument('-c', help='Community name', dest='community')
    args = parser.parse_args()
    user = args.username
    passw = args.password
    infile = args.file
    commun = args.community
    openFile(infile, user, passw, commun)
    
if __name__ == "__main__":
    main()
