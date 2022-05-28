# (Dict_name.update())      used for updating new key(s) and value(s) in a dictionary by a second dictionary
myDict = {
    "Fast": "In a Quick Manner",
    "Manu": "A Student",
    "Marks": [1, 2, 3],
    "AnotherDict": {"Name": "Manu", "section": "J"}
}
updatedict = {
    "Dollar": "Money",
    "Pound": "Money"
    
}
myDict.update(updatedict)
print(myDict)
