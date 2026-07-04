# it contains basic number theory
# 1.PRIME CHECK
#Given a number N, check whether it's prime or not.
# if N=97
N=int(input("enter a no."))
if N%2==0 or N%3==0 or N%5==0 or N%7==0:
    print(N)
    print("NOT PRIME")
else:
    print(N,"ITS PRIME")

# as this code is partially correct ,but it does not satisfies in all coditions like "121" is not prime but in the above code its shows its prime and in "2 its show not prime but its prime same goes with & too".
# here we use another approch for more accuracy
N = int(input("Enter a no.: "))

if N <= 1:
    print(N, "NOT PRIME")
else:
    is_prime = True
    # Check divisibility from 2 up to the square root of N
    # We only need to check up to √N because if N has a factor
    # larger than √N, it must also have a corresponding smaller
    # factor below √N (factors come in pairs)
    for i in range(2, int(N ** 0.5) + 1):
        # If N is divisible by i, it means N has a factor
        # other than 1 and itself — so it's NOT prime
        if N % i == 0:
            is_prime = False
            break # no need to check further, we found a factor
        # If no factor was found in the loop, N is prime
    if is_prime:
        print(N, "ITS PRIME")
    else:
        print(N, "NOT PRIME")