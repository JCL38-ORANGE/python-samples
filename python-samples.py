import my_package.zip_and_enumerate
from my_package.zip_and_enumerate import print_rank as pr
from my_package.int import on_int
from my_package.str import on_str
from my_package.file import on_file
from my_package.error import on_error
from my_package.list import on_list
from my_package.set import on_set
from my_package.dict import on_dict

print('calling \'print_rank()\' function in order to demonstrate zip \
and enumerate functions\n')
pr()

print('calling \'on_int()\' function in order to demonstrate int type \n')
on_int()

print('calling \'on_str()\' function in order to demonstrate str type \n')
on_str()

print('calling \'on_list()\' function in order to demonstrate list type \n')
on_list()

print('calling \'on_set()\' function in order to demonstrate set type \n')
on_set()

print('calling \'on_dict()\' function in order to demonstrate dict type \n')
on_dict()

print('calling \'on_file()\' function in order to demonstrate file handling \n')
on_file()

print('calling \'on_error()\' function in order to demonstrate error handling \n')
on_error()

