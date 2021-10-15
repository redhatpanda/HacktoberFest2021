import rsa


def decryptmsg(cryptmessage, prvt_key):
    decrypted = rsa.decrypt(cryptmessage, prvt_key).decode()
    return decrypted
