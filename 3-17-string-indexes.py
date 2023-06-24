# String Indexes

selfish = '01234567'
        # '01234567'

# [start:stop:stepover]
print(selfish[0:8:2]) # 0246
print(selfish[1:]) # 1234567
print(selfish[:5]) # 01234
print(selfish[::1]) # 01234567
print(selfish[-1]) # 7
print(selfish[::-1]) # 76543210
print(selfish[::-2]) # 7531
