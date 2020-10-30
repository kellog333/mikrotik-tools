# mikrotik-tools

A collection of Mikrotik mass update tools

usage: mikrotikfilter.py [-h] [-u USERNAME] [-p PASSWORD] [-t TIKS] [-r RULES]

Mass update firewall filter rules on Mikrotik devices

optional arguments:
  -h, --help   show this help message and exit
  -u USERNAME  Username of devices
  -p PASSWORD  Password of devices
  -t TIKS      List of Mikrotik devices
  -r RULES     List of rules


usage: mikrotiksnmp.py [-h] [-u USERNAME] [-p PASSWORD] [-f FILE]
                       [-c COMMUNITY]

Mass update snmp settings on a compiled list of Mikrotik devices

optional arguments:
  -h, --help    show this help message and exit
  -u USERNAME   Username of device
  -p PASSWORD   Password of device
  -f FILE       Text file of devices, one per line
  -c COMMUNITY  Community name

