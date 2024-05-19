import matplotlib.pyplot as plt


#My earnings in a year

months=["Far","Ord","Kho","Tir","Mor","Sha","Mer","Aba","Aza","Day","Bah","Esf"] #x axis

yearnings_1401=[2984,4912,9889,8043,10459,5947,8500,9593,10000,7510,11572,11193] #y axis
yearnings_1402=[10200,10735,11262,7573,17714,11200,14000,11000,11000,11000,13500,16500] #y axis


plt.title("My earnings in a year")

plt.bar(months,yearnings_1402)
plt.bar(months,yearnings_1401)


plt.show()