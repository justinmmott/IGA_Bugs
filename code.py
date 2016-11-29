import numpy as np
import matplotlib.pyplot as plt
import random
N = 12 #number of genes per bug
M = 12 #number of bugs
a = []
b = []


def generate_initial_population():
    ai = []
    bi = []
    t = np.arange(0,8*np.pi, 0.001)
    x = 0
    y = 0
    for j in range(M):
        for i in range(N):
            ai.append(random.randint(-5,5))
            bi.append(random.randint(-5,5))
        a.append(ai)
        b.append(bi)
        for i in range(N):
            x += ai[i]*np.cos((i+1)*t)
            y += bi[i]*np.sin((i+1)*t)
        print j
        plt.subplot(3,4,j+1)
        plt.plot(x,y)
        plt.axis('off')
        fig = plt.gcf()
        fig.set_size_inches(12,9, forward = True)
        x = 0
        y = 0
        ai = []
        bi = []
    plt.show()
    print a
    print b
    
def user_select():
    c = []
    i = 0
    while i >= 0:
        while True:
            try:
                i = int(raw_input("Which ones look like bugs? (enter -1 to end):  "))
                c.append(i)
            except:
                print "Invalid Input"
                continue
            else:
                print "Valid input"
                break
    c.sort()
    c = c[1:]
    return c
def breed_mutate(c):
    global a
    global b
    #print "PreMutationA: ", a
    #print "PreMutationB: ", b
    if len(c) == 0:
        print "No bugs were selected"
    else:
        new_a = []
        new_b = []
        for i in range(M):
            cross_point = random.randint(0,N)
            mom = c[random.randint(0,len(c)-1)]
            dad = c[random.randint(0,len(c)-1)]
            if(mom == dad):
                dad = c[random.randint(0,len(c)-1)]
                if(mom == dad):
                    dad = c[random.randint(0,len(c)-1)]
            new_a.append(a[mom][0:cross_point] + a[dad][cross_point:N])
            new_b.append(b[dad][0:cross_point] + b[dad][cross_point:N])
            for j in range(2*N):
                mutation = random.randint(0,1000)
                if mutation == 0:
                    print mutation,"Mutation has occurred",j
                    if j < N:
                        #mutate new_a
                        new_a[len(new_a)-1][j] = random.randint(-5,5)
                    else:
                        #mutate new_b
                        new_b[len(new_b)-1][j-N] = random.randint(-5,5)
    a = new_a
    b = new_b
    print "Breeding Complete"


def next_generation():
    global a
    global b
    #print "New PopulationA: ", a 
    #print "New PopulationB: ", b
    t = np.arange(0,8*np.pi, 0.001)
    x = 0
    y = 0
    for j in range(M):
        for i in range(N):
            x += a[j][i]*np.cos((i+1)*t)
            y += b[j][i]*np.sin((i+1)*t)
        print j
        plt.subplot(3,4,j+1)
        plt.plot(x,y)
        plt.axis('off')
        fig = plt.gcf()
        fig.set_size_inches(12,9, forward = True)
        x = 0
        y = 0
    plt.show()


def main():
    answer = ""
    generate_initial_population() #intial population     
    while answer != "no":
        breed_mutate(user_select()) #breed and mutate
        next_generation() #creates a new population
        answer = raw_input("continue yes or no") #User decides when the bugs have converged
        
main()
 


