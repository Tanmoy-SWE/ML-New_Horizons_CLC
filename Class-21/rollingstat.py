import matplotlib.pyplot as plt

time = [1,2,3,4,5,6,7,8,9,10]
temp = [15, 20, 21, 23, 20, 24, 16, 11, 7, 13]

def moving_avg(temp, window_size):
    avg = []
    for i in range(0, len(temp)-window_size+1):
        sum = 0
        for j in range(i, i+window_size):
            sum += temp[j]
        avg.append(sum/window_size)
    return avg

rolling_stat = moving_avg(temp,2) #first flattening
rolling_stat = moving_avg(rolling_stat,2) #second flattening
rolling_stat = moving_avg(rolling_stat,2) #third flattening

plt.plot(time,temp,rolling_stat,color='cyan')
plt.show()
