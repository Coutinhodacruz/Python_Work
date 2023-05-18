weather = input('how is the weather? ')

if weather == 'rain':
    print('🌧️')
else:
    print('😎')


def sum(a, b):
    return a + b


sum2 = lambda a, b: a + b
print(sum2(5, 10))

greet = lambda greet, name: f"{greet}, {name}"
print(greet('aloha', 'joha'))
