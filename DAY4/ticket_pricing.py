age = int(input("enter age: "))

if age < 12:
  print("Ticket category: child")
  print("Price: Rs 100")
elif age < 60:
  print("Ticket category: adult")
  print("Price: Rs 250")
else:
  print("Ticket category: senior")
  print("Price: Rs 150")