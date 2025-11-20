def add(*args,**kwargs):
    print(sum(args))
    print(sum(kwargs.values()))
    
add(9,2,1,a=4,b=5,c=1,d=3)

# def add(**kwargs):
#     print(sum(kwargs.values()))
    
# add(a=4,b=5,c=1,d=3)

# def add(*args):
#     print(sum(args))
    
# add(4,5,1,3)