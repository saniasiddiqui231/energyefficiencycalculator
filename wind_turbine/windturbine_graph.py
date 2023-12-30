from matplotlib import pyplot as mt

x= [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y= [22,85,110,350,600,900,1274,1533,1863,1960,1990,1998,2000,2000,2000,2000,2000,2000]

# defining the x and y coordinates

mt.xlabel("Wind Speed m/s")
mt.ylabel("Power kW")
mt.xticks(list(range(3, 21)))
mt.yticks(list(range(500, 2600, 500)))
mt.plot(x, y)
mt.show()