def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    if object is None:
        print("Nothing: ", object, obj_type)
    elif object != object:
        print("Cheese: ", object, obj_type)
    elif object == 0:
        print("Zero: ", object, obj_type)
    elif not object:
        print("Empty: ", object, obj_type)
    else:
        print("Type not Found")
        return 1
    return 0
    # print(object)
    # print(obj_type)
