try:
    lunch()
except SyntaxError:
    print('Fix your syntax')
except TypeError:
    print('Oh no! A TypeError has occured')
except ValueError:
    print('A ValueError occured!')
except ZeroDivisionError:
    print('Did by zero?')
else:
    print('No exception')
finally:
    print('Ok then')
