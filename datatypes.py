#Data types are another way of storing stuff
integer = 6000
#An integer is just a number, no quotation marks needed
string = "Hello"
#A string needs quotation marks, and most of the time it is letters
boolean = False
#A boolean usually goes by "bool," but what boolean means is that it is basically a true or false.
santas_naughty_list = ["andrew", "andrew"]
#A list is, well you know. But a list is a bunch of stuff put together, so if you do this
print(santas_naughty_list)
#Then it will print what is on the list!

#Now, moving on to something else.
integer2 = "231"
#You should probably never do this because this is considered "text"
#So if you wanted to print that you would have to do this
print(str(integer2))
#Now if you try to do this
print(integer2)
#It will not work.
#This is another way to print an integer inside a string
print(int(integer2))
#Weird,right