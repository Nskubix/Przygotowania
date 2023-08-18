import time
startPos1 = input("Podaj pozycję startową króla np. A2 B4 ")
endPos1 = input("Podaj końcową pozycję króla np. H7 E5 ")
startPos = [startPos1[0],int(startPos1[1])]
endPos = [endPos1[0],int(endPos1[1])]
currentPos = startPos
ileruchow = 0
jakieruchy = []
startime = time.time()
if(startPos[1] > 8 or endPos[1] > 8):
    print("Za duża liczba")
    exit()

translatee = [
    {"letter": "A","number": 1},
    {"letter": "B","number": 2},
    {"letter": "C","number": 3},
    {"letter": "D","number": 4},
    {"letter": "E","number": 5},
    {"letter": "F","number": 6},
    {"letter": "G","number": 7},
    {"letter": "H","number": 8},
]

for trans in translatee:
    if(trans["letter"] == currentPos[0]):
        currentPos[0] = trans["number"]
    if(trans["letter"] == endPos[0]):
        endPos[0] = trans["number"]


while(1 == 1):
    if(currentPos[0] < endPos[0] and currentPos[1] < endPos[1]):
        currentPos[0] += 1
        currentPos[1] += 1
        jakieruchy.append("NE")
        ileruchow +=1
        continue
    if(currentPos[0] > endPos[0] and currentPos[1] > endPos[1]):
        currentPos[0] -= 1
        currentPos[1] -= 1
        jakieruchy.append("SW")
        ileruchow +=1
        continue
    if(currentPos[0] > endPos[0] and currentPos[1] < endPos[1]):
        currentPos[0] -= 1
        currentPos[1] += 1
        jakieruchy.append("NW")
        ileruchow +=1
        continue
    if(currentPos[0] < endPos[0] and currentPos[1] > endPos[1]):
        currentPos[0] += 1
        currentPos[1] -= 1
        jakieruchy.append("SE")
        ileruchow +=1
        continue
    if(currentPos[0] < endPos[0] and not currentPos[1] < endPos[1]):
        currentPos[0] += 1
        jakieruchy.append("E")
        ileruchow +=1
        continue
    if(currentPos[1] < endPos[1] and not currentPos[0] < endPos[0]):
        currentPos[1] += 1
        jakieruchy.append("N")
        ileruchow +=1
        continue
    if(currentPos[0] > endPos[0] and not currentPos[1] > endPos[1]):
        currentPos[0] -= 1
        jakieruchy.append("W")
        ileruchow +=1
        continue
    if(currentPos[1] > endPos[1] and not currentPos[0] > endPos[0]):
        currentPos[1] -= 1
        jakieruchy.append("S")
        ileruchow +=1
        continue


    if(currentPos[0] == endPos[0] and currentPos[1] == endPos[1]):
        break

print(ileruchow)
for ruch in jakieruchy:
    print(ruch,end= " ")
print("\n")
endtime = time.time()
print("Czas:", endtime-startime+"s")
input()