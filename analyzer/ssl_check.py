import ssl
import socket

def get_ssl_info(domain):

    ctx = ssl.create_default_context()

    with socket.create_connection((domain, 443)) as sock:
        with ctx.wrap_socket(sock, server_hostname=domain) as ssock:
            cert = ssock.getpeercert()

    return cert
