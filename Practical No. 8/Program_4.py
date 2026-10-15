#4.	Create a function simple_interest(p, r, t) to calculate simple interest.
def simple_interest(p, r, t):
    interest = (p * r * t) / 100
    return interest
p=float(input("Enter the principal amount: "))
r=float(input("Enter the rate of interest: "))
t=float(input("Enter the time in years: "))
interest = simple_interest(p, r, t)
print(f"The simple interest is: {interest}")