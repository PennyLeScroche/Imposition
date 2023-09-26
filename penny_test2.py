import random

class Roll:
    pool = []
    opposition = []
    pool_results = []
    opposition_results = []
    result = ""
    def __init__(self,pool_dice,opposition_dice):
        self.pool = []
        self.opposition = []
        self.pool_results = []
        self.opposition_results = []
        self.result = ""
        for x in pool_dice:
            a = random.randint(1,int(x))
            self.pool.append(a)       
            self.pool_results.append(a)     
        for x in opposition_dice:
            a = random.randint(1,int(x))
            self.opposition.append(a)            
            self.opposition_results.append(a)
        self.pool.sort()
        self.opposition.sort()
        self.pool_results.sort()
        self.opposition_results.sort()
        #print("Pool:",self.pool)
        #print("Opposition:",self.opposition)
        if self.pool[-1] - self.opposition[-1] >= 5:
            self.result = "success+"
        elif self.pool[-1] - self.opposition[-1]>0:
            self.result = "success"
        elif self.pool[-1] - self.opposition[-1]==0:
            self.result = "success-"
        else:
            self.result = "failure"
        #print("Starting Pool:",self.pool_results)
        #print("Starting Opposition:",self.opposition_results)
        #print("Final Pool:",self.pool)
        #print("Final Opposition:",self.opposition)
loop = True
while(loop):
    pool = []
    opposition = []
    num_rolls = 0
    result = ""
    pool_input = ""
    opposition_input = "" 
    num_input = ""
    rolls = []
    pool_loop = True
    while(pool_loop):
        print("Input the positive die pool(4-12), separated by commas (ex, 4,4,6,8):")
        pool_input = input()
        pool_input = pool_input.replace("\s","")
        pool_input = pool_input.split(",")
        print(pool_input)
        pool_loop = False
        for x in range(len(pool_input)):
            if pool_input[x]!="4" and pool_input[x]!="6" and pool_input[x]!="8" and pool_input[x]!="10" and pool_input[x]!="12":
                print("Invalid input, please try again")
                print(str(pool_input[x]))
                pool_loop=True
                break    
            
        
        
    
    opposition_loop = True
    while(opposition_loop):
        print("Input the opposition die pool(4-12), separated by commas (ex, 4,4,6,8):")
        opposition_input = input()
        opposition_input = opposition_input.replace(" ","")
        opposition_input = opposition_input.split(",")
        print(opposition_input)
        opposition_loop=False
        for x in range(len(opposition_input)):
            if opposition_input[x]!="4" and opposition_input[x]!="6" and opposition_input[x]!="8" and opposition_input[x]!="10" and opposition_input[x]!="12":
                print("Invalid input, please try again")
                print(str(opposition_input[x]))
                opposition_loop=True
                break
        
            
        
    num_loop = True
    while(num_loop):
        print("How many times do you want to roll these pools?")
        num_input = input()
        num_rolls = int(num_input) if num_input.isdecimal() else 0
        if num_rolls > 0:
            num_loop = False
        else:
            print("Invalid input, please try again")
    for x in range(num_rolls):
        #print("New Roll:",pool_input,opposition_input)
        new_roll = Roll(pool_input,opposition_input)
        rolls.append(new_roll)
    print("Dice Pool | Opposition Dice Pool | Pool Results | Opposition Results | Remaining Pool | Final Result")
    Criticals = 0
    Successes = 0
    Failures = 0
    Mixed = 0
    for x in range(len(rolls)):
        if rolls[x].result == "success+":
            Criticals+=1
        elif rolls[x].result == "success":
            Successes+=1
        elif rolls[x].result == "success-":
            Mixed+=1
        else:
            Failures+=1
        print(x+1,"|",pool_input,"|",opposition_input,"|",str(rolls[x].pool_results),"|",str(rolls[x].opposition_results),"|",rolls[x].pool[-1] - rolls[x].opposition[-1],"|",rolls[x].result)
    print("Rolled a pool of",pool_input,"against a pool of",opposition_input,str(num_rolls),"times with",Successes,"successes,",Criticals,"Critical successes,",Mixed,"Mixed Successes, and",Failures,"failures")
    again_loop = True
    while(again_loop):
        print("would you like to run again(y/n)?")
        a = input()
        if a.lower() == "n":
            again_loop = False
            loop = False
        elif a.lower() == "y":
            again_loop = False
        else:
            print("Invalid input, please try again")