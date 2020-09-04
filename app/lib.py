from machine import I2C, Pin, SPI, UART
import os


def show_file(filename):
    """显示文件内容"""
    with open(filename, 'r') as f:
        for line in f.readlines():
            print(line)


def show_fw():
    """检查固件是否正确,仅ESP板"""
    try:
        import esp
        print(esp.check_fw())
    except:
        print('仅ESP8266支持esp.check_fw()')


if __name__ == '__main__':
    # os.listdir()
    show_file('boot.py')
