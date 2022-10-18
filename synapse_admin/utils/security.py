import random, hashlib, hmac

password_length = 14

digits = "1234567890"
letters = "abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ"
characters = list(letters + digits + "-[]{}()<>")
random.shuffle(characters)


def generate_password():
    return "".join(
            [random.choice(characters) for i in range(password_length)])


def generate_mac(shared_secret, nonce, user):
    mac = hmac.new(key=shared_secret.encode("utf8"), digestmod=hashlib.sha1)

    mac.update(nonce.encode("utf8"))
    mac.update(b"\x00")
    mac.update(user.username.encode("utf8"))
    mac.update(b"\x00")
    mac.update(user.password.encode("utf8"))
    mac.update(b"\x00")
    mac.update(b"admin" if user.admin else b"notadmin")
    return mac.hexdigest()