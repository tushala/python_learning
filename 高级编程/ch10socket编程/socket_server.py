import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 类型,协议
server.bind(("0.0.0.0", 8000))
server.listen()
sock, addr = server.accept()

# 获取从客户端发送的数据
data = sock.recv(1024)  # 以此获取1k的数据
print(data.decode("utf-8"))
sock.send(f"hello {data.decode('utf-8')}".encode("utf-8 "))
server.close()
sock.close()