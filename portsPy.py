"""
Author  : Chamuditha Ravindu
Website : chamuditharavindu.me
Github  : chamuditharav
"""
import socket


def scan(target, ports):
    
    print(f"\n Starting Scan for {str(target)}")
    print("\n\tPort \t Status")
    #print("Starting Scan for ")

    if("," in ports):
        for port in ports.split(","):
            scan_port(target, port)
    elif("-" in ports):
        ports = ports.split("-")
        #print(ports)
        if(int(ports[0].strip()) < int(ports[1].strip())):
            for port in range(int(ports[0].strip()), int(ports[1].strip())+1):
                scan_port(target, int(port))
        else:
            print("No")
            for port in range(int(ports[1].strip()), int(ports[0].strip())+1):
                scan_port(target, int(port))

    else:
        #for port in range(1, ports):
        scan_port(target, int(ports.strip()))


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f"[+]\t{str(port)} \t Open")
        sock.close()
    except:
        if(fullReport in ["y","Y","yes","YES"]):
            print(f"[-]\t{str(port)} \t Close")
        else:
            pass


targets = input("[*] Enter the ip address (seperate by ,): ")
ports = str(input("[*] Port/s eg:- (80) , (80,8080) , (70-500): "))
fullReport = str(input("[*] Full Report (All port status) (Y/N) Default is N : "))

if ',' in targets:
    print("[*] Scanning multiple targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)
