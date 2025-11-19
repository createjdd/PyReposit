#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
struct 模块使用示例
用于将二进制数据转换为整数，或将整数转换为二进制数据
BMP 文件格式解析示例
"""

import base64
import struct

bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAA' +
                   'AAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/' +
                   '/f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/A' +
                   'HwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9' +
                   '//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f' +
                   '/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHw' +
                   'AfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//' +
                   '38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9' +
                   '//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAf' +
                   'AB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHw' +
                   'AfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//' +
                   '3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

def bmp_info(data):
    """
    解析 BMP 文件头信息
    
    BMP 文件格式：
    - 文件头：14 字节
    - 信息头：从偏移量 14 开始，40 字节
    - 宽度：偏移量 18（4 字节，有符号整数，小端序）
    - 高度：偏移量 22（4 字节，有符号整数，小端序）
    - 颜色深度：偏移量 28（2 字节，无符号整数，小端序）
    """
    # 检查 BMP 文件头（前 2 字节应该是 'BM'）
    if data[:2] != b'BM':
        raise ValueError('不是有效的 BMP 文件')
    
    # 使用 struct 解析二进制数据
    # '<' 表示小端序（little-endian）
    # 'i' 表示有符号整数（4 字节）
    # 'H' 表示无符号短整数（2 字节）
    
    # 宽度：偏移量 18，4 字节，有符号整数
    width = struct.unpack('<i', data[18:22])[0]
    
    # 高度：偏移量 22，4 字节，有符号整数
    height = struct.unpack('<i', data[22:26])[0]
    
    # 颜色深度（bits per pixel）：偏移量 28，2 字节，无符号整数
    color = struct.unpack('<H', data[28:30])[0]
    
    return {
        'width': width,
        'height': height,
        'color': color
    }

# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print(bi)
print('ok')
