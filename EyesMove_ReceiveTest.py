import serial
from time import sleep

def recv(serial):
    while True:
        data = serial.read_all()
        if data == '':
            continue
        else:
            break
        sleep(0.3)
    return data

if __name__ == '__main__':
    serial = serial.Serial('COM9', 9600, timeout=0.5)  # 打开COM并设置波特率为115200，COM1只适用于Windows
                                                          # ser.timeout＝0.5  # 读超时设置
                                                            # ser.writeTimeout＝0.5  # 写超时
    if serial.isOpen():
        print("open success")
    else:
        print("open failed")

    while True:

        # str1 = input("请输入要发送到串口的话：")
        # a = str1 + "\n"
        # # print(len(a))
        # serial.write((a).encode("gbk"))#write(data)：发送data，并返回发送字节数。
        #                                 # 如果bytes和bytearray可用（python 2.6以上），
        #                                 # 则接受其作为参数；否则接受str作为参数。
        #                                 #encode将字符串转换成参数指定的格式,此处转换为‘gbk’格式，防止出现中文乱码

        #sleep(0.1)
        data = recv(serial)
        if data != b'':
            if len(data) == 8:
                dat_x = data[2] * 256
                data_x = dat_x + data[3]
                print(data_x)

                dat_y = data[4] * 256
                data_y = dat_y + data[5]
                print(data_y)

                print("数据传输成功")
        #data = data.decode('utf-8')  # 由于串口使用的是字节，故而要进行转码，否则串口会不识别
        # print(type(data))
        # #print('get data from serial port:', data)
        # print("receive : ", data.decode("gbk"))