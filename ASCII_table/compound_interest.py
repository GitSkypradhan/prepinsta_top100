principal_amount = int(input('Enter the Principal Amount: '))
rate_interest = float(input('Enter the Rate of Interest: '))
years = float (input('Enter the years: '))

def compound_interest(p,r,t):
    interest = p * ((1 + r/100)**t)
    return interest

total_due = compound_interest(principal_amount,rate_interest,years)
print("Interest Amount is: ",total_due)