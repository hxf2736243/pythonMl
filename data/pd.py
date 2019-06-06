import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'name':['john','mary','peter','jeff','bill','lisa','jose'],
    'age':[23,78,22,19,45,33,20],
    'gender':['M','F','M','M','M','F','M'],
    'state':['california','dc','california','dc','california','texas','texas'],
    'num_children':[2,0,0,3,2,1,4],
    'num_pets':[5,1,0,5,2,2,3]
})

# a simple line plot
df.groupby(['state','gender']).size().unstack().plot(kind='bar',stacked=True)
# show
plt.show()
# save
plt.savefig('output.png')
