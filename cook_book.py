def cook_book_dict():
    cook_book = {}
    with open("files/cook_book.txt", encoding="utf-8") as text:
        first_str = True
        for string in text:
            if first_str:
                key = string.strip()
                cook_book[key] = []
                first_str = False
            elif string.strip().isdigit():
                continue
            elif string == "\n":
                first_str = True
            else:
                name, quantity, measure = map(strip, string.split("|"))
                ingridient = dict(ingridient_name=name, quantity=int(quantity), measure=measure)
                cook_book[key].append(ingridient)
    return cook_book


def strip(value: str):
    return value.strip()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = cook_book_dict()
    for dish in dishes:
        for ingridient in cook_book[dish]:
            shop_list[ingridient["ingridient_name"]] = dict(measure=ingridient["measure"], quantity=ingridient["quantity"]*person_count)
    return shop_list


print(cook_book_dict())
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
