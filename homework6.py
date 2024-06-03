my_dict = {'Anton' : 1996, "Nikita" : 1999}
print(my_dict)
print(my_dict.get('Anton'))
my_dict['Anna'] = 2003
print(my_dict.get('Anna'))
my_dict.update({'Maxim' : 1997,
                'Denis' :1988})
print(my_dict)
a = my_dict.pop('Anton')
print(a)
print(my_dict)

my_set = {1, 3, 4, 5, 5, 2, 3, 5, 7, 6, 3, 4}
print(my_set)
my_set.update(['Anton'], (8, 9, 10))
print(my_set.remove(1))
print(my_set)