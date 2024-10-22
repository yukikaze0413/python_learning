# 本程序将使用split()函数对字符串进行分词操作
import re


def get_char(txt):
    # 设定分割符参数
    vlist = re.split(r'[\s,.!?:;]\s*', txt)
    # 生成字典变量
    vdic_freq = dict()
    # 遍历列表，统计每个词的频率
    for vchar in vlist:
        if vchar in vdic_freq:
            vdic_freq[vchar] += 1
        else:
            vdic_freq[vchar] = 1
    # 进行降序排列
    vdic_sort = sorted(vdic_freq.items(), key=lambda x: x[1], reverse=True)
    # 返回字典
    return vdic_sort


if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        vtext = f.read()
    vstr = get_char(vtext)
    print('列出文本中出现的单词：\n')
    print(vstr)
