print("==============================")
print("   PYTHON SMART CALCULATOR   ")
print("==============================")

while true:
    print("\n--- main menu ---")
    print("1. add (+)")
    print("2. subtract (-)")
    print("3. multiply (*)")
    print("4. divide (/)")
    print("5. exit")
    choice = input("enter your choice (1-5): ")

if choice == '5':
     print("\nThank you for using Smart Calculator. Goodbye! ")
     break

  if choice in ['1', '2', '3', '4']:
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print(" Invalid input! Please enter numbers only.")
      continue
      
    if choice == '1':
      print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
      print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
      print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
      if num2 == 0:
        print(" Error: Division by zero is not allowed!")
      else:
        print(f"Result: {num1} / {num2} = {num1 / num2}")
  else:
    print(" Invalid Choice! Please choose a valid operation (1-5).")
