import json, ssl
import urllib.request


def _get_ssl_context():
    """
        Return ssl context with disabled check hostname
    """
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    return ctx


def get(url, access_token = None):
    if access_token:
        headers = {
            "Authorization": "Bearer {}".format(access_token)
        }
        req = urllib.request.Request(url, headers=headers)
    else:
        req = urllib.request.Request(url)

    with urllib.request.urlopen(req, context=_get_ssl_context()) as f:
        return f.getcode(), json.loads(f.read().decode())
    

def post(url, data, access_token = None):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if access_token:
        headers["Authorization"] = "Bearer {}".format(access_token)

    json_data = json.dumps(data).encode("utf-8")

    req = urllib.request.Request(url, json_data, headers)
    with urllib.request.urlopen(req, context=_get_ssl_context()) as f:
        return f.getcode(), json.loads(f.read().decode())


def put(url, data, access_token):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if access_token:
        headers["Authorization"] = "Bearer {}".format(access_token)

    json_data = json.dumps(data).encode("utf-8")

    req = urllib.request.Request(url, json_data, headers, method="PUT")
    with urllib.request.urlopen(req, context=_get_ssl_context()) as f:
        return f.getcode(), json.loads(f.read().decode())
