# get number of years first
num_years = int(input("How many years do you want to analyze? "))

# need a running total
rain_running_total = 0

# here's the outer loop for years
for year in range(num_years):
    # here's the inner loop for months
    for month in range(12):
        # note that range indexes at 0, so we have to add 1
        subtotal = float(input(f'For Year {year+1} and Month {month+1}, how many inches of rain was there? '))
        # update running total
        rain_running_total += subtotal

# calculate average
average = rain_running_total / (num_years * 12)

# print
print(f'Number of months is: {num_years * 12}')
print(f'Total inches of rainfall is: {rain_running_total:.2f}')
print(f'Average inches per month is: {average:.2f}')
