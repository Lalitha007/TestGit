# format string : read variables in to a string i want to print
# Start the string with f for format as f"Hello {somevar}

my_name='Lalitha'
height=50 #Inches

print( f"My name is {my_name}.")
print( f"My height is {height}.")


#  .format() will use this when i want to apply a format to already created string


hilarious = False
joke_valution= "Is this funny:{}"

print(joke_valution.format(hilarious))


w="new..0"
e="life!!"

print(w+e)



y="what"

print(f"I also said {y}")
print(f"I also said '{y}' now")

# string example 1

print("Mary had a little lamb")
e='cheese'
f='burger'
k='cake'
print(e+f , end=' ')
print(k)

print(e+f)
print(k)

#formatting of a string - Complex

formatter = "{} {} {} {}"

print(formatter.format(123,2,3,4))
print(formatter.format( True , False , True, False))
print(formatter.format(formatter , formatter , formatter,formatter))

print("""What is this supposed to mean
          New data? Hmm""")

print('.'*10 , "xxxxxx" , '.'*10)

month="Jan\nFeb\nMar\n"
month2="\nJan\nFeb\nMar"

print(month,month2)


#Escape sequences - ex \n and an important escape sequence is to escape a single quote or double quote
#print("I want a "cheese" burger")
# escape single quotes and double quotes
print("I am '6 1/2\" tall. ")
print("/tI'm tabbed in.")
print("I'm \\ a \\ cat.")


# exercise

print("How old are you?" , end='')
age=input()
print("How tall are you?" , end='')
height=input()
print("How much do u weigh?", end='')
weight=input()

print(f"You are this old {age} and are this tall {height} and weight about {weight} kgs")
