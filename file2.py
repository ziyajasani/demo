import json

# a simple json array
MYJSON = """
{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
"""

# load it into a var
myjson = json.loads(MYJSON)

fname = myjson['firstName']
print(fname)
