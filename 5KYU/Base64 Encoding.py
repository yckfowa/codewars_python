import base64


def to_base_64(string):
    string_byte = string.encode("ascii")
    base64_byte = base64.b64encode(string_byte)
    base64_string = base64_byte.decode("ascii").replace("=", "")

    return base64_string


def from_base_64(string):
    base64_string = " " + string + "=="
    base64_bytes = base64_string.encode("ascii")
    string_byte = base64.b64decode(base64_bytes)
    new_string = string_byte.decode("ascii")

    return new_string

