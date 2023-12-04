with open(r"2023/Day 2/Input.txt",'r') as text:
    text = text.readlines()
    text = list(map(lambda x: x.strip().split(";"),text))
   
game_ids = list()
sumofpow = list()
for round in text :
    # print(round)
    red,green,blue = [],[],[]
    for i in range(len(round)):
        if i==0:
            round_0= round[i].split(':')
            id = round_0[i].split(" ")[1]
            round_1 = list(map(lambda x: x.strip(),round_0[1].split(',')))
            for box in round_1:
                if box.endswith(' red'):
                    red.append(int(box.split(" ")[0]))
                elif box.endswith(' green'):
                    green.append(int(box.split(" ")[0]))
                elif box.endswith(' blue'):
                    blue.append(int(box.split(" ")[0]))
            
        else:
            round_11= round[i].split(',')
            round_11 = list(map(lambda x: x.strip(),round[i].split(',')))
            # print(round_11)
            for box in round_11:
                if box.endswith(' red'):
                    red.append(int(box.split(" ")[0]))
                elif box.endswith(' green'):
                    green.append(int(box.split(" ")[0]))
                elif box.endswith(' blue'):
                    blue.append(int(box.split(" ")[0]))
    
    sumofpow.append(max(red)*max(green)*max(blue))     # part 2

    red_stat, green_stat, blue_stat = True,True,True

    for val in red:
        # print(val)
        if val <= 12:
            # print('continued_red')
            continue   
        else:
            red_stat = False

    if red_stat:
        for val in green:
            if val <= 13:
                # print('continued_green')
                continue       
            else:
                green_stat = False

    if red_stat and green_stat:
        for val in blue:
            if val <= 14:
                continue
            else:
                blue_stat = False

    if red_stat and green_stat and blue_stat:
        game_ids.append(int(id))  #for part 1
        
print('part 1:',sum(game_ids))
print('part2:',sum(sumofpow))
