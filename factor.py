'FACTORS'
#Print all factors of a given number.

N=int(input("Enter a No."))
for i in range(1,N+1):
    if N%i==0:
        print(i)

#Prime Factorization
#Find the prime factorization of a number (e.g., 60 = 2² × 3 × 5).
N = int(input("Enter a number: "))

factor = 2  # start checking from the smallest prime

while factor <= N:
    if N % factor == 0:
        print(factor)      # this is a prime factor
        N = N // factor    # divide N by this factor, update N
    else:
        factor += 1         # move to next number to try