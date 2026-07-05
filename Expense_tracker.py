expenses=[]
def add_expense():
    expense={}
    expense['category']=input("Enter category:")
    num=int(input("Enter the amount:"))
    if(num<=0):
        print("Amount cannot be negative or zero")
    else:
         expense['amount']=num
         expenses.append(expense)
         print("Expense added successfully")

def view_expenses():
    if(len(expenses)==0):
        print("No expenses to show")
    else:
        for index,expense in enumerate(expenses,start=1):
            print(f"{index}. {expense['category']}  ₹{expense['amount']}")
        print("-" * 30)
        view_total_expense()

def view_total_expense():
    total=0
    if(len(expenses)==0):
        print("No expenses to show")
    else:
        for expense in expenses:
            total+=expense['amount']
        print(f'Total Expense: ₹{total}')

def category_wise_expense():
    totals={}
    for expense in expenses:
        item=expense['category']
        price=expense['amount']
        if item in totals:
            totals[item]+=price
        else:
            totals[item]=price
    for category,total in totals.items():
        print(f'{category}: ₹{total}') 

def delete_expense():
    num=int(input("Enter the expense number:"))
    if(len(expenses)>=num and num>0):
        expenses.pop(num-1)
        print("Expense successfully deleted")
    else:
        print("Invalid expense number")

def exit_expense():
    print("Thank you for using the Expense Tracker!")



while True:
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expense")
    print("4. View Category-wise Expense")
    print("5. Delete Expense")
    print("6. Exit")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        add_expense()
    elif(choice==2):
        view_expenses()
    elif(choice==3):
        view_total_expense()
    elif(choice==4):
        category_wise_expense()
    elif(choice==5):
        delete_expense()
    elif(choice==6):
        exit_expense()
        break
    else:
        print("Invalid choice")