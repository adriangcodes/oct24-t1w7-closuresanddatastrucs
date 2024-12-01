# List - array -  ordered (indexed) collection of items - mutable, can have duplicates

# Dictionary (dict) - collection of items - mutable - unordered - not indexed
# keyed - key/value pairs - keys cannot have duplicates

person1 = {
    "name": "Matt",
    "surname": "Flynn",
    "age": 52
}

print(person1)
print(type(person1))

print(person1["age"]) # presents error if key not found
print(person1.get("name")) # presents none if key not found

print(person1.get("foo", "Key not found")) # second value provides default response

# if key already exists, replace - if key does not exist, creates key and adds new value
person1["address"] = {"state": "QLD", "postcode": 4000, "city": "Brisbane"} 
print(person1)

print(person1["address"]["postcode"]) #calling dictionary within dictionary

person1.pop("age") # deletes key
print(person1)

person1.update({"age": 18}) # either updates or adds key/value pair
print(person1)

# Loop

for key in person1:
    print(f'Key: {key}')
    print(f'Value: {person1[key]}')
    
for key, val in person1.items():
    print(f'Key: {key}')
    print(f'Value: {val}')