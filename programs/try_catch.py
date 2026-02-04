# try block helps to test block of code for errors
# except block lets you handle the error

# try:
#     f= open("sample.txt", "w")
#     try:
#         f.write("This is a try except block code for opening file")
#     except:
#         print("Something went wrong while writing the file")
#     finally:
#         f.close()

# except:
#     print("Error opening given file!!")

# finally:
#     print("Everying good")

## Raise exceptions

x= -1
if x< 0:
    # raise keyword is used to raise an exception
    raise Exception("Sorry, no number below 0")

# x= 323

# if not type(x) is int:
#     raise TypeError("Only integers are allowed")