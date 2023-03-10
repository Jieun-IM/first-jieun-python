gender = int(input("여성이면 1, 남성이면 0을 입력하세요: "))
height = int(input("당신의 키는 얼마입니까? "))
huri = int(input("당신의 허리 둘레는 얼마입니까? "))

if gender == 1:
    RFM = 76 - (20*(height/huri)) + 12*gender
    print("당신의 RFM은   %f" %RFM)
    
elif gender == 0:
    RFM = 64 - (20*(height/huri)) + 12*gender
    print("당신의 RFM은   %f" %RFM)

else:
    print("1과 0 둘 중 하나만 입력하세요.")