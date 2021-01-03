#HeadsorTails

Printing 10 random variables where 1 respresents heads and 0 represents tails. 

for y in range(10):
    x= random.choice([0,1])
    print ("Value",y, ":",x)
        
        
For 1000 tosses, Calculating and plotting the relative frequency of the number of heads and adding a red line at the 0.5 level
    
numberoftoss=1000
sum1=0
proba=[]
for i in range (numberoftoss):
    x= random.choice([0,1])
    sum1=sum1+x
    f=sum1/(i+1)
    proba.append(f)
        
plt.plot(proba)

plt.plot(np.arange(numberoftoss)+1,.5*np.ones_like(proba),color='red')
plt.show()
 
For 10000 tosses, Calculating and plotting the relative frequency of the number of heads and adding a red line at the 0.5 level

numberoftoss=10000
sum1=0
proba=[]
for i in range (numberoftoss):
    x= random.choice([0,1])
    sum1=sum1+x
    f=sum1/(i+1)
    proba.append(f)
        
plt.plot(proba)

plt.plot(np.arange(numberoftoss)+1,.5*np.ones_like(proba),color='red')
plt.show()
