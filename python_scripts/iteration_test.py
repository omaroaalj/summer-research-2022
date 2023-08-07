# scratch work to test iterations and creating intervals (10,000 rows at a time)
import sys
interval = 1
for i in range(100):
    interval = interval + 1
    print(i)
    if interval >= 11:
        # print(interval)
        user_input = input('continue? [y/n]: ')
        while user_input not in ['y','n']:
            user_input = input('continue? [y/n]: ')
        if user_input == 'y':
            interval = 1
        elif user_input == 'n':
            break

print('loop ended')
sys.exit(0)
