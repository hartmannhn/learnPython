#=======================================================================
# Documentation
#=======================================================================
#
#       script to simulate the actual chance using pseudo random
#   distribution. the result graph shows the actual chance from using
#   the base chance as base and increment value.
#
#   author : @hartmannhn
#
#=======================================================================

#=======================================================================
# Library Used
#=======================================================================

import matplotlib.pyplot as plt
import numpy as np
import random
import progressbar as pb

#=======================================================================
# Parameter Declaration
#=======================================================================

#if true, use default base chance
#if false, use user input as base chance
useDefaultBaseX = True

#if useDefaultBaseX is true, this is the default base chance
defaultBaseX = 0.5

#number of test performed to each chance
#setting this to high number will causes longer wait time
#higher number produce more accurate result and generally smoother graph
#default value = 10000
maxtest = 10000

#if true, display progress bar
#if false, display nothing
displayPb = True

#if true, smoothes the graph
#if false, display the graph as it is
smoothGraph = True

#=======================================================================
# Function Codes
#=======================================================================

#=======================================================================
#define function for plotting
def prdplot(x,y,marker):
    plt.plot(x,y,marker)
    plt.title("Pseudo Random Distribution")
    plt.xlabel('base chance (%)')
    plt.ylabel('actual chance (%)')
    plt.grid(True)
    plt.axis([0,100,0,100])
    plt.xticks(np.arange(0,105,5))
    plt.yticks(np.arange(0,105,5))
    plt.show()    

#=======================================================================
#define the progress timer class
class progress_timer:
    
    def __init__(self,n_iter,description=""):
        self.n_iter         = n_iter
        self.iter           = 0
        self.description    = description + ': '
        self.timer          = None
        self.initialize()

    def initialize(self):
        widgets    = [self.description, pb.Percentage(),' ',pb.Bar(marker=pb.RotatingMarker()),' ',pb.ETA()]
        self.timer = pb.ProgressBar(widgets=widgets,maxval=self.n_iter).start()

    def update(self,q=1):
        self.timer.update(self.iter)
        self.iter += q

    def finish(self):
        self.timer.finish()

#=======================================================================
#define the pseudo random calculation class
class pseudo_calc:

    def __init__(self,plotx,maxtest,ptimer=None):
        self.plotx          = plotx
        self.ploty          = []
        self.maxtest        = maxtest
        self.index          = 0
        self.chance         = 0
        self.timerExist     = False
        self.initialize(ptimer)

    def initialize(self,ptimer):
        if ptimer != None:
            self.pt         = ptimer
            self.timerExist = True
            
        for i in self.plotx:
            #add the test result to the ploty
            self.ploty.append(self.count(i))
            #update progress bar if timer exist
            if self.timerExist:
                self.pt.update()

    def count(self,i):
        #set temporary placeholder for chance
        tempChance = i
        
        #number of occurence per chance
        k = 0

        #running the test, saving any occurence to 'k'
        j = 1
        for j in range(0,self.maxtest):
            #generate random number to test the chance
            tempRandom = random.randint(1,101)
            if (tempRandom <= tempChance):
                k = k + 1
                tempChance = i
            else:
                tempChance = tempChance + i
        return k/self.maxtest*100

#=======================================================================
#define function for smoothing the graph by filtering the noises
def filternoise(signal,repeat):
    copy_signal = np.copy(signal)
    for j in range(repeat):
        for i in range(3,len(signal)):
            copy_signal[i-1] = (copy_signal[i-2] + copy_signal[i])/2
    return copy_signal

#=======================================================================
# Function Codes
#=======================================================================

#initiate base chance
if useDefaultBaseX:
    baseX = defaultBaseX
else:
    baseX = float(input("Enter interval of chance (in %) : "))

plotx = np.arange(baseX,100.,baseX)

#initiate progress bar
if displayPb:
    pt = progress_timer(description='Calculating... ',n_iter=len(plotx))
else:
    pt = None

#initiate pseudo random calculation
prd = pseudo_calc(plotx=plotx,maxtest=maxtest,ptimer=pt)

#end progress bar
if displayPb:
    pt.finish()

#smoothing the graph using the filternoise function
if smoothGraph:
    plotynew = filternoise(prd.ploty,100)
else:
    plotynew = prd.ploty    

#plotting plotx and ploty
prdplot(x=prd.plotx,y=plotynew,marker='-b')

#=======================================================================
