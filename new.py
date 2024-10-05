# Defining thhe function
def simple_interest(p, n, r):
    """
    This function takes following inputs
    p = Principal in INR
    n = Number of years 
    r = Rate of Interest in %p.a.
    Output = Interest and amount
    """

    I = (p * n * r) / 100
    A = p + I
    return I, A


# Take input from the user
p = float(input("Please enter principal in INR : "))
n = float(input("Please enter number of years : "))
r = float(input("Please enter rate of interest in %p.a. : "))

# Call the function 
I, A = simple_interest(p, n, r)

# Print the results
print(f"Simple Interest : {I:.2f} INR")
print(f"Amount : {A:.2f} INR")