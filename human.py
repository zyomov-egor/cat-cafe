from dice import Dice
from house_new import House


class Human():
    def choose_dice(self, dice_list: list[int]):
        while True:
            print(dice_list)
            res = input('Выберите 1 кубик: ')
            dice = Dice.load(res)
            if dice in dice_list:
                dice_list.remove(dice)
                return dice
            else:
                print('Такого кубика нет!')
    def choose_action(self, house: House=None, dices=[int, int]):
        while True:
            while True:
                tower = int(input('выберите номер башни башни: '))
                if not(1 <= tower <= 5):
                    print('Такой башни нет!')
                    continue
                break
            while True:
                floor = int(input('выберите какой кубик отвечает за этаж башни: '))
                if floor not in dices:
                    print('Такого кубика нет!')
                    continue
                break
            item = dices.remove(floor)[0]
            if house._get(tower, dices[0]) == "":
                return tower, floor, item
            else:
                ans = input('Сделайте другой выбор или пропустите ход \nВы хотите пропустить ход? ')
                if ans in ['да', 'Да', 'ДА', 'y', 'Y', 'Yes', 'YEs', 'YES']:
                    return None
                else:
                    continue




