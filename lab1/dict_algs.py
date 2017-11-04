Ivan ={
    "name": "ivan",
    "age": 34,
    "children":
        [{ "name": "vasja", "age": 17, },
         { "name": "petja", "age": 10, }],
}
darja = {
    "name": "darja",
    "age": 41,
    "children": [{ "name": "kirill", "age": 21, },
                 { "name": "pavel", "age": 15,}]
}
emps = [Ivan, darja]
for i in emps:
    for j in range(len(i["children"])):
        if ('age' not in i['children'][j]):
            continue
        if i["children"][j]["age"] > 18:
            print(i["name"])