p_hp = 40
is_crit = 0

def recover(hp, crit):
    if crit == 1:
        hp += 70
    else:
        hp += 50
    if hp > 100:
        hp = 100
    return hp

new_hp = recover(p_hp, is_crit)
second_hp = recover(p_hp, 1)

print(second_hp) 

print(new_hp)

a = 4

def example():
    global a
    a = a +1
    
example()

print(a)