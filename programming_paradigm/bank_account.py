class BankAccount:
	def __init__(self, account_balance=0):
		self.account_balance = account_balance

	
	def deposit(self, amount):
		self.amount = float(input("Enter the amount to be deposited: "))
		self.account_balance += amount

	def withdraw(self, amount):
		self.amount = float(input("Enter the amount to be withdrawn: "))
		if self.account_balance >= amount:
			self.account_balance -= amount
			print(f" You withdrew {amount}")
		else:
			print(" Insufficient balance ")

	def display_balance(self):
		print(f"Available balance : {self.account_balance}")