import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


characters = ['A', 'B', 'C', 'D', 'E']

datafiles = []


for char in characters:
    newdf = pd.read_csv("HEAT_{}_final.csv".format(char) , skiprows = 5, names= ['date','WD','WS', 'CWS', 'HW', 'T', 'A', 'B', 'C', 'D', 'E', 'Z', 'H', 'TH', 'I', 'K', 'l', 'WBGT', 'M', 'N']).drop(['WD', 'WS', 'HW', 'A', 'B', 'C', 'D', 'E', 'Z', 'H', 'TH', 'I', 'K', 'l', 'M', 'N'], axis = 1) 
    datafiles.append(newdf)

print(datafiles[0])

datafiles[3] = datafiles[3].append({'T' :17.99} , ignore_index=True) #create row with NaN data using the mean of temprature
datafiles[3] = datafiles[3].append({'T' : 17.99} , ignore_index=True) 
datafiles[4] = datafiles[4].append({'T' : 18.35} , ignore_index=True)

datafiles[3]=datafiles[3].interpolate() #interpolation for sensor's 4 data
datafiles[4]=datafiles[4].interpolate() #interpolation sensor's 5 data

pearson_T = []
pearson_WBGT = []
pearson_CWS = []
for i in range(0,4): #calcuate pearson's correlation between all the sensors for the Temprature, WBGT and Crosswind Speed
    for j in range(i+1,5):
        pearson_T.append((datafiles[i]['T']).corr(datafiles[j]['T']))
        pearson_WBGT.append((datafiles[i]['WBGT']).corr(datafiles[j]['WBGT']))
        pearson_CWS.append((datafiles[i]['CWS']).corr(datafiles[j]['CWS']))
# print(pearson_T)
# print(pearson_WBGT)
# print(pearson_CWS)


spearman_T = [] 
spearman_WBGT = []
spearman_CWS = []

for i in range(0,4): #calcuate Spearman's correlation between all the sensors for the Temprature,WBGT and Crosswind Speed
    for j in range(i+1,5):
        temp_df = datafiles[i]
        temp_df1 = datafiles[j]
        spearman_T.append((datafiles[i]['T']).corr(datafiles[j]['T'], method='spearman'))
        spearman_WBGT.append((datafiles[i]['WBGT']).corr(datafiles[j]['WBGT'], method='spearman'))
        spearman_CWS.append((datafiles[i]['CWS']).corr(datafiles[j]['CWS'], method='spearman'))

print(spearman_T)
print(spearman_WBGT)
print(spearman_CWS)



# fig = plt.figure(figsize=(15,6))  #Creation Pearson's correlation plot for Temperature,WBGT and CWS
# ax = fig.add_subplot(1, 3, 1)
# ax.set_ylabel('Correlation',fontsize=14)
# ax.set_xlabel('Sensors\' combination',fontsize=14)
# ax.set_title('Temperature (℃)')
# ax1 = fig.add_subplot(1, 3, 2)
# ax1.set_xlabel('Sensors\' combination',fontsize=14)
# ax1.set_title('Wet Bulb Globe Temperature (℃)')
# ax2 = fig.add_subplot(1,3,3)
# ax2.set_xlabel('Sensors\'s combination',fontsize=14)
# ax2.set_title('Crosswind Speed (m/s)')

# ax.scatter([x for x in range(1,11)], pearson_T, edgecolor='black')
# ax1.scatter([x for x in range(1,11)], pearson_WBGT,edgecolor='black')
# ax2.scatter([x for x in range(1,11)], pearson_CWS,edgecolor='black')
# fig.suptitle('Pearson\'s correlation')


# fig1 = plt.figure(figsize=(15,6)) #Creation Pearson's correlation plot for Temperature,WBGT and CWS
# ax = fig1.add_subplot(1, 3, 1)
# ax.set_ylabel('Correlation',fontsize=14)
# ax.set_xlabel('Sensors\' combination',fontsize=14)
# ax.set_title('Temperature (℃)')
# ax1 = fig1.add_subplot(1, 3, 2)
# ax1.set_xlabel('Sensors\' combination',fontsize=14)
# ax1.set_title('Wet Bulb Globe Temperature (℃)')
# ax2 = fig1.add_subplot(1,3,3)
# ax2.set_xlabel('Sensors\'s combination',fontsize=14)
# ax2.set_title('Crosswind Speed (m/s)')

# ax.scatter([x for x in range(1,11)], spearman_T, edgecolor='black',cmap='greens')
# ax1.scatter([x for x in range(1,11)], spearman_WBGT,edgecolor='black')
# ax2.scatter([x for x in range(1,11)], spearman_CWS,edgecolor='black')
# fig1.suptitle('Sperman\'s correlation')
# fig1.tight_layout()
# plt.show()
















     
    
