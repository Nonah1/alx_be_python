class BankAccount:
	def __init__(self, account_balance=0):
		self.account_balance = account_balance

	
	def deposit(self, amount):
		self.amount = float(input("Enter the amount to be deposited: "))
		self.account_balance += amount

	def withdraw(self, amount):
		self.amount = float(input("Enter the amount to be withdrawn: "))

		if amount > self.account_balance :
			return False
		else:
			self.account_balance -= amount
			return True
		
	def display_balance(self):
		print(f"Available balance : {self.account_balance}")