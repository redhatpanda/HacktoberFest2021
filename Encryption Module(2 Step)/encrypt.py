import rsa


def encryptmsg(message, pub_key):
    encrypted = rsa.encrypt(message.encode(), pub_key)
    return encrypted
