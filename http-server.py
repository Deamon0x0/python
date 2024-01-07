# from http.server import HTTPServer, BaseHTTPRequestHandler

# print("[*] If you don't know your Host address, type 'ipconfig' in the terminal[*] or use 127.0.0.1 \n")

# host = input("Enter Host Adress: ")

# try:
#  port = int(input("Enter deseired port: "))
# except:
#     print("Nigga 4digit integers MF no alphabets")
    
# class spin(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header("Content-type", 'text/html')
#         self.end_headers()
        
#         self.wfile.write(bytes("<head><body><h1><h1/>hello<body/></head>", "utf-8"))
#     def do_POST(self):
#         self.send_response(200)
#         self.send_header("Content-type", "application/json")
#         self.end_headers()
        
#         self.wfile.write(bytes("", "utf-8"))
        
# server = HTTPServer((host, port), spin)

# print(f"[*] Starting server at port {port}  [*]..\n")
# print("[+] Server is now running......[+]")

# server.serve_forever()
# # server.server_close()

# print("[*] The server has ended [*]")







from http.server import HTTPServer, BaseHTTPRequestHandler

print("[*] If you dont know what to enter as host input '127.0.0.1' or type ipconfig in the terminal [*]")
host = input("Enter Host: ")
try:
    port = int(input("Enter port number to use: "))
except:
    print("nigga 4 digit no interger")

class spinServer(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<h1>Idiot</h1>", "utf-8"))
    
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write()
        
server = HTTPServer((host, port), spinServer)

print("[*] the server is starting now.... [*]")
print(f"[+] the Server is running at {host}, {port} [+]\n")


# close = input("press Q to stop serving, C to continue: ").upper()

# if close == "Q":
#     print("[*] The server has ended [*]")
#     server.server_close()
# elif close == "C":
#     pass
# else:
#     print("invalid")

server.serve_forever()

