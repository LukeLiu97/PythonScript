# -*- coding: utf-8 -*-
import wave
import numpy as np
import sys
import binascii


def text2list(path: str):
    lines = []
    try:
        with open(path, 'r', encoding="utf-8") as fd:
            lines = fd.readlines()
            lines = [element.strip() for element in lines]
    except FileNotFoundError as err:
        print("FileNotFoundError:{}".format(err))
        sys.exit("Please input a right file path,and retry!")
    return lines


def text2array():
    lines = text2list("audio_data.txt")
    nums = []
    for line in lines:
        num0 = line[0:4]
        num1 = line[4:]
        num0 = int.from_bytes(binascii.a2b_hex(num0), 'big')
        num1 = int.from_bytes(binascii.a2b_hex(num1), 'big')
        nums.append(num0)
        nums.append(num1)
    ndarray = np.array(nums)
    return ndarray.tostring()


def array2wave(wave_data):
    # 打开WAV文档
    f = wave.open(r"sweep.wav", "wb")

    # 配置声道数、量化位数和取样频率
    f.setnchannels(1)  # 单声道
    f.setsampwidth(2)  # 16bit
    f.setframerate(8000)  # 8K
    # 将wav_data转换为二进制数据写入文件
    f.writeframes(wave_data)
    f.close()


if __name__ == "__main__":
    wave_data = text2array()
    array2wave(wave_data)
