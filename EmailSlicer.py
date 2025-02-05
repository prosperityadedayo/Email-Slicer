email = input("Enter your Email: ")
email = email.strip()
slicer_index = email.index("@")
username = email[ :slicer_index]
domain_name = email[slicer_index: ]
print(f"your User name is {username}  and your Domain name is {domain_name}")