import secrets


def generate_unique_id():
    return secrets.token_hex(8)
