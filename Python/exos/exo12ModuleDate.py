from datetime import date

date1 = date(1998, 4, 23)
today = date.today()

diff = today - date1


print(f"Nombre de jours : {diff}")
print(f"Nombre d'années : {diff.days // 365}")
