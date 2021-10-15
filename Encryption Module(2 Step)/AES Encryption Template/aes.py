import rsa
import rsa.randnum
import random
from Crypto.Cipher import AES
from secrets import token_bytes

key = rsa.randnum.read_random_bits(128)  # Generate a Random Key
pub_key, prvt_key = rsa.newkeys(
    512
)  # Generate Public & Private Keys for RSA Encryption
encrypted_aes_key = rsa.encrypt(key, pub_key)  # Encrypt the Random Key using RSA


def encrypt(msg):  # Sending End
    cipher = AES.new(
        key, AES.MODE_EAX
    )  # Using the Random Key, encrypt the data using AES
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(
        msg.encode("ascii")
    )  # Encode the Data to ASCII, since AES takes only Bytes
    return nonce, ciphertext, tag


# Send the Encrypted Data, along with the Encrypted Random Key (RSA Encrypted)
def decrypt(nonce, ciphertext, tag):  # Receiving End
    aes_key = rsa.decrypt(encrypted_aes_key, prvt_key)  # Decrypt the Key using RSA
    cipher = AES.new(
        aes_key, AES.MODE_EAX, nonce=nonce
    )  # Use the above key to decrypt the Data.
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode("ascii")  # Decode the text from ASCII to String
    except:
        return False


nonce, ciphertext, tag = encrypt(input("Enter a message: "))
plaintext = decrypt(nonce, ciphertext, tag)
print(f"Cipher text: {ciphertext}")
if not plaintext:
    print("Message is Corrupted")
else:
    print(f"Plain Text: {plaintext}")
