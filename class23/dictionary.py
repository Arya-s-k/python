student = {"id1":{
"name": "sam",
"grade": "class 6",
"subject": ["sst","maths","science"]
},
"id2":{
"name": "johny",
"grade": "class 10",
"subject": ["english","maths","social science"]
},
"id3":{
"name": "Jackie",
"grade": "class 6",
"subject": ["english","P.E","science"]
},
"id1":{
"name": "sam",
"grade": "class 6",
"subject": ["sst","maths","science"]

}}

result = {}

for key,value in student.items():
    if value not in result.values():
        result[key] = value
        
print("the dict without duplicates ",result)