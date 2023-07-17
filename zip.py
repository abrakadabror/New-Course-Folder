friends = ['Rolf', 'Bob', 'Jen', 'Anne']
time_since_seen = [3, 7, 15, 11]

combined = list(zip(friends, time_since_seen))
# dodajemy do tupli kolejny element
long_timers_01 = list(zip(friends, time_since_seen, [1, 2, 3, 4, 5]))
long_timers = list(zip(friends, time_since_seen))


print(combined)
# usuwamy z rezultatu nawiasy i apostrofy
result = ' '.join([f"{name}: {time}" for name, time in combined])
print(result)
print(long_timers_01)
