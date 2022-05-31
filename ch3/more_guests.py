guest_list = ['djonga','ronaldinho','jesus']
print(f"{guest_list[0].title()}, poderia vir ao meu jantar?")
print(f"{guest_list[1].title()}, poderia vir ao meu jantar?")
print(f"{guest_list[2].title()}, poderia vir ao meu jantar?")
print(f"\n{guest_list[1].title()} não poderá vir.")

guest_list.remove('ronaldinho')
guest_list.append('igão')

print(f"\n{guest_list[0].title()}, poderia vir ao meu jantar?")
print(f"{guest_list[1].title()}, poderia vir ao meu jantar?")
print(f"{guest_list[2].title()}, poderia vir ao meu jantar?")

print("\nAchei uma mesa de jantar maior.")
guest_list.insert(0, 'mítico')
guest_list.insert(2, 'gordox')
guest_list.append('faker')

print(f"\n{guest_list[0].title()}, poderia vir ao meu jantar?")
print(f"{guest_list[1].title()}, poderia vir ao meu jantar?")
print(f"{guest_list[2].title()}, poderia vir ao meu jantar?")
print(f"{guest_list[3].title()}, poderia vir ao meu jantar?")
print(f"{guest_list[4].title()}, poderia vir ao meu jantar?")
print(f"{guest_list[5].title()}, poderia vir ao meu jantar?")
