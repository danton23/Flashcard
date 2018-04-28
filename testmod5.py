import random
vocab = {}
def Update():
    new=input("please add a new item to the dictionary  ")
    vocab[new]={}
#Update()#this adds new dictionary to vocab
def Test():
    print(vocab['jools'])
#Test()

def Choose():
    print(vocab)
    choice=input("please select a dictionary item \n")
    print(vocab[choice])
#Choose()   #this will print the users choice of dictionary
def AddEntry():
        addingnew=input("please choose a new dictionary to add to vocab \n")
        vocab[addingnew]={}
        print (vocab)
#AddEntry() #this is the SAME as update
def Update2():
    print ("here are the existing dictionaries" , vocab)
    choice=input ("which do you choose?")
    for item in vocab:
     if choice== item in vocab:
        newkey=input("choose a new German word \n")
        newval=input("choose a new English translation  \n")
        vocab[item].update({newkey:newval})
        print(item)
#Update2()    #this will allow user to see and then select dictionary and input
            # a new key and value into it
def UserTest():
    for x in vocab:
        print (x)  #this is necessary so ONLY prints keys (not keys and vals inside)   
    choice=input(" \n please select a dictionary item ")
    if choice in vocab.keys():  #instead of = we use the in command as will iterate over entire dict simiarly we use not in (instead of ! in or !=) at bottom
         choice==(vocab[choice])
         selection=(vocab[choice])
         currentQuestion=random.choice(list(selection.items()))
         current2=currentQuestion[0]
         current3=currentQuestion[1]
         answer=input(" what is this word in English "+current2)
         if answer==current3:
             print("\n correct! \n")
         elif answer != current3:
              print (" \n wrong! \n")
    if choice not in vocab.keys():
         return#this function allows user to select a dictionary adn then tests 
#UserTest()                       #whether the user knows the value for the key (can be used
def Test():                      #to test vocabulary with languages
    print (vocab)   
    choice=input(" please select a dictionary category \n")
    selection=(vocab[choice])
    print(selection.keys(), selection.values())
def find(key, dictionary):
    for k in dictionary.items():
        if k == key:
            dictionary.pop[k, None]
def delete(key):
    map(vocab.pop, [key])

def deleteCat():
    choice=input ("please select a dictionary to modify \n")
    if choice in vocab.keys():    #WORKS UP TO THE POINT OF SHOWING KEYS AND VALS WITHIN DICT NEEDS TWEAKING!!!!!
        choice==(vocab[choice])
        print (vocab[choice])
        choice2=input("select an item")
        del vocab[choice][choice2]
        print ("item removed")
      #  if choice2 in choice.keys()
      #  choice==(vocab[choice]) #RELEVANT function this will remove a whole dic (plus keys and values according to user input)
       # choice.pop(choice2, None)
    else:
        return
    

#this will show the user the keys 
#Test()                                          #and values within a dictionary item

