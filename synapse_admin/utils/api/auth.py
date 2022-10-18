from synapse_admin.types.config import LogedUser

from . import requests
from synapse_admin.utils import security

def login(url, username, password):
    data = {
        "type": "m.login.password",
        "user": username,
        "password": password
    }

    status_code, resp_data = requests.post(url+"/_matrix/client/r0/login", data)
    if status_code != 200:
        print("Login failed")
        exit(1)

    return resp_data.get("user_id"), resp_data.get("access_token")


def register(url, user, secret_key):
    reg_url = url + "/_synapse/admin/v1/register"

    status_code, resp_data = requests.get(reg_url)
    if status_code != 200:
        print("Error! Received {}".format(status_code))
        if 400 <= status_code < 500:
            try:
                print(resp_data["error"])
            except Exception:
                pass
        exit(1)

    nonce = resp_data["nonce"]
    mac = security.generate_mac(secret_key, nonce, user)

    data = {
        "nonce": nonce,
        "username": user.username,
        "password": user.password,
        "mac": mac,
        "admin": user.admin,
        "user_type": None,
    }

    status_code, resp_data = requests.post(reg_url, data)
    if status_code != 200:
        print("Error! Received {}".format(status_code))
        if 400 <= status_code < 500:
            try:
                print(resp_data["error"])
            except Exception:
                pass
        exit(1)

    user.id = resp_data["user_id"]