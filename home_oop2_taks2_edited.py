def get_ing_from_line(line):
    line = line.rstrip().split("|")
    cash = {"ingredient_name": line[0], "quantity": line[1], "measure": line[2]}
    return cash


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shopping_list = {}

    for dish in dishes:
        if dish not in cook_book:
            print(f"Ошибка: Блюдо '{dish}' отсутствует в книге рецептов.")
            continue

        for ingredient in cook_book[dish]:
            name = ingredient["ingredient_name"]
            quantity = ingredient["quantity"] * person_count
            measure = ingredient["measure"]

            if name in shopping_list:
                shopping_list[name]["quantity"] += quantity
            else:
                shopping_list[name] = {"measure": measure, "quantity": quantity}
    return shopping_list


def extractor(lines):
    i = 0
    output = {}

    while i < len(lines):
        dish_name = lines[i].strip()
        try:
            ingredient_count = int(lines[i + 1].strip())
        except:
            print("incorrect ing quantity")
            return {}
        ingredients = []

        for j in range(i + 2, i + 2 + ingredient_count):
            name, quantity, measure = map(str.strip, lines[j].split("|"))
            ingredients.append({
                "ingredient_name": name,
                "quantity": int(quantity),
                "measure": measure,
            })

        output[dish_name] = ingredients
        i += 3 + ingredient_count
    return output


lines = []
file = "C:\\Users\\Ruslan\\Documents\\recipes.txt"

def parse_recipes(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f_lines:
            for line in f_lines:
                lines.append(line)
            if len(lines) == 0:
                print("Empty File")
            else:
                output = extractor(lines)
                print(output)
                result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 25, output)
                print("00000000-")
                print(result)

    except:
        print("FileNotFoundError")


cook_book = parse_recipes(file)
if cook_book:
    shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 25, cook_book)
    print(shop_list)