from aes import AES
import readwrite
aes = AES(0x2b7e151628aed2a6abf7158809cf4f3c)


def encrypt(fileName):
    data = readwrite.read(fileName)
    # print(data)
    hex_string = '0x' + data.hex()
    print(hex_string)
    an_integer = int(hex_string, 16)
    print(an_integer)
    hex_value = hex(an_integer)
    print(hex_value)
    plain_text = int(hex_value, 16)  # 0x3243f6a8885a308d313198a2e0370734
    cipher_text = aes.encrypt(plain_text)
    print(cipher_text)
    str_val = str(cipher_text)
    byte_val = str_val.encode()
    readwrite.write(fileName, byte_val)
# # from fileinput import filename
# from aes import AES
# import readwrite
# # # plain_text = "hello world"
# # # hex_string = '0x' + b'hello world'.hex()
# fileName = "helloworld.txt"
# # with open("Files/" + fileName, "rb") as f:
# #     data = f.read()
# data = readwrite.read(fileName)
# print(data)
# hex_string = '0x' + data.hex()
# print(hex_string)
# an_integer = int(hex_string, 16)
# print(an_integer)
# hex_value = hex(an_integer)
# print(hex_value)
# plain_text = int(hex_value, 16)  # 0x3243f6a8885a308d313198a2e0370734
# aes = AES(0x2b7e151628aed2a6abf7158809cf4f3c)
# cipher_text = aes.encrypt(plain_text)
# print(cipher_text)
# str_val = str(cipher_text)

# # converting string to bytes
# byte_val = str_val.encode()
# readwrite.write(fileName, byte_val)
# # with open("Files/" + fileName, "wb") as f:
# #     f.write(byte_val)
# print("\n")
# print("encrypted file")
# # with open("Files/" + fileName, "rb") as f:
# #     data = f.read()
# # data = Decimal(data.decode("utf-8"))
# # print(data)

# # decrypted = hex(aes.decrypt(int(data)))
# # bytes_object = bytes.fromhex(decrypted[2:])
# # ascii_string = bytes_object.decode("ASCII")
# # print(ascii_string)