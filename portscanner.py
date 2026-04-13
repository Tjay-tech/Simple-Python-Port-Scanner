import socket 
def port_scanner(ip):
    #enter the first and last port you wnat to scan
    start_port = int( input("enter start port no:"))
    End_port = int (input("enter end port number:"))
    for p in range(start_port,End_port+1):
        try:
            #create socket interface 
            server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            server.settimeout(0.5)
            result = server.connect_ex((ip,p))
            if result == 0:
                print(f"port {p} is open on {ip}")                             
        except:
            pass  
        finally:
            server.close()

#collects ip addrss f network to be scanned 
target_ip=input("enter ip:").strip()
port_scanner(target_ip)
        

 

 