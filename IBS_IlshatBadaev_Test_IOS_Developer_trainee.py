def convert_string(str, count):
    inner_res = ''
    result = ''
    inner_str = ''
    j = 0
    
    while j < len(str):
        if (str[j].isdigit()):
            bracket_pair = 1                                      # указываем на наличие скобок
            close_bracket_index = j + 2                           # задаем индекс символа, после начинающейся скобки
            while bracket_pair > 0:                               # поиск индекса закрывающейся скобки
                if (str[close_bracket_index] == ')'): 
                    bracket_pair -= 1
                if (str[close_bracket_index] == '('):
                    bracket_pair += 1
                close_bracket_index += 1
            inner_str = str[j + 2: close_bracket_index - 1]       # содержимое внутренней строки
            inner_res += convert_string(inner_str, int(str[j]))   # после нахождения внутр. строки, передаем в функцию, и так ищем пока не закончатся скобки
            j = close_bracket_index                               # если символы остались после скобки, проверяем дальше
        else:
            inner_res += str[j];                                  # если это не цифра, а буква, прибавляем к промежуточному результату
            j = j + 1                                        
            
    while count != 0:                                             # сколько раз мы печатаем строку
        result += inner_res                                        
        count -= 1                                          
    return result

input_string = input()
output_string = ''
temp = 0

for i in range(len(input_string)):                                # Проверка на корректность введенных данных
    if input_string[i] == '(':                                  
        if i == 0 or not input_string[i - 1].isdigit():
            print('Данные введены не корректно:', input_string, 'Проверьте введенные данные')
            quit()
        temp += 1
    if input_string[i] == ')':
        temp -= 1
if temp != 0:
    print('Данные введены не корректно:', input_string, 'Проверьте введенные данные')
    quit()

output_string = convert_string(input_string, 1)
print(output_string)