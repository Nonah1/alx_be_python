def display_menu():
	print ("\n Shopping List Manager ")
	print ("1. Add Item ")
	print ("2. Remove Item")
	print ("3. View List")
	print ("4. Exit")

def main():
	shopping_list = []
	while True:
		display_menu()
		choice = input("Enter your choice. ")

		if choice == "1":
			item = input("Enter the item you want to add: ").strip()
			if item:
				shopping_list.append(item)
				print(f"{item} has been added to your shopping list")
			else: 
				print("Item name cannot be empty.")
		elif choice == "2":
			item = input("Enter the item to remove").strip()
			if item in shopping_list:
				shopping_list.remove(item)
				print(f"{item} has been removed")
			else:
				print(f"{item} is not in your shopping list")
		elif choice == "3":
			if shopping_list:
				print("Your shopping list: ")
				index = 1
				for item in shopping_list:
					print(f"{index}. {item}")
					index += 1
			else:
				print(" Your shopping list is currently empty. ")
		elif choice == "4":
			print("Goodbye!")
			break
		else: 
			print("Invalid choice, please try again.")
if __name__ == "__main__":
	main()
	

