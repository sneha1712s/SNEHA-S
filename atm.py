account = {
    'balance': 1000,
    'transactions': []
}

def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds!")
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: ${amount}")
        print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

def deposit(account, amount):
    account['balance'] += amount
    account['transactions'].append(f"Deposit: ${amount}")
    return f"Deposit successful. Remaining balance: ${account['balance']}"

def get_balance(account):
    return account['balance']

def get_transaction_history(account):
    return account['transactions']

# Example usage:
print("Balance:", get_balance(account))
#deposit(account, 500)
withdraw(account, 200)
withdraw(account, 1000)
print("Balance:", get_balance(account))
print("Transaction History:", get_transaction_history(account))

test_dict = {"fname": deposit, "age" : 50, "address" : "salem"}

res = test_dict['fname'](account, 500)
 
# printing result 
print("The required call result : " + str(res))