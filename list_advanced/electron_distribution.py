number_of_electrons = int(input())
electrons_list = []
index = 0

while number_of_electrons > 0:
    index += 1
    shell = 2 * index ** 2

    if number_of_electrons >= shell:
        electrons_list.append(shell)
        number_of_electrons -= shell
    else:
        electrons_list.append(number_of_electrons)
        number_of_electrons = 0

print(electrons_list)
