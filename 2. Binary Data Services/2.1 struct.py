"""
@file: 2.1 struct.py
@time: 2019/01/17
@author: sch
"""
import struct


def Diff():
    a = 0x12345678

    print('{msg} default -> {result}'.format(msg = hex(a), result = ' '.join([hex(r) for r in struct.pack('i', a)])))
    print('{msg} little endian -> {result}'.format(msg = hex(a), result = ' '.join([hex(r) for r in struct.pack('<i', a)])))
    print('{msg} big endian -> {result}'.format(msg = hex(a), result = ' '.join([hex(r) for r in struct.pack('>i', a)])))


def IsBigEndian():
    a = 0x12345678

    result = struct.pack('i', a)
    if hex(result[0]) == '0x78':
        print("Machine is little endian")
    else:
        print("Machine is big endian")  # human read

    import sys
    print("sys.byteorder -> ", sys.byteorder)  # use system byteorder


def PackNetworkPcap(fmt, s = b'hello world'):
    fmt = fmt.format(len = len(s))
    p_1 = struct.pack(fmt, len(s), s)
    print("pack {msg} use \"{fmt}\"  -> {chars}".format(msg = s, fmt = fmt, chars = p_1))
    return p_1


def Calcsize():
    print('ci -> {} bytes.'.format(struct.calcsize('ci')))  # 默认本机，字节补齐
    print('@ci -> {} bytes.'.format(struct.calcsize('@ci')))  # 本机size大小，字节补齐
    print('=ci -> {} bytes.'.format(struct.calcsize('=ci')))  # byte 顺序为本机，size 为标准字节数
    print('<ci -> {} bytes.'.format(struct.calcsize('<ci')))  # byte 顺序小端，size 为标准字节数
    print('>ci -> {} bytes.'.format(struct.calcsize('>ci')))  # byte 顺序大端，size 为标准字节数
    print('!ci -> {} bytes.'.format(struct.calcsize('!ci')))  # byte 顺序网络序(大端)，size 为标准字节数


def Unpack(fmt, string):
    result = struct.unpack(fmt, string)
    print("unpack {string} use {fmt} -> {chars}".format(string = string, fmt = fmt, chars = tuple([hex(r) for r in result])))


def Pack(fmt, msg = (0x11223344, 0x55667788)):
    result = struct.pack(fmt, *msg)
    print("pack {msg} use \"{fmt}\" -> {chars}".format(fmt = fmt, chars = " ".join([hex(r) for r in result]), msg = result))
    return result


def PackInto(s):
    import ctypes

    fmt = "I{len}s".format(len = len(s))
    f = ctypes.create_string_buffer(struct.calcsize(fmt))

    print("Before pack buffer is -> {f}".format(f = f.raw))
    struct.pack_into(fmt, f, 0, *(len(s), s))
    print("After pack buffer is -> {f}".format(f = f.raw))

    return fmt, f


def UnpackFrom(fmt, buffer):
    result = struct.unpack_from(fmt, buffer, 0)
    print("Unpack from \'{f}\' -> {r} ({type})".format(f = fmt, r = result, type = type(result)))


def IterUnpack(fmt, buffer):
    result = struct.iter_unpack(fmt, buffer)
    print("Unpack from \'{f}\' -> {r} ({type})".format(f = fmt, r = result, type = type(result)))
    print("Unpack result -> ", [r for r in result])


if __name__ == '__main__':
    # Diff()
    # IsBigEndian()
    # Calcsize()

    # Unpack('ii', Pack('ii'))
    # print()
    # Unpack('<ii', Pack('<ii'))
    # print()
    # Unpack('>ii', Pack('>ii'))

    # print()
    PackNetworkPcap('>H{len}s')
    PackNetworkPcap('>I{len}s')
    PackNetworkPcap('>L{len}s')
    PackNetworkPcap('>Q{len}s')
    PackNetworkPcap('>f{len}s')

    # UnpackFrom(*PackInto(b'hello world'))
    # print()
    # IterUnpack(*PackInto(b'hello world'))
