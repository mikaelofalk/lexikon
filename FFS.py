#!/usr/bin/python
import sys
import re
import random


"""
    Falks FrågeSpel
"""


def CommaSplit(List):
    for i in range(len(List)):
        
        List[i]=List[i].split(":")
    y = [s for s in List if len(s) == 2]
    return y


def List2Dict(List):

    my_dict = {}
    for i in range(len(List)):
        my_dict[i]=List[i]
    return my_dict
    


def QuizzGame(Dictionary, k, Straff):
    #print(len(Dictionary))
    Q = (random.choice(list(Dictionary)))
    #A = random.sample(list(Dictionary), 3)
    #for i in range(len(A)):
    #    A[i]=(Dictionary[A[i]])

    #A.append(Dictionary[Q])

    #random.shuffle(A)
    print("Antal frågor kvar: ", len(Dictionary))
    QuestionItem=Dictionary[Q]
    print("\n", QuestionItem[1], "\n")
    
    SpellTest=input("Spell it! \n")
    if SpellTest.strip(',.').lower() == QuestionItem[0].strip(',.').lower():
        print ("Right")
        k=k+100
        del Dictionary[Q]

        if len(Dictionary)>0:
            QuizzGame(Dictionary, k, Straff)
        else:
            print("\n Quizz completed")
    else:
        print ("Wrong!")
        print ("Wrong, we were looking for: ", QuestionItem[0])
        k=k+100
        Nr = k


        for i in range(Straff):
            Dictionary[Nr+i]=QuestionItem
            
        
        QuizzGame(Dictionary, k, Straff)

Straff = input("Hej och välkommen till Falks FrågeSpel, hur många straff frågor vill du få om du svarar fel? \n")
Straff=int(Straff)
Titlar = []
TitelList=[]
Text = []
Falks_Magnifika_Lexikon = {}
for i in sys.argv[1:]:
    file = open(i, 'r')
    text=file.read()
    

    Titel = (re.split(r'\*{3}', text))
    Titel.pop(0)
    Titel = list(filter(None, Titel))
    for i in Titel:
     
        if i == i.upper():
            TitelList.append(i)
        else:
            Text.append(i)
if len(TitelList)>1 and len(TitelList)==len(Text):
    for i in range(len(TitelList)):
        Falks_Magnifika_Lexikon[i] = [TitelList[i], Text[i]]

    r=0
    print("\nVälj vilken titel du vill öva på:\n")
    for i in range(len(Falks_Magnifika_Lexikon)):
        X=(Falks_Magnifika_Lexikon[i])
        print(r,X[0])
        r=r+1
    Val=int(input())
    X = (Falks_Magnifika_Lexikon[Val])
else:
    X=[0]
    X.append(Text[0])

        
lines=X[1]
lines = [s.strip() for s in lines.splitlines()]
lines2 = [x for x in lines if x]
List2 = CommaSplit(lines2)
Dictionary = List2Dict(List2)

k=0

QuizzGame(Dictionary, k, Straff)
