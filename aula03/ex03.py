from digitInput import floatInput

student_grades = [floatInput(f'Insira sua {n+1}ª nota:\n>>>', lambda value: 0 <= value <= 10) for n in range(3)]

grade_average = sum(student_grades) / len(student_grades)

print(f'Sua média é {grade_average:5.2f}')

if grade_average<3:
    print('reprovado')
elif grade_average<7:
    print('exame de recuperação')
else:
    print('aprovado')