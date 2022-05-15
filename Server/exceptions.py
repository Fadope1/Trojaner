class CloseServer(Exception):
    """Raised when admin closes the server"""


class AccessDenied(Exception):
    """Raised when a non admin tries to do something -> wrong password"""
