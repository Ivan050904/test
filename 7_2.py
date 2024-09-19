import io

def custom_write(file_name,strings):
    string_positions = {}
    file = open(file_name,'w', encoding= 'utf-8')
    line = 1

    for string in strings:
        position_byte = file.tell()
        file.write(string + '\n')
        string_positions[(line,position_byte)] = string
        line +=1
    file.close()
    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

