
# SECTION 2, TASK 1
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# SECTION 2, TASK 2

add_ons = "audio system" if attendees < 100 else "projector"
print(add_ons)


# SECTION 2, TASK 3 (in shorthand per assignement)

food = input("Would you like vegetarian food? (yes/no): ")
if food == "yes": print("Veggie Delight Caterers") 
else: print("Gourmet Meals Caterers")