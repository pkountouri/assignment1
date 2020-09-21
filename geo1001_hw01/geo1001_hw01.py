#-- GEO1001.2020--hw01
#-- [Pinelopi-Eirini Kountouri] 
#-- [5386454]

#1.1 Compute mean,variance,standar devision
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.interpolate import UnivariateSpline
from scipy.stats import pearsonr
from scipy.stats import spearmanr



def pmf(sample):    #PMF
    fi = sample.value_counts()
    return fi / len(sample)

def my_dist(x):     #PDF 
    return np.exp(-x ** 2)

characters = ['A', 'B', 'C', 'D', 'E']

datafiles = []

for char in characters:
    newdf = pd.read_csv("HEAT_{}_final.csv".format(char) , skiprows = 5, names=[x for x in range(19)])   
    datafiles.append(newdf)

means = []
var = []
std = []
temp = []
ws = []
wd = []

for df in datafiles:
    means.append(df.mean())
    std.append(df.std()) 
    var.append(df.var())
    temp.append(df.iloc[:,4]) #temprature data
    ws.append(df.iloc[:,1]) #wind speed data
    wd.append(df.iloc[:,0]) #wind direction data

final_mean = pd.concat(means, axis = 1)
final_var = pd.concat(var, axis = 1)
final_std = pd.concat(std, axis = 1)


print(final_mean)
#1.2 Temprature values' histogram
import matplotlib.pyplot as plt

fig1 = plt.figure(figsize=(15,6)) 
fig2 = plt.figure(figsize=(15,6))
fig3 = plt.figure(figsize=(15,6))
fig5 = plt.figure(figsize=(15,6))
fig6 = plt.figure(figsize=(15,6))
fig7 = plt.figure(figsize=(15,6))
fig8 = plt.figure(figsize=(15,6))
fig9 = plt.figure(figsize=(20,6))
fig10 = plt.figure(figsize=(15,6))
fig11 = plt.figure(figsize=(15,6))

fs = 14

for i, t in enumerate(temp): 
    axis = "ax" + str(i) 
    
    axis = fig1.add_subplot(1, 5, i+1) #histogram,temprature, 27 bins (fig1)
    axis.hist(t, bins = 27 , edgecolor = 'black')
    axis.set_ylabel('Frequence',fontsize=fs)
    axis.set_xlabel('Temperature (℃)',fontsize=fs)
    axis.tick_params(labelsize=fs)
    axis.set_title('Histogram for Temprerature')

    axis = fig2.add_subplot(1, 5, i+1) #histogram,temprature, 5 bins (fig2)
    axis.hist(t, bins = 5, edgecolor = 'black')
    axis.set_ylabel('Frequence',fontsize=fs)
    axis.set_xlabel('Temperature (℃)',fontsize=fs)
    axis.tick_params(labelsize=fs)
    axis.set_title('Histogram for Temprerature')

    axis = fig3.add_subplot(1, 5, i+1) #histogram for temprature, 50 bins (fig3)
    axis.hist(t, bins = 50 , edgecolor = 'black') 
    axis.set_ylabel('Frequence',fontsize=fs)
    axis.set_xlabel('Temperature (℃)',fontsize=fs)
    axis.tick_params(labelsize=fs)
    axis.set_title('Histogram for Temprerature')

    axis = fig5.add_subplot(1, 5, i+1)  #box plot,temprature (fig4)
    axis.boxplot(t, showmeans=True)
    axis.set_ylabel('Temperature (℃)',fontsize=fs)
    axis.set_xlabel('Sensor ' + characters[i],fontsize=fs)
    axis.tick_params(labelsize=16)
    axis.set_title('Box plot for Temprerature')
    
    df = pmf(t)   #PMF, temprature (fig7)
    df1 = df.to_frame()
    df1.reset_index(inplace=True)
    df1.columns = ['Temprature', 'PMF']
    df1 = df1.astype(float)
    p = df1.sort_values(by=['Temprature'])
    axis = fig8.add_subplot(1, 5, i+1)
    axis.bar(p['Temprature'], p['PMF'] , width = 0.8)
    axis.set_ylabel('Probability (%)',fontsize=fs)
    axis.set_xlabel('Temperature (℃)')
    axis.set_title('Probability Mass Fuction')
    

    data = t.to_numpy() #CDF, temprature
    data_sorted = np.sort(data)
    p = 1. * np.arange(len(data)) / (len(data) - 1)   # calculate the proportional values of samples
    axis = fig10.add_subplot(1, 5, i+1)
    axis.plot(data_sorted,p)
    axis.set_xlabel('Temperature')
    axis.set_ylabel('CDF')
    axis.set_title('Histogram of CDF')
    
    hist, bins = np.histogram(t, bins=50, normed=True) #PDF, temprature
    bin_centers = (bins[1:]+bins[:-1])*0.5
    axis = fig11.add_subplot(1, 5, i+1)
    axis.plot(bin_centers, hist)
    axis.set_ylabel('Probability (%)',fontsize=fs)
    axis.set_xlabel('Temperature (℃)')
    axis.set_title('Probability Density Fuction')
    
    

    
# 2.2 Kernel & PDF for Wind speed
ax12 = plt.axes()
wind_speed= ws[0]
ax12 = sns.kdeplot(data=wind_speed,label = 'KDE ')
ax12.set(xlabel='wind speed sensor A', ylabel='Probability',label = 'KDE')
    

    
for i, s in enumerate(ws): #box plot wind speed (fig5)
    axis = fig6.add_subplot(1, 5, i+1)  
    axis.boxplot(s, showmeans=True)
    axis.set_ylabel('Wind speed (m/s)',fontsize=fs)
    axis.set_xlabel('Sensor ' + characters[i], fontsize=fs)
    axis.tick_params(labelsize=fs)
    axis.set_title('Box plot for Wind speed')
    
for i,d in enumerate(wd): #box plot wind direction (fig6)
    axis = "ax" + str(i)
    axis = fig7.add_subplot(1, 5, i+1)  
    axis.boxplot(d, showmeans=True)
    axis.set_ylabel('Wind direction (deg)', fontsize=fs)
    axis.set_xlabel('Sensor ' + characters[i],fontsize=fs)
    axis.tick_params(labelsize=fs)
    axis.set_title('Box plot for Wind direction')


fig4 = plt.figure() 
ax4 = plt.axes()

#1.3 frequency polygons in temprature values
for i, t in enumerate(temp):  #frequency polygon
    t = t.to_numpy()
    [frequency,bins]=np.histogram(t, bins=50)
    ax4.plot(bins[:-1],frequency, label = 'Sensor ' + characters[i])
    ax4.set_ylabel('Frequence',fontsize=fs)
    ax4.set_xlabel('Temperature (℃)',fontsize=fs)
    ax4.grid(axis='y', alpha=0.8)
    ax4.set_title('Frequency polygon for Temprerature')
    
   

    
plt.legend()

fig1.tight_layout()
fig2.tight_layout()
fig3.tight_layout()
fig5.tight_layout()
fig6.tight_layout()
fig7.tight_layout()
fig8.tight_layout()
fig9.tight_layout()
fig10.tight_layout()




plt.show()


