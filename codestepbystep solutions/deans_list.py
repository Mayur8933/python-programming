def deans_list(grades):
    empty_dict = {}
    store = set()
    for key,value in grades.items():
        if value >= 3.5:
            empty_dict[key] = value
    print(empty_dict)
    for key in empty_dict.keys():
        store.add(key)
    print(store)


deans_list({"Hermione": 4, "Harry": 3.4, "Ron": 3.4, "Ginny": 3.8, "Draco": 3.7})
