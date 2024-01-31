
def jokefunc():
    color = input("what is your favorite color")
    pname = input("what is favorite pet name")
    print("you have your favorite dog is " + (color) + " and its name is " + (pname))

def dad_joke():
    color = input("what is your favorite color")
    pname = input("what is favorite pet name")
    print("you have your favorite dog is " + (color) + " and its name is " + (pname))


name = input("what is your name ")
print ("choose your joke " + (name))
print ("n1 band name\n2 color joke")

choice = int(input("you choose: "))

if choice <= 1:
    jokefunc()
else:
    dad_joke()
