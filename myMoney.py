import math #простенький калькулятор вычета зп по месяцу по дню по часу с учётом выходных (8 выходных в месяце)
def main():
    name = str(input("\n ВВЕДИТЕ СВОЁ ИМЯ -> "))
    try:
        myMoney = int(input(name + ' ВВЕДИТЕ СВОЮ ЗП ЗА МЕСЯЦ \n -> '))
        print('_'*52, "|"*2, name + " ПОЛУЧАЕТ ЗП, С УЧЁТОМ ВЫХОДНЫХ, ПО ДНЯМ, ЧАСАМ, МИНУТАМ ", "|"*2, "_"*50)
        if myMoney > 9999:    
            wDay  = myMoney / 24 
            hours = wDay / 8 
            minut = hours / 60 
            year  = myMoney * 12
            print("\n  тенге в месяц -> " + str(myMoney),
                  f"\n  тенге в год ->  {math.ceil(year)}",
                  f"\n  тенге в день ->  {math.ceil(wDay)}", 
                  f"\n  тенге в час ->    {math.ceil(hours)}", 
                  f"\n  тенге в минуту -> {math.ceil(minut)}") 
        else:
            myMoney < 9998
            print(name + "\n это очень маленькая зарплата, такой не бывает, ты врёшь!\n")
            return main()
    except ValueError: 
        print(name + " пииши число, а не текст!")
        return main()
if __name__ == "__main__":
    main()
    