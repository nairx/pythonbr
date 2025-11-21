try:
    # a=6
    print(a-"hello")
except (NameError,TypeError):
    print("Invalid type")
except:
    print("Something went wrong")


# try:
#     # a=6
#     print(a-"hello")
# except NameError:
#     print("invalid value of a")
# except TypeError:
#     print("Invalid type")
# except:
#     print("Something went wrong")
    
    
# try:
#     print(a)
# except:
#     print("Something went wrong")
# else:
#     print("Else block")
# finally:
#     print("Finally block")