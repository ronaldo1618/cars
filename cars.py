showroom = {'328i', '240sx', 'GTR', '350z'}
print(len(showroom))
showroom.add('328i')
showroom.update({'mustang GT', 'Geo Metro'})
showroom.discard('mustang GT')
junkyard = {'idk', 'doa', 'thunderbird', '328i', 'Geo Metro'}
already_have = junkyard.intersection(showroom)
showroom.union(junkyard)
showroom.discard({'idk', 'doa'})
print(showroom)