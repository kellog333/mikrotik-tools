import argparse
import os
import sys
import paramiko

def updateTik(host, user, passw, rules):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"[*] Connecting to {host}")
    client.connect(host, username=user, password=passw)
    print("[*] Adding rules")
    with open(rules, 'r') as rulefile:
        rule = rulefile.readlines()
        for i in rule:
            try:
                i = str(i)
                stdin, stdout, stderr = client.exec_command(f"{i}")
                print(f"[*] Adding {i}")
            except:
                print(stderr.readlines())
                pass
    print("[*] Done")
    print("[*] Closing connection")
    stdin.close()
    stdout.close()
    stderr.close()
    client.close()


def openFile(infile, user, passw, rules):
    with open(infile, 'r') as filer:
        hosts = filer.readlines()
        for i in hosts:
            i = i.strip()
            updateTik(i, user, passw, rules)


def main():
    parser = argparse.ArgumentParser(description="Run list of commands on multiple devices")
    parser.add_argument('-u', help="Username of devices", dest='username')
    parser.add_argument('-p', help="Password of devices", dest='password')
    parser.add_argument('-t', help="List of Mikrotik devices", dest='tiks')
    parser.add_argument('-c', help="Commands list", dest='rules')
    args = parser.parse_args()
    user = args.username
    passw = args.password
    infile = args.tiks
    rules = args.rules
    openFile(infile, user, passw, rules)


if __name__ == "__main__":
    main()
