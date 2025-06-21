#some notes on how the function join works in py3.12

words = ["hello", "world", "LOUD"]
nums = ['1','2','3']
chars = ['a','b','c']

print("{}".join(words))
print("\n".join(nums))
print(''.join(chars))

#"\n".join() was not allowed in Python 3.11 and earlier
# rule for {} brakes: even number of {} + extra {} for computing expression inside so a pair of {} to show {}

num = 10
print(f'{{{{{num}}}}}')     # prints {{10}}
print(f'{{{{num}}}}')       # prints {{num}}

print("{:,.2f}".format(12345.12345))    # prints 12,345.12
print(f"{1234:0>12}")                   # prints 000000001234
print("|%-56d|" % 123)
print("|%056d|" % 123)
print("|%56d|" % 123)

name = "James"
surn = "Bond"
print(f"My name is {surn}, {name.upper()} {surn.upper()}")
print('My name is {surn} {name}'.format(name = 'J', surn = 'B')) # local vars are overwritten in the func
print('My name is {1}, {0} {1}'.format(name, surn))         # OK
print('My name is {surn} {name}'.format(surn, name))        # KeyError
print(name, surn)
