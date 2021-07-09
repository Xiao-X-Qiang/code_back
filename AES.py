import base64
from Crypto.Cipher import AES
import hashlib

'''
采用AES对称加密算法
'''


# str不是32的倍数那就补足为16的倍数
def add_to_32(value):
    while len(value) % 32 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes


def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes

#计算密码的md5值
def get_md5(text):
    md = hashlib.md5()
    md.update(text.encode('utf-8'))
    return md.hexdigest()

# 加密方法
def encrypt_oracle(text,password):
    """
    使用ECB进行AES加密
    :param text: 待加密文本
    :param password: 秘钥
    :return: 使用秘钥加密后的文本
    """
    # 初始化加密器
    aes = AES.new(add_to_16(password), AES.MODE_ECB)
    # 先进行aes加密
    encrypt_aes = aes.encrypt(add_to_16(text))
    # 用base64转成字符串形式
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
    print(encrypted_text)
    return encrypted_text


# 解密方法
def decrypt_oralce(text,password):
    """
    使用ECB解密AES
    :param text: 待解密文本
    :param password: 秘钥
    :return: 解密后的文本
    """
    # 初始化加密器
    aes = AES.new(add_to_16(password), AES.MODE_ECB)
    # 优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
    # 执行解密密并转码返回str
    decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')
    print('decrypted_text', decrypted_text)
    return decrypted_text


if __name__ == '__main__':
    text = '''welcome to chacuo.net''' # 不能包括汉字

    password = "hello"
    # password = get_md5("helloworld")
    entrypted_text = encrypt_oracle(text,password)

    decrypt_oralce(entrypted_text,password)

    print(get_md5("helloworld"))
