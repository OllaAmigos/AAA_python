import math
def step2_umbrella():
    print('зонтик оказался дырявым! Сколько лет она хранила его у себя?')
    years = int(input())
    if years < 5:
        tmp_message = 'наверное, ей продали дырявый зонтик😢, придется мокнуть...'
        print(tmp_message.capitalize())
    else:
        print(f'ничего себе, за {years} лет в зонте появилось {math.factorial(years)} дырок!')

def step2_no_umbrella():
    dict = {
            1:'в бар',
            2:'не помню, куда',
            3: 'в бар',
            4: 'не помню, куда'
    }
    print('утка решила вспомнить, куда она ходила последнее время.')
    for key in dict:
        print(f'"Так.. {key}го числа я ходила..{dict[key]}"')
    print('Похоже, утке-маляру🦆 надо бы перестать пить. ')
def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

if __name__ == '__main__':
    step1()

