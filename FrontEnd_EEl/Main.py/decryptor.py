from decimal import Decimal
from aes import AES
import readwrite
aes = AES(0x2b7e151628aed2a6abf7158809cf4f3c)

# with open("Files/" + fileName, "rb") as f:
#     data = f.read()


def decrypt(fileName):
    data = readwrite.read(fileName)
    data = Decimal(data.decode("utf-8"))
    print(data)
    decrypted = hex(aes.decrypt(int(data)))
    bytes_object = bytes.fromhex(decrypted[2:])
    ascii_string = bytes_object.decode("ASCII")
    print(ascii_string)
    byte_val = ascii_string.encode()
    #readwrite.write(fileName, byte_val)
    with open("Downloads/" + fileName, "wb") as f:
        f.write(byte_val)
    print("\n")
    print("decrypted file")