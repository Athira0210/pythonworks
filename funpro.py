from functools import reduce
lst=[1,2,3,4,6]

# squares=list(map(lambda n:n**2,lst))
# print(squares)

#map <5 num-5 > 5 num+1

num_out=list(map(lambda n:n-1 if n<5 else n+1,lst))
print(num_out)

evens=list(filter(lambda n:n%2==0,lst))
print(evens)

gt_ten=list(filter(lambda n:n>2,lst))
print(gt_ten)

sum=reduce(lambda n1,n2:n1+n2,lst)
print(sum)

maximum=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
print(maximum)

minimum=reduce(lambda n1,n2:n1 if n1<n2 else n2,lst)
print(minimum)

product=reduce(lambda n1,n2:n1*n2,lst)
print(product)

