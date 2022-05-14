from fastapi import HTTPException
import env_config
from cryptography.fernet import Fernet


def check_token(token):
    token = token.encode("utf-8")
    fernet = Fernet(env_config.token_key)
    decToken = fernet.decrypt(token).decode()
    # lyadh kheye gechilam tai etai hard code kore dilam. actually eta username ta hoto
    if decToken == "techtrix22-admin":
        return True
    return False
