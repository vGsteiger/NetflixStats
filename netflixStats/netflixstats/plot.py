import matplotlib.pyplot as plt
import matplotlib.dates as mdates

rtime_array = []
date_array = []

current_date = 0
curr_date_index = -1

for ite in range(i - 1):
    if movie_list[ite, 0] == None:
        continue
    if not current_date == movie_list[ite, 0]:
        current_date = movie_list[ite, 0]
        date_array.append(datetime.strptime(movie_list[ite, 0], '%d/%m/%Y').date())
        rtime_array.append(int(movie_list[ite, 2]))
        curr_date_index += 1
    else:
        trun = int(rtime_array[curr_date_index]) + int(movie_list[ite, 2])
        rtime_array[curr_date_index] = trun

plt.plot_date(mdates.date2num(date_array), rtime_array, linestyle='-')

fig.autofmt_xdate()
plt.show()