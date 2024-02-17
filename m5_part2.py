# prompt for number of books first
num_books = int(input('How many books did you purchase? '))
 
# check for increasing amount of books
if num_books <= 1:
    points = 0
elif num_books <= 3:
    points = 5
elif num_books <= 5:
    points = 15
elif num_books <= 7:
    points = 30
else:
    points = 60
 
# display number of points earned
print(f'You earned {points} points!')