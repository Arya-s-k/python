country_code = {
    "india": "0091",
    "usa" : "001",
    "australia": "0061",
    "nepal":"0097"
}

print("the country code for india")
print(country_code.get("india","not found"))

print("the country code for usa ")
print(country_code.get("usa","not found"))