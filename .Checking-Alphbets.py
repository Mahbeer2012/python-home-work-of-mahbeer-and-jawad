print("enter a chracter", end="")
c = input() 
if len (c)>1:
    print("/ninvalid input!")
else:
    if c>='a' and c<='z':
        print("/n/"" +c+ "/" is an alphbet.")
    elif c>='A' and c<='Z':
        print("/n/"" +c+ "/" is an alphbet.")
    else:
          print("/n/"" +c+ "/" is not an alphbet!")
          