import random

for el in range(100):
    extents = random.choice(['jpg', 'txt', 'mp3', 'png'])
    name = str(random.random())[2:]

    file = f'{name}.{extents}'

    with open('trash/' + file, 'w') as fh:
        fh.write('')