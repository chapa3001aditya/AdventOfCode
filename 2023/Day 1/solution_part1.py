with open(r"2023/Day 1/Input.txt",'r')as text:
    text = text.readlines()
    text = list(map(lambda x: x.strip(),text))

calibration_value = list()

for query in text:
    number = str()
    for i in query:
        if i.isdigit():
            number += i
    calibration_value.append(number)


calibration_value = list(map(lambda x: x if len(x)<= 2 else x[0]+x[-1],calibration_value ))
calibration_value = list(map(lambda x: int(x[0]+x[0]) if len(x)==1 else int(x),calibration_value))
            
print(sum(calibration_value))
