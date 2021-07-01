
# Import required libraries
from matplotlib import colorbar
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import random
import streamlit as st


st.markdown('''

# A Simple Pareto Analysis Simulator



**Random Text**
- Built by Arden & GEM CSU
- Contact: a.laldin@nhs.net, g.hutston@nhs.net

***

***
***


# A Simple Pareto Analysis Simulator

***
***



''')

# Pareto Analysis Simulation 


st.subheader('Step 1. Data Creation')

st.write('''
Create a dataset with pesudo-random numbers   using the sliders below        
 
 
 Note that the highest value in the generated list of numbers is highighted          
''')


# Number to base simulations off
#number_to_create = st.sidebar.selectbox("Choose Number of Trusts",[8,9,10,11,12,13,14,15])

number_to_create = st.slider("Choose Number of Trusts", 8, 15, 1)
# Code for input user defined variable

# Build data frame
wait_list = list(random.sample(range(0, 120), number_to_create))

df = pd.DataFrame({"PatientsWaiting": wait_list})

# Create Trust Names
trust ="Trust "
df.index = [trust + str(i) for i in range(0, number_to_create)]

st.table(df.style.highlight_max(axis=0,color="dodgerblue"))


# Sort Values in Desecnding order
df2 = df.sort_values(by='PatientsWaiting', ascending=False)


st.subheader('Step 2. Arranging Data')


st.markdown('''
 After generating our dataset we arrange it in descending order 
 
 You can see the highlighted value changing positions
 ''')


st.table(df2.style.highlight_max(axis=0,color="dodgerblue"))




# Add cumulative percentage column
df3 = df2
df3["cumulative_sum"] = df3["PatientsWaiting"].cumsum()

# Add cumulative percentage column
df3["cum_percentage"] = round(df3["PatientsWaiting"].cumsum()/df3["PatientsWaiting"].sum()*100,2)


st.subheader('Step 3 & 4. Calculations')


st.markdown('''
 Then we calculate Cumulative Sums(totals) and Cumulative Proportions''')


st.table(df3.style.highlight_max(axis=0,color="dodgerblue"))





# Set figure and axis
fig, ax = plt.subplots(figsize=((number_to_create+3),8))

# Plot bars (i.e. frequencies)
ax.bar(df3.index, df3["PatientsWaiting"])
ax.set_title("Pareto Chart")
ax.set_xlabel("NHS Trusts")
ax.set_ylabel("Frequency");

# Second y axis (i.e. cumulative percentage)
ax2 = ax.twinx()
ax2.plot(df3.index, df3["cum_percentage"], color="orange", marker="D", ms=7)
ax2.axhline(80, color="r", linestyle="dashed")
ax2.yaxis.set_major_formatter(PercentFormatter())
ax2.set_ylabel("Cumulative Percentage");

st.subheader('Step 5. Plotting')

st.markdown('''
 - Trusts are ordered by frequency (greatest to least) move left to right
 - First y-axis (left) displays frequency (raw counts) 
 - Second y-axis (right) displays cumulative proportion
 - Red horizontal line provides reference for 80% threshold
 
 Rerun the simulator a few times, it is not uncommon for deviations from the 80/20 rule to occur''')



st.pyplot(fig)

