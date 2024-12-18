filepath ="E:\\colab_F\\home\\txt\\"
def files_to_list(filepath ,files):
    list_files = []

    for filename in files:
        lines =[]
        file =filepath + filename
        try:


            with open(file, "r", encoding="utf-8") as f_lines:
                lines.append(filename)
                for line in f_lines:
                    lines.append(line.strip())
                if len(lines) ==0:
                    print("Empty File")
                else:
                    lines.insert(1,len(lines)-1)  
                    list_files.append(lines)
        except:
            print("FileNotFoundError")

    return list_files
list_files = files_to_list(filepath ,["1.txt" ,"2.txt" ,"3.txt"])

def parcing(list_files):
    result = []
    for file in sorted(list_files,key=len):
        for line in file:
            result.append(line)

    return result
result = parcing(list_files)
print("------------------------")
print(result)
with open(filepath + 'result_file.txt', 'w') as f:
    f.writelines([f"{line}\n" for line in result])