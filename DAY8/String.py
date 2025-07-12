str = "RajaRamMohanRoy"

print(len(str))  # 15
print(str)  # RajaRamMohanRoy
print(str[0])  # R
print(str[7])  # M
print(str[14])  # y
print(str[-1])  # y
print(str[-8]) # M
print("-1---------------------------------------------")

print(str[0:4])  # Raja
print(str[4:7])  # Ram
print(str[7:12])  # Mahon
print(str[12:])  # Roy
print("-2--------------------------------")

print(str[ : ]) # RajaRamMohanRoy
print(str[ ::-1]) # yoRnahoMmaRajaR
print("---3---------------------------------------")

print(str[3:9])
print(str[ ::3])
print(str[12:4]) # no output
print("------4------------------------------------")

print(str[5: :-1])
print(str[-12:-5])
print(str[-5:-14:-1])
print("----------5--------------------------------")

print(str[ :-5:-1])
print(str[-5:-10])
print(str[7:13:0]) # Error: step cannot be zero