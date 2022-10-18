from . import requests

def set_display_name(url, access_token, user):
    data = {
        "displayname": user.displayname
    }
    status_code, resp_data = requests.put(
        "{}/_synapse/admin/v2/users/{}".format(url, user.id),
        data, access_token
    )
    if status_code != 200:
        print("Error! Received {}".format(status_code))
        if 400 <= status_code < 500:
            try:
                print(resp_data["error"])
            except Exception:
                pass
        exit(1)


def add_to_room(url, access_token, user_id, room_id):
    data = {
        "user_id": user_id
    }

    status_code, resp_data = requests.post(
        "{}/_synapse/admin/v1/join/{}".format(url, room_id), data, access_token)
    if status_code != 200:
        print("Error! Received {}".format(status_code))
        if 400 <= status_code < 500:
            try:
                print(resp_data["error"])
            except Exception:
                pass
        exit(1)