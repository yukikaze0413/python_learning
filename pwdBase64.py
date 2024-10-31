import base64


def pwdbase64(pwd):
    pwd0 = base64.b64encode(pwd.encode('utf-8')).decode()
    return pwd0


def pwdbase64_decode(pwd):
    pwd1 = base64.b64decode(pwd.encode('utf-8')).decode()
    return pwd1


if __name__ == '__main__':
    pwd1 = input("请输入密码：")
    str1 = pwdbase64(pwd1)
    print(f"加密后密码为：{str1}")
    print(f"解密后密码为：{pwdbase64_decode(str1)}")

'''
Base64是一种将二进制数据转换为ASCII字符的编码方式，常用于在需要通过文本传输的场合，如电子邮件、URL等。
Python提供了base64模块来对二进制数据进行编码和解码。
'''