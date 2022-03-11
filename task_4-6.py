class ValueTypeError(Exception):
    def __init__(self, text):
        self.text = text


class Warehouse:

    def __init__(self, name_warehouse=''):
        self.office_equipment = {'printer': {}, 'scanner': {}, 'xerox': {}}
        self.name_warehouse = name_warehouse

    def __str__(self):
        result_str = f'{self.name_warehouse}\n'
        for k, v in self.office_equipment.items():
            result_str += str(k) + ': {'
            for ki, vi in v.items():
                result_str += str(ki) + ': ' + str(vi) + '; '
            result_str += '} \n'

        return result_str + '\n'

    def take_equipment(self, equipment, count=1):
        try:
            if isinstance(count, int):
                if count < 0:
                    raise ValueTypeError('The number must be positive!')
                else:
                    equip = equipment.get_type_equipment()
                    name_equip = equipment.name_model
                    if equip in self.office_equipment.keys():
                        if name_equip in self.office_equipment[equip].keys():
                            self.office_equipment[equip][name_equip] += count
                        else:
                            self.office_equipment[equip][name_equip] = count

                    else:
                        print('The warehouse does not accept this office equipment!')

            else:
                raise ValueTypeError('The string must be a number!')

        except ValueTypeError as err:
            print(err)

    def give_equipment(self, equipment, count=1):
        try:
            if isinstance(count, int):
                if count < 0:
                    raise ValueTypeError('The number must be positive!')
                else:
                    equip = equipment.get_type_equipment()
                    name_equip = equipment.name_model
                    if equip in self.office_equipment.keys():
                        if name_equip in self.office_equipment[equip].keys():
                            if self.office_equipment[equip][name_equip] > count:
                                self.office_equipment[equip][name_equip] -= count
                            elif self.office_equipment[equip][name_equip] == count:
                                del self.office_equipment[equip][name_equip]
                            else:
                                print('There is not so much office equipment in stock!')

                        else:
                            print(f'Equipment {equip} is not stored in a warehouse!')

                    else:
                        print(f'Equipment {equip} is not stored in a warehouse!')

            else:
                raise ValueTypeError('The string must be a number!')

        except ValueTypeError as err:
            print(err)


class OfficeEquipment:
    formats = ["A2", "A3", "A4", "A5"]

    def __init__(self, name_model='', weight=0.0, price=0.0):
        self.name_model = name_model
        self.weight = weight
        self.price = price


class Printer(OfficeEquipment):
    __type_equipment = 'printer'

    def __init__(self, name_model, weight, price, color=False, max_format='A4'):
        super().__init__(name_model, weight, price)
        self.color = color
        if max_format.upper() in self.formats:
            self.print_format = max_format.upper()
        else:
            print(f'{max_format} is undefined format')

    def print_text(self, text):
        if self.color:
            print(f'The printed text: "{text}" is colored')
        else:
            print(f'The printed text: "{text}" is not colored')

    def get_type_equipment(self):
        return f'{self.__type_equipment}'


class Scanner(OfficeEquipment):
    __type_equipment = 'scanner'

    def __init__(self, name_model, weight, price, color=False, max_format='A4'):
        super().__init__(name_model, weight, price)
        self.color = color
        if max_format.upper() in self.formats:
            self.print_format = max_format.upper()
        else:
            print(f'{max_format} is undefined format')

    def scan_text(self, text):
        if self.color:
            print(f'The scanned text: "{text}" is colored')
        else:
            print(f'The scanned text: "{text}" is not colored')

    def get_type_equipment(self):
        return f'{self.__type_equipment}'


class Xerox(OfficeEquipment):
    __type_equipment = 'xerox'

    def __init__(self, name_model, weight, price, color=False, max_format='A4'):
        super().__init__(name_model, weight, price)
        self.color = color
        if max_format.upper() in self.formats:
            self.print_format = max_format.upper()
        else:
            print(f'{max_format} is undefined format')

    def copy_text(self, text):
        print(f'The text: "{text}" is copied by {self.name_model}')

    def get_type_equipment(self):
        return f'{self.__type_equipment}'


sklad = Warehouse('Warehouse 1781')
print_1 = Printer('HP laserjet', 3, 9937, True, 'A4')
print_2 = Printer('brother hl-1110r', 3.5, 13367, True, 'A4')
scaner_1 = Scanner('HP OfficeJet Pro 9010', 2, 17059, True, 'A4')
xerox_1 = Xerox('Epson LW400 Label Works', 2, 13500, False, 'A4')
xerox_2 = Xerox('Wanhao GR1', 3, 40000, False, 'A4')
xerox_3 = Xerox('Pantum P2207', 2.9, 13867, True, 'A4')

sklad.take_equipment(print_1)
sklad.take_equipment(print_2, 5)
sklad.take_equipment(scaner_1, 4)
sklad.take_equipment(xerox_1, 5)
sklad.take_equipment(xerox_3, 8)
print(sklad)

sklad.give_equipment(xerox_3, 4)
sklad.give_equipment(print_2, 4)
print(sklad)
sklad.give_equipment(print_2, 1)
print(sklad)
