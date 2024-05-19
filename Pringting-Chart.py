mylist=[
    [23,56,78],
    [10,20,30],
    [5,28,67]
]



mystr1="\n".join(["\t".join([f"{col}" for col in row]) for row in mylist])

mystr2="\n".join(["\t".join([f"{col + (col * 0.1)}" if col > 20 else f"{col}" for col in row]) for row in mylist])

print(mystr1)
print(50*("#"))
print(mystr2)

