my_dict={'apple':3,'banana':1,'cherry':2}
asc_dict=dict(sorted(my_dict.items()))
print("Ascending order by key:",asc_dict)
desc_dict=dict(sorted(my_dict.items(),reverse=True))
print("Descending order by key:",desc_dict)
asc_value=dict(sorted(my_dict.items(),key=lambda item:item[1]))
print("Ascending order by key value:",asc_value)
desc_value=dict(sorted(my_dict.items(),key=lambda item:item[1],reverse=True))
print("Descending order by key value:",desc_value)
