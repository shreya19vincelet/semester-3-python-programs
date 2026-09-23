def add_entry(d):
    d["city"]="Kanpur"
    return d
def reassign_dict(d):
    d={"name":"Avnish","age":"20"}
    print("reassigned dictonary",d)
my_dict={"name":"Shreya","age":"20"}
print(add_entry(my_dict))
reassign_dict(my_dict)
print(my_dict)