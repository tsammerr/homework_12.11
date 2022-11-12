import random

size1 = int(input('Size 1 -> '))
begin1 = int(input('Begin 1 -> '))
end1 = int(input('End 1 -> '))

list1 = list()

for i in range(size1):
    list1.append(random.randint(begin1, end1))

for i in range(0, len(list1)):
    print(f'{list1[i]}[{i}]', end=' ')
print()

size2 = int(input('Size 2 -> '))
begin2 = int(input('Begin 2 -> '))
end2 = int(input('End 2 -> '))

list2 = list()

for i in range(size2):
    list2.append(random.randint(begin2, end2))

for i in range(0, len(list2)):
    print(f'{list2[i]}[{i}]', end=' ')
print()

mer = list1 + list2
print(f'Merged list: {mer}')

non_d = list(dict.fromkeys(mer))
print(f'List whithout duplicates = {non_d}')

dupes = [x for n, x in enumerate(mer) if x in mer[:n]]
print (f'Duplicates = {dupes}')

print(f'Mininmun : {(min(mer))}')
print(f'Maximum : {(max(mer))}')

def non_duplicates(mer):
    mp = {}
    for i in mer:
        mp[i] = mp[i] + 1 if i in mp else 1
    return {i for i in mp.keys() if mp[i] == 1}

print (f'Non duplicates = {non_duplicates(mer)}')