"""
@file: 14.1 configparser.py
@time: 2019/01/28
@author: sch
"""
from configparser import ConfigParser, ExtendedInterpolation

# parser = ConfigParser()
# parser = ConfigParser(interpolation = None)
parser = ConfigParser(interpolation = ExtendedInterpolation())


# -------------------------------------------------------------------
# single file read
config_file = "./14.1 configparser.conf"

parser.read(config_file)

print()
print("special测试".center(80, '-'))
print('special url -> ', parser.get("special", "url"))

print()
print("has测试".center(80, '-'))
print("parser.has_section('bug_tracker') -> ", parser.has_section('bug_tracker'))
print("parser.has_section('bug') -> ", parser.has_section('bug'))
print("parser.has_option('bug_tracker', 'url') -> ", parser.has_option('bug_tracker', 'url'))
print("parser.has_option('bug_tracker', 'urls') -> ", parser.has_option('bug_tracker', 'urls'))

print()
print("get测试".center(80, '-'))
print("default server -> ", parser.get("DEFAULT", "server"))
print("bug_tracker server -> ", parser.get("bug_tracker", "server"))
print('bug_tracker port -> ', parser.getint("bug_tracker", "port"))

print()
print("set测试".center(80, '-'))
print("url -> ", parser.get("DEFAULT", "url"))

parser.set("DEFAULT", "server", "127.0.0.2")
print("url -> ", parser.get("DEFAULT", "url"))

with open(config_file, 'w') as f:
    parser.write(f)

print()
print("遍历所有节区".center(80, '-'))
for section_name in parser.sections():
    print("Section: ", section_name)  # DEFAULT节区打印不出
    print(" " * 4, "Options: ", parser.options(section_name))
    for key, value in parser.items(section_name):
        print(" " * 8, "{} = {}".format(key, value))  # 节区具体内容包含了 DEFAULT节区的所有内容
    print()

print()
print("遍历所有节区，以字典方式遍历".center(80, '-'))
for section_name in parser:
    print("Section: ", section_name)  # DEFAULT节区也被打印出来
    section = parser[section_name]
    print(" " * 4, "Options: ", list(section.keys()))
    for name in section:
        print(" " * 8, "{} = {}".format(name, section[name]))  # 节区具体内容包含了 DEFAULT节区的所有内容
    print()

# ---------------------------------------------------------------------
# config file list read
print("读取文件列表".center(80, '-'))
config_list = ['1.conf', '2.conf', "./14.1 configparser.conf"]
found = parser.read(config_list)

missing = set(config_list) - set(found)
print("missing file list: ", missing)
