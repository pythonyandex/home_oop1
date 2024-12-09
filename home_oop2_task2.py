
filepath ="C:\\Users\\RuslanMammadov\\Downloads\\Home2\\"
def files_to_list(filepath ,files):
    list_files = []

    for file in files:
        lines =[]
        file =filepath + file
        try:

            with open(file, "r", encoding="utf-8") as f_lines:
                for line in f_lines:
                    lines.append(line.strip())
                if len(lines) ==0:
                    print("Empty File")
                else:
                    list_files.append(lines)
        except:
            print("FileNotFoundError")
    return list_files
list_files = files_to_list(filepath ,["1.txt" ,"2.txt" ,"3.txt"])

def parcing(list_files):
    result = []
    for file in sorted(list_files)[::-1]:
        for line in file:
            result.append(line)

    return result
result = parcing(list_files)
print(result)