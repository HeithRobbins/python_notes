def greeting(time_of_day, *args, **kwargs):
    print(f"Hi {' '.join(args)}, i hope that you are having a great {time_of_day}")

    if kwargs:
        print('Your tasks for the day are:')
        for key, val in kwargs.items():
            print(f"{key} => {val}")


greeting('Morning',
         'Kristine', 'Hundgens',
         first='Empty diswasher',
         second="take pupper outside",
         third='Math homework')
