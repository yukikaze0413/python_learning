import hashlib


def md5(str0):
    # 创建MD5对象
    hl = hashlib.md5()
    # 传入要加密的字符串
    hl.update(str0.encode('utf-8'))
    # 获取加密后的结果
    return hl.hexdigest()


if __name__ == '__main__':
    # 输入 明文
    str1 = input("Enter the string: ")
    # 调用 md5() 函数加密
    md5_str = md5(str1)
    # 输出 密文
    print("The MD5 hash of the string is:", md5_str)

'''hashlib库同样包含实现哈希加密的各种算法，如MD5、SHA1等。
这里使用MD5算法对输入的字符串进行加密，并输出其MD5哈希值。
这些方法的使用方法与 MD5 类似，通常包括以下几个步骤：
创建哈希对象，例如：hl = hashlib.sha256()
使用 update() 方法传入要哈希的数据。
调用 hexdigest() 方法获取哈希值的十六进制表示。'''
