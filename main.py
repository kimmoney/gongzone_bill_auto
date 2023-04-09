import serial
import datetime

print('serial ' + serial.__version__)

# Set a PORT Number & baud rate
PORT = 'COM3'
BaudRate = 9600

ARD= serial.Serial(PORT,BaudRate)

str="\r영수증NO : {}\n\r사업자번호 : 1205000430\n\r주소 : 인천시 부평구 마장로 49\n\r성명 : 장수연\n\r전화 : 032-521-5777\n\r일자 : {}\n\r \n\r\x1b!\x00------------------------------------------\n\r\n\r소계 :          50,000\n\r\x1b!\x00------------------------------------------\n\r현금 :          50,000\n\r\x1b!\x00------------------------------------------\n\r-\n\r-\n\r-\n\r-\n\r-\n\r-".format(datetime.datetime.now().strftime("%f"),datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# B=str(B)
# Trans="Q" + A + B
# Trans= Trans.encode('utf-8')


# while (True):
ARD.write(str.encode("EUC-KR"))  # Q12345678 전송
# print(A)
print(str.encode("EUC-KR"))
# print(datetime.datetime.now().strftime("%f"))
# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))