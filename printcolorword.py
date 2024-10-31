#方法一：使用\033[显示方式m打印颜色
# 打印红色文本
print('\033[91m' + "This is red text" + '\033[0m')
# 打印绿色文本
print('\033[92m' + "This is green text" + '\033[0m')


#方法二：使用颜色库colorama打印颜色
import colorama
from colorama import init, Fore, Back, Style

init()
print(Fore.RED + "This is red text" + Style.RESET_ALL)
print(Fore.GREEN + "This is green text" + Style.RESET_ALL)
