#У Пети есть 20 рублей.
#Если одна плитка шоколада стоит 10 рублей, то он сможет купить две плитки.
#Если одна плитка шоколада стоит 5 рублей, то он сможет купить четыре плитки.

#Для данной задачи разберём два случайных события, чтобы проверить работу программы!

a = 5 #стоимость ОДНОЙ плитки
b = 20 #кол-во денег у Пети

if b/a == 4:
  print("Петя сможет купить четыре плитки")
elif b/a == 2:
  print("Петя сможет купить две плитки")

a = 10 #стоимость ОДНОЙ плитки
b = 20 #кол-во денег у Пети

if b/a == 4:
  print("Петя сможет купить четыре плитки")
elif b/a == 2:
  print("Петя сможет купить две плитки")
