#!/usr/bin/env python3
"""彭城七里徐州旅游攻略 - HTTPS 本地服务器 (绑定 127.0.0.1:443)"""
import http.server
import ssl
import os
import socket
import threading
import time

PORT = 443
CERT_FILE = os.path.join(os.path.dirname(__file__), 'server.crt')
KEY_FILE = os.path.join(os.path.dirname(__file__), 'server.key')
ROOT_DIR = os.path.dirname(__file__)

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT_DIR, **kwargs)

    def log_message(self, format, *args):
        pass

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'public, max-age=3600')
        super().end_headers()

def find_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def main():
    os.chdir(ROOT_DIR)
    local_ip = find_local_ip()

    server_address = ('127.0.0.1', PORT)
    httpd = http.server.HTTPServer(server_address, QuietHandler)

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print(f"=" * 60)
    print("彭城七里徐州旅游攻略 - HTTPS 服务器")
    print(f"=" * 60)
    print(f"本机地址: https://127.0.0.1:{PORT}")
    print(f"局域网地址: https://{local_ip}:{PORT} (需关闭防火墙)")
    print(f"项目目录: {ROOT_DIR}")
    print("-" * 60)
    print("按 Ctrl+C 停止服务器")
    print("=" * 60)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
        httpd.server_close()

if __name__ == '__main__':
    main()
