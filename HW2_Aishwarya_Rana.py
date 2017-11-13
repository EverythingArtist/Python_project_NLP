list1 =  ["fun", "couple", "love", "love", "comedy"];
list2 =  ["fast", "furious", "shoot", "action"];
list3 = ["couple", "fly", "fast", "fun", "fun", "comedy"];
list4 =  ["furious", "shoot", "shoot", "fun", "action"];
list5 =  ["fly", "fast", "shoot", "love", "action"];


Test = ["fast","couple","shoot","fly"];

fast = Test[0]
couple = Test[1]
shoot = Test[2]
fly = Test[3]


fastCom = 0
coupleCom = 0
shootCom = 0
flyCom = 0

fastAc = 0
coupleAc = 0
shootAc = 0
flyAc = 0

comedy = 0
action = 0

lastWordCom = list1[-1]    #taking last word for first list


cleanlist1 = []
[cleanlist1.append(x) for x in list1 if x not in cleanlist1]
print(cleanlist1)
if(cleanlist1[-1] == lastWordCom):          #if this list has same word as last word in list 1
    comedy += 1
    if(fast in cleanlist1):
        fastCom += 1
    if(couple in cleanlist1):
        coupleCom += 1
    if(shoot in cleanlist1):
        shootCom += 1
    if(fly in cleanlist1):
        flyCom += 1
else:
    action += 1
    if(fast in cleanlist1):
        fastAc += 1
    if(couple in cleanlist1):
        coupleAc += 1
    if(shoot in cleanlist1):
        shootAc += 1
    if(fly in cleanlist1):
        flyAc += 1

print("fastCom: " , fastCom)
print("coupleCom: " , coupleCom)
print("shootCom: " , shootCom)
print("flyCom: " , flyCom)
print("               ")
print("fastAc: " , fastAc)
print("coupleAc: " , coupleAc)
print("shootAc: " , shootAc)
print("flyAc: " , flyAc)
print("               ")


cleanlist2 = []
[cleanlist2.append(x) for x in list2 if x not in cleanlist2]
print(cleanlist2)
if(cleanlist2[-1] == lastWordCom):          #if this list has same word as last word in list 1
    comedy += 1
    if(fast in cleanlist2):
        fastCom += 1
    if(couple in cleanlist2):
        coupleCom += 1
    if(shoot in cleanlist2):
        shootCom += 1
    if (fly in cleanlist2):
        flyCom += 1
else:
    action += 1
    if(fast in cleanlist2):
        fastAc += 1
    if(couple in cleanlist2):
        coupleAc += 1
    if(shoot in cleanlist2):
        shootAc += 1
    if (fly in cleanlist2):
        flyAc += 1

print("fastCom: " , fastCom)
print("coupleCom: " , coupleCom)
print("shootCom: " , shootCom)
print("flyCom: " , flyCom)
print("            ")
print("fastAc: " , fastAc)
print("coupleAc: " , coupleAc)
print("shootAc: " , shootAc)
print("flyAc: " , flyAc)
print("                 ")


cleanlist3 = []
[cleanlist3.append(x) for x in list3 if x not in cleanlist3]
print(cleanlist3)
if(cleanlist3[-1] == lastWordCom):          #if this list has same word as last word in list 1
    comedy += 1
    if(fast in cleanlist3):
        fastCom += 1
    if(couple in cleanlist3):
        coupleCom += 1
    if(shoot in cleanlist3):
        shootCom += 1
    if(fly in cleanlist3):
        flyCom += 1
else:
    action += 1
    if(fast in cleanlist3):
        fastAc += 1
    if(couple in cleanlist3):
        coupleAc += 1
    if(shoot in cleanlist3):
        shootAc += 1
    if(fly in cleanlist3):
        flyAc += 1


print("fastCom: " , fastCom)
print("coupleCom: " , coupleCom)
print("shootCom: " , shootCom)
print("flyCom: " , flyCom)
print("                   ")
print("fastAc: " , fastAc)
print("coupleAc: " , coupleAc)
print("shootAc: " , shootAc)
print("flyAc: " , flyAc)
print("                 ")


cleanlist4 = []
[cleanlist4.append(x) for x in list4 if x not in cleanlist4]
print(cleanlist4)
if(cleanlist4[-1] == lastWordCom):          #if this list has same word as last word in list 1
    comedy += 1
    if(fast in cleanlist4):
        fastCom += 1
    if(couple in cleanlist4):
        coupleCom += 1
    if(shoot in cleanlist4):
        shootCom += 1
    if(fly in cleanlist4):
        flyCom += 1
else:
    action += 1
    if(fast in cleanlist4):
        fastAc += 1
    if(couple in cleanlist4):
        coupleAc += 1
    if(shoot in cleanlist4):
        shootAc += 1
    if(fly in cleanlist4):
        flyAc += 1


