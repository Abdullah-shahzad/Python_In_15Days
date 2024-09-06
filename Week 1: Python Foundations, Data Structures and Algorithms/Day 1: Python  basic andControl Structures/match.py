number = int(input('Enter a number: '))

for i in range(number):
    d = input("Please enter a day of the week: ")
    day = d.lower()

    match day:
        case 'sunday':
            print(f"{i+1}: It's Sunday!")
        case 'monday':
            print(f"{i+1}: It's Monday!")
        case 'tuesday':
            print(f"{i+1}: It's Tuesday!")
        case 'wednesday':
            print(f"{i+1}: It's Wednesday!")
        case 'thursday':
            print(f"{i+1}: It's Thursday!")
        case 'friday':
            print(f"{i+1}: It's Friday!")
        case 'saturday':
            print(f"{i+1}: It's Saturday!")
        case _:
            print(f"{i+1}: It's not a day name.")
