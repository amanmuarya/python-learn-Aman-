# range() Function
# range() ka use numbers ki sequence generate karne ke liye hota hai.

for i in range(5):
    print(i)


#     range(start, stop, step)
# Third parameter step batata hai ki number kitna increase hoga.

for i in range(1, 10, 2):
    print(i)


#     Reverse counting with range()
# Negative step use karke reverse counting kar sakte hain.

# for i in range(5, 0, -1):
#     print(i)

    # 1 se 10 tak numbers ka square print karna hai

for i in range(1, 11):
    print(i, "=", i*i)