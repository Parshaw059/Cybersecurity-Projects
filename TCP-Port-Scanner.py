import socket
U_ip = input("Enter Your IP for Port Scanning :-")
S_p=int(input("Enter the Start port :-"))
E_p=int(input("Enter the End port :-"))

for i in range(S_p,E_p+1,1):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result=sock.connect_ex((U_ip,i))
    if result==0:
        print(f"Port {i} is open")
    else:
        print(f"Port {i} is closed")
    sock.close()
