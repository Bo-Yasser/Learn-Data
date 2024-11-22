morethanonedict={
    "dict_one" : { 
        "age" : 35,
        "name" : "Osama",
        "list" : ["CR7", True,"best"]
    },
    "dict_two" : {
        "age" : 21,
        "name" : "Mohamed",
        "set" :{1,"messi",False}
    },
    "dict_three" :{
        "age" : 22,
        "name" : "ahmed",
        "tuple" : ("imbabi" ,True ,"madrid")
    }
}
#print(morethanonedict)
print(morethanonedict["dict_one"]["age"])
print(morethanonedict.get("dict_one")["age"])


dict_1={
    "age" : 35,
    "name" : "Osama",
    "list" : ["CR7", True, "best"]
}

dict_2={
    "age" : 21,
    "name" : "Mohamed",
    "set" : {1,"messi" ,False}
}

dict_3={
    "age" : 22,
    "name" : "ahmed",
    "tuple" : ("imbabi" ,True ,"madrid" )
}

alldicts={
    "dict_one" : dict_1,
    "dict_two" : dict_2,
    "dict_three" : dict_3
}

#print(alldicts)
print(alldicts["dict_one"]["age"])
print(alldicts.get("dict_one")["age"])


print(len(alldicts["dict_one"]))


print(alldicts["dict_one"].keys())
print(alldicts["dict_two"].values())
print(alldicts["dict_three"]["tuple"][0])
print(alldicts["dict_one"]["list"][0])




print("="* 50)
print("="* 50)
print("="* 50)





user={
    "name" : "osama"
}
print(user)
user.clear()
print(user)

print("="* 50)

member={
    "name" :"osama"
}
print(member)
member["age"]= [1,2,3]
print(member)
member.update({"country" : "egypt", "name2" : "mazen"})
print(member)

print("="*50)

main={
    "name" : "osama"
}
b=main.copy()
print(b)

main.update({"skills" : "fighting"})
print(main)
print(b)

print(main.keys())
print(main.values())




print("="*50)
print("="*50)
print("="*50)



cv= {
    "name" : "osama"
}
print(cv)
print(cv.setdefault("name" , "oz"))
print(cv)
cv.setdefault("age", 36)
print(cv)

print("="*50)


genral={
    "name" : "mohamed",
    "skill" : "fighting"
}

genral.update({"country" : "sumal"})
print(genral)

print(genral.popitem())

print("=" * 50)


view= {
    "name" : "osama",
    "skill" : "fighting"
}

allitems = view.items()
print(view)
view["age"]=36
print(allitems)


print("="* 50)

a = ["keyone","keytwo","keythree"]
b = "x" 

print(dict.fromkeys(a, b))



