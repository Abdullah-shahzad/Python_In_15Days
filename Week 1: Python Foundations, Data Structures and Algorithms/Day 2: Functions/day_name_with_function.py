def day_name(n):
    while n:
        d = input("Please enter a day of the week: ")
        day = d.lower()
        n -= 1
        match day:
            case 'sunday':
                print("It's Sunday!")
            case 'monday':
                print("It's Monday!")
            case 'tuesday':
                print("It's Tuesday!")
            case 'wednesday':
                print("It's Wednesday!")
            case 'thursday':
                print("It's Thursday!")
            case 'friday':
                print("It's Friday!")
            case 'saturday':
                print("It's Saturday!")
            case _:
                print("It's not a day name.")




number = int(input('Enter a number: '))
day_name(number)


