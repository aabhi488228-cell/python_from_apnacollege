# #mydict.keys
student={
    "name":"manik rao",
    "subjects": {
        "phy":69,
        "chem":89,
        "maths":56
    }

}
print(len(student))#total numbers of keys
print(student.keys())

## my dict values
student={
    "name":"manik rao",
    "subjects": {
        "phy":69,
        "chem":89,
        "maths":56
    }

}
print(list(student.values()))

## mydict.items
student={
    "name":"manik rao",
    "subjects": {
        "phy":69,
        "chem":89,
        "maths":56
    }

}
pairs=list(student.items())

print(pairs[0])

## myDict.get(key) method

student={
    "name":"manik rao",
    "subjects": {
        "phy":69,
        "chem":89,
        "maths":56
    }
}
print(student["name"])
print(student.get("name"))
print(student.get("name2"))#none

## myDict.update(newDICT)
student={
    "name":"manik rao",
    "subjects": {
        "phy":69,
        "chem":89,
        "maths":56
    }
}
student.update({"city":"banglore"})
print(student)