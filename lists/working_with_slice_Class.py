tags = [
    'python',
    'development',
    'tutorials',
    'code',
    'programming'
]

# print(tags[2:4:2]) #[start:stop;step]

slice_obj = slice(1,4,2)


##this below is to show how you can found the start,stop,step when you are not calling the slice method
print(slice_obj.start)
print(slice_obj.stop)
print(slice_obj.step)

print(tags[slice_obj])