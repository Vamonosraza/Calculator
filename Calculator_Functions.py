# I was working on this function that would prevent any errors from crashing the Calculator. This works, excepts it also prints out "NONE". I was planning on doing this with the rest of the calculator so it would be unbreakable but did not have time due to other responsibilities outside of JTC. However it was fun and I learned much.
def get_bill():
    try:
        bill = float(input("What was the total bill?:\n $"))
    except ValueError as ERROR:
        print('Invalidinput \n')
        print(ERROR)
        print("\n Please try again")
        return get_bill()
        
