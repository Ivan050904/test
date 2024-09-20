team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
print(' В команде мастера кода участников: %d' % team1_num)
print('Сегодня участников в командах %d и %d' %(team1_num, team2_num))
print('Команда волшебники данных решила задач: {}{}'.format(score_2,'!'))
print('Волшебники данных решили задачу за {}{}'.format(team1_time, 'c!'))
print(f'Количество решенных задач по командам: {score_1} и {score_2} задач')
print(f'Результат битвы: {challenge_result}')
print(f'сегодня было решено {tasks_total} задач в среднем по {time_avg} секунды на задачу')