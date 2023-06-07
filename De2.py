'''
        ===== Đề 2 =====
Câu 1: Nêu vai trò của địa chỉ IP và cổng (port) trong mạng
Câu 2: Xây dựng chương trình theo mô hình client-server sử
    dụng StreamWriter và thực hiện các công việc sau:
    a, Client: gửi tín hiệu kết nối server
    - Gửi lệnh UP hoặc LO và một xâu ký tự đến server
    - Nhận kết quả về
    b, Server: Chấp nhận kết nối
    - Hiển thị thông tin Client
    - Kiểm tra xem lệnh nhận được là lệnh gì (UP/LO)
    - Nhận xâu ký tự từ Client
    - Thực hiện biến đổi xâu thành chữ hoa (UP) hoặc
    chữ thường (LO)
    - Trả về kết quả cho client
'''

#=============================================================
# Câu 1:
# Địa chỉ IP và cổng (port) đóng vai trò quan trọng trong việc giao tiếp giữa các
# thiết bị trong mạng.

#     - Địa chỉ IP là một địa chỉ duy nhất được gán cho mỗi thiết bị trong mạng
# để xác định vị trí của thiết bị đó trên mạng. Địa chỉ IP được sử dụng để định
# tuyến gói dữ liệu đến đúng thiết bị và nơi đích trong mạng.

#     - Cổng (port) là một con số được gán cho mỗi ứng dụng hoặc dịch vụ trong
# một thiết bị để phân biệt các ứng dụng/dịch vụ khác nhau. Cổng đóng vai trò
# như một kênh truyền thông để dữ liệu được gửi và nhận giữa các ứng dụng/dịch
# vụ trên mạng.

# Khi một thiết bị muốn gửi dữ liệu đến một thiết bị khác trong mạng, nó sẽ sử
# dụng địa chỉ IP của thiết bị đích và cổng của ứng dụng/dịch vụ đang được sử
# dụng để gửi dữ liệu đến thiết bị đó. Cổng đảm bảo rằng dữ liệu sẽ được gửi đến
# đúng ứng dụng/dịch vụ đang được sử dụng trên thiết bị đích, trong khi địa chỉ
# IP đảm bảo rằng dữ liệu sẽ được gửi đến thiết bị đích đúng và vị trí đích trong
# mạng.

# Vì vậy, địa chỉ IP và cổng đóng vai trò quan trọng trong việc định tuyến dữ
# liệu và truyền thông giữa các thiết bị trong mạng.
#=============================================================
# Câu 2:
                    # -----SERVER-----
import socket

host= 'localhost'
port= 9050

def create_connect(host, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind((host, port))
    sk.listen(5)
    print('Server san sang')
    return sk

def create_data(mes):
    data = mes + '\0'
    return data

def send_data(sk, mes):
    message = create_data(mes)
    sk.sendall(message.encode('utf-8'))

def recv_data(sk):
    data = bytearray()
    msg = ''
    while not msg:
        data1 = sk.recv(1024)
        if not data1: raise ConnectionError()
        data = data + data1
        if b'\0' in data1:
            msg = data.rstrip(b'\0')
    msg = msg.decode('utf-8')
    return msg

if __name__=='__main__':
    sk = create_connect(host, port)
    client_sk, client_addr = sk.accept()
    print(f'Dia chi client: {client_addr}')
    while True:
        # Nhan 1
        data = recv_data(client_sk)
        print('Client: %s'%data)
        if data=='bye':
            client_sk.close()
            break
        # Gui 2
        lenh, xau = (list)(data.split('|'))
        result = ''
        if lenh.upper()=='UP': result = xau.upper()
        elif lenh.upper()=='LO': result = xau.lower()
        else: result = xau
        send_data(client_sk, result)
        print('SERVER: %s'%result)

                    # -----CLIENT-----
# import socket

# host= 'localhost'
# port= 9050

# def create_connect(host, port):
#     sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sk.bind((host, port))
#     sk.listen(5)
#     print('Server san sang')
#     return sk

# def create_data(mes):
#     data = mes + '\0'
#     return data

# def send_data(sk, mes):
#     message = create_data(mes)
#     sk.sendall(message.encode('utf-8'))

# def recv_data(sk):
#     data = bytearray()
#     msg = ''
#     while not msg:
#         data1 = sk.recv(1024)
#         if not data1: raise ConnectionError()
#         data = data + data1
#         if b'\0' in data1:
#             msg = data.rstrip(b'\0')
#     msg = msg.decode('utf-8')
#     return msg

# if __name__=='__main__':
#     sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sk.connect((host, port))
    
#     while True:
#         #Gui 1
#         msg = input('Client: Nhap lenh|xau: ')
#         send_data(sk, msg)
#         if msg=='bye':
#             sk.close()
#             break
#         #Nhan 2
#         msg = recv_data(sk)
#         print('Server: %s'%msg)