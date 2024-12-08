file1 = open("C:\\Users\\RuslanMammadov\\Downloads\\recipes.txt", "r", encoding="utf-8")
i = 0
output = {}
lines = file1.readlines()


while i < len(lines) - 1:

    dish = lines[i].rstrip()
    output[dish] = []
    count = int(lines[i + 1])

    j = i + 2
    e = i + count + 3


    while j < e - 1:
        line = lines[j].rstrip().split("|")
        cash = {"ingredient_name": line[0], "quantity": line[1], "measure": line[2]}
        output[dish].append(cash)
        j += 1

    i = e
print(output)


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        for ing in output[dish]:
            if ing["ingredient_name"] in result.keys():
                result[ing["ingredient_name"]]["quantity"] = int(result[ing["ingredient_name"]]["quantity"]) * person_count

            else:
                result[ing["ingredient_name"]] = {"measure": ing["measure"],"quantity": int(ing["quantity"]) * person_count}
    return result


result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 25)
print("00000000-")
print(result)
