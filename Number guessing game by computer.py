import random
def number_game(number):
    list_number = []
    print('selected number :',number)
    unknown = random.randint(0,100)
    list_number.append(unknown)
    n = ''
    print(unknown)
    while n != "correct":
        n = input()
        if n == 'correct':
            print('correct')
            break
        elif n == 'bigger':
            print('bigger')
            r = random.randint(number,list_number[-1])
            if r not in list_number:
                unknown = r
                list_number.append(unknown)
            else:
                unknown = random.randint(number,list_number[-1])
            print(unknown)
        elif n == 'smaller':
            r = random.randint(list_number[-1],number)
            if r not in list_number:
                unknown = r
                list_number.append(unknown)
            else:
                unknown = random.randint(list_number[-1],number)
            print(unknown)

def answer():
    number = int(input())
    number_game(number=number)

answer()