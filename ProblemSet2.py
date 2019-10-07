# -*- coding: utf-8 -*-

n = 12

while n > 0:
    balance = balance - monthlyPaymentRate*balance
    balance = balance + (annualInterestRate/12)*balance
    n -= 1

print(round(balance,2))

-------------------------------------------------------------------------------

min_month_amount = 0
x = balance

while x > 0:
    n = 12
    x = balance
    min_month_amount += 10
    while n > 0:
        x = x - min_month_amount
        x = x + (annualInterestRate/12)*x
        n -= 1
        
print(min_month_amount)

-------------------------------------------------------------------------------

epsilon = 100

x = 0
low = balance/12
high = (balance*(1 + (annualInterestRate/12))**12)/12
monthly_amount = (high + low)/2
index = 0

while abs(x - balance) > epsilon:
    index += 1
    monthly_amount = (high + low)/2
    n = 12
    x = balance
    while n > 0:
        x = x - monthly_amount
        if x > 0:
            x = x + (annualInterestRate/12)*x
        n -= 1
    if x > 0:
        low = monthly_amount
    elif x < 0:
        high = monthly_amount
    if index == 50:
        break
print(round(monthly_amount,2))   
        

        