with open(r"2023/Day 1/Input.txt",'r')as text1:
    text1 = text1.readlines()
    text1 = list(map(lambda x: x.strip(),text1))

num1 = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0}


text2 = list()

calibration_value1 = list()


for sample in text1:
    sample_str = ""
    sub_str = ''
    i = 0
    while i in range(len(sample)):
        if sample[i].isdigit():
            sample_str += str(sample[i])
            i += 1 
        else:
            sub_str +=sample[i]
            for num1_eng , val in num1.items(): 
                if num1_eng in sub_str:
                    sample_str += str(num1[num1_eng])
                    sub_str = sub_str[-1]
            i += 1    

    text2.append(sample_str)
                
print(text2)
for query1 in text2:
    number1 = str()
    for i in query1:
        if i.isdigit():
            number1 += i
    calibration_value1.append(number1)


calibration_value1 = list(map(lambda x: x if len(x)<= 2 else x[0]+x[-1],calibration_value1 ))
calibration_value1 = list(map(lambda x: int(x[0]+x[0]) if len(x)==1 else int(x),calibration_value1))
            
print(calibration_value1)
print(sum(calibration_value1))
