numbers=list(map(int,input("enter numbers separated by spaces:"),split()))
even_count=0
odd_count=0
for n in numbers:
    if n %2==0:
        even_count+=1
    else:
        odd_count+=1
print("even numbers:",even_count)
print("odd numbers:",odd_count)