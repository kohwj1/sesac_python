def simple_interest(principal, rate, time):
    return principal * rate * time


# print(simple_interest(10000000, 0.03875, 5))
# print(simple_interest(1100000, 0.05, 5/12))

def simple_interest_amount(principal, rate, time):
    return principal + simple_interest(principal, rate, time)

# print(simple_interest_amount(10000000, 0.03875, 5))
# print(simple_interest_amount(1100000, 0.05, 5/12))