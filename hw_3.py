file_info = []
filenames = ['file1.txt', 'file2.txt', 'file3.txt']
    
for filename in filenames:
    with open(filename, 'r', encoding='utf-8') as file:
      lines = file.readlines()
      file_info.append([filename, len(lines), lines])
    
file_info.sort()
    
with open('result.txt', 'w', encoding='utf-8') as result_file:
    for info in file_info:
        for line in info:
            result_file.write(str(line) + '\n')


