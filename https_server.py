import http.server
import ssl

server_address = ('0.0.0.0', 443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='server.crt', keyfile='server.key')
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Serving HTTPS on port 443 ...")
httpd.serve_forever()
