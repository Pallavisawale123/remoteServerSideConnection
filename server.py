import logging
import socket
from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler

import utils.file_util as file_util

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(threadName)-12s][%(levelname)-5s] %(message)s",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler()
    ]
)

# Get server IP and port
hostname = socket.gethostname()
SERVER_HOST = socket.gethostbyname(hostname)
SERVER_PORT = 8000


# Restrict to a particular path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


def check_connection():
    """
    Method to check the connection with the server.
    :return: True if client connection is successful, else False
    """
    return True


# Create and run the server
with SimpleXMLRPCServer(
        (SERVER_HOST, SERVER_PORT),
        requestHandler=RequestHandler,
        logRequests=True,
        allow_none=True
) as server:
    logging.info("Registering functions...")
    server.register_function(file_util.write_file)
    server.register_function(file_util.get_sha256)
    server.register_function(file_util.get_sha256)
    server.register_function(file_util.delete_file)
    server.register_function(file_util.is_file_exists)
    server.register_function(check_connection, 'check_connection')

    logging.info("Starting server on %s:%d", SERVER_HOST, SERVER_PORT)
    server.serve_forever()
