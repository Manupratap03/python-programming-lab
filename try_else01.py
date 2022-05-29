try:
    x = 1
except:
    print('Failed to set x')
else:
    print('No exception occured')
finally:
    print('We always do this')
