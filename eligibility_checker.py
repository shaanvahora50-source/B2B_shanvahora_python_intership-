age = int(input("enter your age: "))
has_id = input("Do you have a valid id? (yes/no): ").lower()

if age > 18 and  has_id == "yes":
 print("eligible")

else:
 print("not aligible")