def second_biggest(l1):
    if len(l1)<2:
        return "list must contains atleast two elements"
    largest=float('-inf')
    second_largest=float('-inf')
    for i in l1:
        if i>largest:
            second_largest=largest
            largest=i
        elif i>second_largest and i!=largest:
            second_largest=i
    if second_largest==float('-inf'):
        return "No second_largest element found"
    else:
        return f'second biggest is : {second_largest}'

l1=list(map(int,input("Enter the elements:").split()))
print(second_biggest(l1))
