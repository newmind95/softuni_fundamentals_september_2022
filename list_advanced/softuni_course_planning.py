from typing import List


def check_exist_lesson(lesson: str, schedule: List[str]) -> bool:
    if lesson in schedule:
        return True

    return False


initial_schedule = input().split(', ')

command = input()
while not command == 'course start':

    action = command.split(':')[0]
    lesson_title = command.split(':')[1]
    lesson_exist = check_exist_lesson(lesson_title, initial_schedule)

    if action == 'Add':

        if not lesson_exist:
            initial_schedule.append(lesson_title)
        # print(initial_schedule)
        # print()

    elif action == 'Insert':

        index = int(command.split(':')[2])

        if not lesson_exist and 0 <= index < len(initial_schedule):
            initial_schedule.insert(index, lesson_title)
            # print(f'Insert {lesson_title} at index {index}')
            # print(initial_schedule)
            # print()

    elif action == 'Remove':

        lesson_exercise_exist = check_exist_lesson(f'{lesson_title}-Exercise', initial_schedule)
        if lesson_exist:
            initial_schedule.remove(lesson_title)
            # print(f'Remove {lesson_title} successfully')
            # print(initial_schedule)
            # print(f'Remove {lesson_title}-Exercise successfully')
            # print()

        if lesson_exercise_exist:
            initial_schedule.remove(f'{lesson_title}-Exercise')
        
        # else:
        #     print(f'{lesson_title} or {lesson_title}-Exercise does not exist')
        

    elif action == 'Swap':
        other_lesson_title = command.split(':')[2]
        other_lesson_exist = check_exist_lesson(other_lesson_title, initial_schedule)
        # print('Swap method')

        if lesson_exist and other_lesson_exist:
            index_of_lesson_title = initial_schedule.index(lesson_title)
            index_of_other_lesson = initial_schedule.index(other_lesson_title)
            print(f'{lesson_title} and {other_lesson_title}')

            initial_schedule[index_of_lesson_title], initial_schedule[index_of_other_lesson] = initial_schedule[index_of_other_lesson], initial_schedule[index_of_lesson_title]
            print(initial_schedule)
            
            if check_exist_lesson(f'{other_lesson_title}-Exercise', initial_schedule):
                initial_schedule.remove(f'{other_lesson_title}-Exercise')
                index_of_lesson_title = initial_schedule.index(other_lesson_title)
                initial_schedule.insert(index_of_lesson_title + 1, f'{other_lesson_title}-Exercise')
                print(f'{lesson_title} and {other_lesson_title} swapped')
                print(f'insert {lesson_title} at index {index_of_lesson_title + 1}')
                print(initial_schedule)
                print()
        else:
            print(f'{lesson_title} or {other_lesson_title} does not exist!')
            print()

    elif action == 'Exercise':
       
        if not lesson_exist:
            initial_schedule.append(lesson_title)
            # print(f'exerice method')
            # print(initial_schedule)
            # print()

        if  f'{lesson_title}-Exercise' not in initial_schedule:
            initial_schedule.append(f'{lesson_title}-Exercise')
            # print(f'{lesson_title} is not equal ot {lesson_title}-Exercise')
            # print(f'Append {lesson_title}-Exercise')
            # print(initial_schedule)
            # print()

    command = input()

for lesson_index, lesson_title in enumerate(initial_schedule):
    print(f'{lesson_index + 1}.{lesson_title}')
