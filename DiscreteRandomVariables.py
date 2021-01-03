#The probability for having the value 1, 2, 3.... and 6 of one dice for 1000 rolls

runs=1000
x= np.random.randint(1,7, size=runs)
y=np.bincount(x)[1:]
#print(y)
z=y/runs
a=np.array([1,2,3,4,5,6])
#The histogram of the results 
plt.bar(a,z)
plt.show()

#The probability for having the value 1, 2, 3.... and 6 of 2 die for 1000 rolls
runs=1000
x1= np.random.randint(1,7, size=(runs))+np.random.randint(1,7, size=(runs))
#print(x1)
y1=np.bincount(x1)[1:]
print(y1)
z1=y1/runs

a1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#The histogram of the results 
plt.bar(a1,z1)
plt.show()

#The function to calculate the mean and variance of a discrete random variable
m=[]
def mean(x,y):
    global m
    m=x*y
    mean1=sum(m)
    return mean1

#Variance
def variance(x,y):
    n=x*m
    variance1=sum(n)-(mean(x,y)**2)
    return variance1

#For one die
print("One die:")
print("Mean:", mean(a,z))
print("True mean", np.mean(x))
print("Variance",variance(a,z))
print("True Variance",np.var(x))
print('\n')

#For two die
print("Two die:")
print("Mean:", mean(a1,z1))
#print(a1,z1)
print("True mean", np.mean(x1))
print("Variance",variance(a1,z1))
print("True Variance",np.var(x1))
print('\n')

#Calculating the correlation between X and Y
x= np.random.randint(0,50,1000)

y=+x+np.random.normal(0,10,1000)

corr=np.corrcoef(x,y)
print("Correlation:",corr)
#I observe that X and Y has a low positive correlation as the both increase together
#To obtain a negative correlation all the random integers in x must be negative.
plt.scatter(x,y)
plt.show()
