## https://www.youtube.com/watch?v=9H6muyZjms0
# nie działa, coś chyba nie tak z get_stats to chyba 2.0

class_list = [[["peter", "parker"], [80.0, 70.0, 85.0]],
            [["bruce", "wayne"], [100.0, 80.0, 74.0]],
            [["captain", "america"], [8.0, 10.0, 96.0]]]


def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
        print(new_stats)
    return new_stats


def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print("waring: no grades data")
    except:
        print("error")


print(get_stats)




#try:
#    a = int(input("give me 1st num"))
#    b = int(input("give me 2nd num"))
#    print("a/b", a/b)
#    print("a+b", a+b)
#except ValueError:
#    print("ValueError: could not convert to a number")
#except ZeroDivisionError:
#    print("ZeroDivisionError: can not divide by zero")
#except:
#    print("GeneralError: something went wrong")
