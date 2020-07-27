#Daniel Lu
#07/23/2020

#Tells the user which day of the week they will return on given the starting day and length of travel

departure = int(input("Please enter the number of the day that you are leaving(0-Sunday, 1-Monday,...., 6-Saturday): "))
length = int(input("How long will you be away?: "))

return_day = (departure + length) % 7
print("You will return on day",return_day)
