from .make_request import request, OK


def response(url) -> bool:
    return request(url).status_code == OK
