#personala Information Tuple
personal_info = (
                "faheem",
                "17",
                "karachi",
                "software developent",
                "pakistan")


#first item
print("First item:",personal_info[0])

#last item
print("last item:",personal_info[-1]) 

#Total item
print("Total item:",len(personal_info))

#Complete tuple using for loop
print("complete tuple:")

for item in personal_info:
    print(item)