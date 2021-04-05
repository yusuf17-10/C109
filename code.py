import csv
import plotly.figure_factory as ff
import statistics 
import pandas as pd

df=pd.read_csv("code.csv")
data=df["Height"].tolist()


mean=sum(data)/len(data)
mode=statistics.mode(data)
median=statistics.median(data)
std=statistics.stdev(data)

print("mean  :"+str(mean))
print("median  :"+str(median))
print("mode  :"+str(mode))
print("std  :"+str(std))

first_std_start,first_std_end=mean-std,mean+std
list_of_data_within_first_std=[]

for i in range(0,len(data)):
    if(data[i]>first_std_start and data[i]<first_std_end):
        list_of_data_within_first_std.append(data[i])
        

percantage_of_data_in_first_std=len(list_of_data_within_first_std)*100.0/len(data)


print(str(percantage_of_data_in_first_std )+"% data_lie first_standard_deviation")

second_std_start,second_std_end=mean-2*std,mean+2*std
list_of_data_within_second_std=[]

for i in range(0,len(data)):
    if(data[i]>second_std_start and data[i]<second_std_end):
        list_of_data_within_second_std.append(data[i])
        

percantage_of_data_in_second_std=len(list_of_data_within_second_std)*100.0/len(data)


print(str(percantage_of_data_in_second_std )+"% data_lie second_standard_deviation")


third_std_start,third_std_end=mean-3*std,mean+3*std
list_of_data_within_third_std=[]

for i in range(0,len(data)):
    if(data[i]>third_std_start and data[i]<third_std_end):
        list_of_data_within_third_std.append(data[i])
        

percantage_of_data_in_third_std=len(list_of_data_within_third_std)*100.0/len(data)


print(str(percantage_of_data_in_third_std )+"% data_lie third_standard_deviation")


fig=ff.create_distplot([data],["Height"],show_hist=False)

fig.show()

