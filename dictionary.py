def tagore():
    return"this is the my bank balance"

test_dict={"fname":tagore,"age":20,"address":"ballari"}   # tagore is a function 

print("the original dictionary is :"+str(test_dict))
res=test_dict['fname']() # fname is a key, tagore  it calls the function here it returns value and stores in res.
print("the required call result:"+str(res))