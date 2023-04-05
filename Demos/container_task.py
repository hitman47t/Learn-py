from dataclasses import dataclass
import pprint

@dataclass()
class Item():
    name: str
    weight: int
    cost: int

@dataclass()
class Cell():
    items: list
    sum: int

SPACE = 4
ITEMS = [
    Item('SmartPhone', 1, 1500),
    Item('Laptop', 3, 4000),
    Item('Tablet', 2, 2000),
    Item('HearPhone', 1, 1000)
]

table = [
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
]

def main():
    for i in range(len(ITEMS)):
        print('i=', i, ITEMS[i])
        for j in range(SPACE+1):
            print('  j=', j)
            if i == -1:
                table[i][j] = [0]
            else:
                ost = j - ITEMS[i].weight
                if ost > 0:
                    cur_value = ITEMS[i].cost + sum(table[i - 1][ost])
                else:
                    if ost == 0:
                        cur_value = ITEMS[i].cost
                    else:
                        cur_value = 0

                prev_value = sum(table[i - 1][j])

                best_value = max(cur_value, prev_value)

                table[i][j] = [best_value]

                print(f'    ost={ost}, prev_value= {prev_value}, ITEMS[{i}].cost={ITEMS[i].cost} cur_value={cur_value}, best_value={best_value} {table[i][j]}')



    pp = pprint.PrettyPrinter(width=50)
    pp.pprint(table)

if __name__ == "__main__":
    main()
