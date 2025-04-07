# 1 запись: 69485 Jack
# 2 запись: 95715 qwerty
# 3 запись: 95715 Alex
# 4 запись: 83647 M
# 5 запись: 197128 qwerty
# 6 запись: 95715 Jack
# 7 запись: 93289 Alex
# 8 запись: 95715 Alex
# 9 запись: 95715 M

def get_gen(obj1, obj2):
    return ((obj1[i_n], obj2[i_n]) for i_n in range(min(len(obj1), len(obj2))))


my_str = ['a', 'b', 'c', 'd']
my_tuple = (10, 20, 30, 40)
my_generator = get_gen(my_str, my_tuple)

print(my_generator)

for i_item in my_generator:
    print(i_item)


