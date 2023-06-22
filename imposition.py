import random
class Old_Result():
    spell = 0
    path = 0
    imp = 0
    die_result = 0
    result = ""
    def __init__(self,spell_die,path_die,imposition_die):
        self.spell = random.randint(1,spell_die)
        self.path = random.randint(1,path_die)
        self.imp = random.randint(1,imposition_die)
        if self.imp >= spell and self.imp >= path:
            if(self.spell>self.path):
                self.die_result = self.spell
            elif(self.path>=self.spell):
                self.die_result = self.path
        elif self.imp >= self.spell and self.imp < self.path:
            self.die_result = self.path
        elif self.imp < self.spell and self.imp >= self.path:
            self.die_result = self.spell
        else:
            if self.spell>self.path:
                self.die_result = self.spell
            else:
                self.die_result = self.path
        if self.die_result > 0 and self.die_result < 4:
            self.result = "failure"
        elif self.die_result >= 4 and self.die_result < 7:
            self.result = "partial success"
        else:
            self.result = "success"

class New_Result:
    spell = 0
    path = 0
    imp = 0
    result = "error"
    def __init__(self,spell_die,path_die,imposition_die):
        self.spell = random.randint(1,spell_die)
        self.path = random.randint(1,path_die)
        self.imp = random.randint(1,imposition_die)
        if (self.spell > self.imp) and (self.path > self.imp):
            self.result = "success"
        if (self.spell > self.imp) and (self.path <= self.imp):
            self.result = "partial success"
        if (self.spell <= self.imp) and (self.path > self.imp):
            self.result = "partial success"
        if (self.spell <= self.imp) and (self.path <= self.imp):
            self.result = "fail"

dice = False
spell = False
path = False
imp = False
roll = False
spell_size = 0
path_size = 0
imp_size = 0
rolls = 0
while not(dice):
    print("Would you like to use the old or new imposition dice system?")
    type = input()
    if type.lower() == "old" or type.lower() == "new":
        dice = True
    else:
        print("invalid input, please try again")
while not (spell):
    print("What is the size of the spell die(4,6,8,10,12)?")
    spell_size = input()
    if int(spell_size) == 4 or int(spell_size) == 6 or int(spell_size) == 8 or int(spell_size) == 10 or int(spell_size) == 12:
        spell = True
    else:
        print("Invalid input, plese try again")
while not (path):
    print("What is the size of the path die(4,6,8,10,12)?")
    path_size = input()
    if int(path_size) == 4 or int(path_size) == 6 or int(path_size) == 8 or int(path_size) == 10 or int(path_size) == 12:
        path = True
    else:
        print("Invalid input, plese try again")        
while not (imp):
    print("What is the size of the imposition die(4,6,8,10,12)?")
    imp_size = input()
    if int(imp_size) == 4 or int(imp_size) == 6 or int(imp_size) == 8 or int(imp_size) == 10 or int(imp_size) == 12:
        imp = True
    else:
        print("Invalid input, plese try again")        
while not roll:
    print("How many Rolls would you like to make?")
    rolls = input()
    if int(rolls) > 0:
        roll = True
        rolls = int(rolls)
    else:
        print("Invalid input, please try again")

results = []
output = []

#print("rolled "+str(rolls)+" dice")
#print(results.count())
success = 0
partial = 0
failure = 0
if type.lower()=="old":
    for x in range(rolls):
        result = Old_Result(int(spell_size),int(path_size),int(imp_size))
        results.append(result)  
    output.append(["Spell","Path","Imposition","Die Result","Result"])
    for x in range(len(results)):
        output.append([results[x].spell,results[x].path,results[x].imp,results[x].die_result,results[x].result])
    for x in range(len(output)):
        if output[x][4]=="success":
            success+=1
        elif output[x][4] == "partial success":
            partial+=1
        else:
            failure+=1
        print(output[x])
    print("For "+str(rolls)+" rolls in the old Imposition Dice system with a d"+str(spell_size)+" Spell Die, a d"+str(path_size)+" Path Die, and a d"+str(imp_size)+" Imposition Die the results are:")
    print("Successes: "+str(success)+", Partial Successes: "+str(partial)+", Failures: "+str(failure))
else:
    for x in range(rolls):
        result = New_Result(int(spell_size),int(path_size),int(imp_size))
        results.append(result)
    output.append(["Spell","Path","Imposition","Result"])
    for x in range(len(results)):
        output.append([results[x].spell,results[x].path,results[x].imp,results[x].result])
    for x in range(len(output)):
        if output[x][3]=="success":
            success+=1
        elif output[x][3] == "partial success":
            partial+=1
        else:
            failure+=1
        print(output[x])
    print("For "+str(rolls)+" rolls in the new Impositions Dice system with a d"+str(spell_size)+" Spell Die, a d"+str(path_size)+" Path Die, and a d"+str(imp_size)+" Imposition Die the results are:")
    print("Successes: "+str(success)+", Partial Successes: "+str(partial)+", Failures: "+str(failure))
    
