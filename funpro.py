lst=[1,2,3,4,6]

# squares=list(map(lambda n:n**2,lst))
# print(squares)

#map <5 num-5 > 5 num+1

num_out=list(map(lambda n:n-1 if n<5 else n+1,lst))
print(num_out)