print("fastCom: " , fastCom)
print("coupleCom: " , coupleCom)
print("shootCom: " , shootCom)
print("flyCom: " , flyCom)
print("                 ")
print("fastAc: " , fastAc)
print("coupleAc: " , coupleAc)
print("shootAc: " , shootAc)
print("flyAc: " , flyAc)
print("                 ")

cleanlist5 = []
[cleanlist5.append(x) for x in list5 if x not in cleanlist5]
print(cleanlist5)
if(cleanlist5[-1] == lastWordCom):          #if this list has same word as last word in list 1
    comedy += 1
    if(fast in cleanlist5):
        fastCom += 1
    if(couple in cleanlist5):
        coupleCom += 1
    if(shoot in cleanlist5):
        shootCom += 1
    if(fly in cleanlist5):
        flyCom += 1
else:
    action += 1
    if(fast in cleanlist5):
        fastAc += 1
    if(couple in cleanlist5):
        coupleAc += 1
    if(shoot in cleanlist5):
        shootAc += 1
    if(fly in cleanlist5):
        flyAc += 1


print("fastCom: " , fastCom)
print("coupleCom: " , coupleCom)
print("shootCom: " , shootCom)
print("flyCom: " , flyCom)
print("                 ")
print("fastAc: " , fastAc)
print("coupleAc: " , coupleAc)
print("shootAc: " , shootAc)
print("flyAc: " , flyAc)
print("                 ")


print("Count of sentences that end with comedy are: ", comedy)
print("Count of sentences that end with action are: ",action)

posteriorProbCom = comedy / ((comedy+action)*1.0)
print("Posterior probability of comedy is: ",posteriorProbCom)

posteriorProbAct = action/ ((comedy+action)*1.0)
print("Posterior probability of actions is: ",posteriorProbAct)
print("                 ")

probFastCom = (fastCom * 1.0) / comedy
probFastAc = (fastAc*1.0)/action
print("probability of fast in comedy is: ", probFastCom)
print("probability of fast in action is: ", probFastAc)
print("                 ")

probCoupleCom = (coupleCom * 1.0) / comedy
probCoupleAc = (coupleAc*1.0)/action
print("probability of couple in comedy is: ", probCoupleCom)
print("probability of couple in action is: ", probCoupleAc)
print("                  ")

probShootCom = (shootCom * 1.0) / comedy
probShootAc = (shootAc*1.0)/action
print("probability of shoot in comedy is: ", probShootCom)
print("probability of shoot in action is: ", probShootAc)
print("                 ")

probFlyCom = (flyCom * 1.0) / comedy
probFlyAc = (flyAc*1.0)/action
print("probability of fly in comedy is: ", probFlyCom)
print("probability of fly in action is: ", probFlyAc)
print("                 ")

uniCom = []
uniAc = []
if(lastWordCom in cleanlist1):
 cleanlist1.remove("comedy")
 uniCom.extend(cleanlist1)
else:
    cleanlist1.remove("action")
    uniAc.extend(cleanlist1)


if(lastWordCom in cleanlist2):
 cleanlist2.remove("comedy")
 uniCom.extend(cleanlist2)
else:
    cleanlist2.remove("action")
    uniAc.extend(cleanlist2)

print(cleanlist2)

if(lastWordCom in cleanlist3):
 cleanlist3.remove("comedy")
 uniCom.extend(cleanlist3)
else:
    cleanlist3.remove("action")
    uniAc.extend(cleanlist3)

print(cleanlist3)

if(lastWordCom in cleanlist4):
 cleanlist4.remove("comedy")
 uniCom.extend(cleanlist4)
else:
    cleanlist4.remove("action")
    uniAc.extend(cleanlist4)

print(cleanlist4)

if(lastWordCom in cleanlist5):
 cleanlist5.remove("comedy")
 uniCom.extend(cleanlist5)
else:
    cleanlist5.remove("action")
    uniAc.extend(cleanlist5)

print(cleanlist5)
# print("this is unicome:",uniCom)
# print("this is uniac: ", uniAc)


def getUniqueWords(allWords) :
    uniqueWords = []
    for i in allWords:
        if not i in uniqueWords:
            uniqueWords.append(i)
    return uniqueWords


print("these are unique words in comedy: ",getUniqueWords(uniCom))
print("these are unique words in action: ",getUniqueWords(uniAc))

uniLastCom = getUniqueWords(uniCom)
uniLastAc = getUniqueWords(uniAc)
f = open("movie-review.NB",'w')
print >>f, 'Unique words in comedy sentences are: ', uniLastCom
print >>f, 'Unique Words in action sentences are ', uniLastAc
