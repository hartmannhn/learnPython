#!/usr/bin/env python
# coding: utf-8

# In[201]:


import pandas as pd

filename = 'dataset_superstore_simple.csv'

data = pd.read_csv(filename)
data.head(5), data.count(),data.dtypes


# In[23]:


q1 = data.groupby(['customer_id']).sum()
q1 = q1.sort_values(['sales'],ascending=False)
q1.head(1)


# In[36]:


#q2_cat = list(set(data['category'])) #q2_cat = list(dict.fromkeys(data['category']))

q2 = data.groupby(['category','sub_category'])['profit'].sum()
q2['Office Supplies']


# In[44]:


q3 = data['order_id'][data['profit']<0].count()
q3


# In[95]:


q4 = data.groupby(['customer_id'])['sales'].sum()
customer = ['JE-16165', 'KH-16510', 'AD-10180']

q4=q4[q4.index.isin(customer)].sort_values(ascending=False)
q4,q4.head(1)
#customer_id is index not value after groupby


# In[127]:


data['order_date']=pd.to_datetime(data['order_date'])
yearly_sales = data.groupby(data['order_date'].dt.year).agg({'sales':'sum','customer_id':'count','profit':'sum'}).rename(columns={'sales':'total_sales','customer_id':'customer_count','profit':'total_profit'})

# \ can be used to split long line of command into separate line

q5 = yearly_sales.sort_values(['total_profit'],ascending=False)
yearly_sales,q5.head(1)


# In[176]:


import matplotlib.pyplot as plt

q6 = data.copy()
q6['year']=q6['order_date'].dt.year

plot_year = [2014,2015]
q6 = q6[q6['year'].isin(plot_year)]

colormap = {2014:'red',2015:'green'}

for item in plot_year:
    plt.scatter(q6['sales'][q6['year']==item],                q6['profit'][q6['year']==item],                c=q6['year'][q6['year']==item].map(colormap),
                label=item)
plt.title('Sales vs Profit 2014-2015')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.legend()
plt.show(), q6.head(5)


# In[197]:


q7 = data.copy()
q7['year']=q7['order_date'].dt.year
q7 = q7[q7['year'].isin([2015])]
q7 = q7.groupby(['customer_id']).sum()
q7 = q7.sort_values(['sales'],ascending=False).head(10)

x = list(q7.index)
y = q7['profit']
y_pos = range(len(x))

plt.bar(y_pos,y,align='center')
plt.xticks(y_pos,x,rotation=90)
plt.xlabel('Customer')
plt.ylabel('Total Profit')
plt.title('Total Profit of Top 10 Sales in 2015')
plt.show(),q7

