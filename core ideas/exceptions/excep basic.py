#v.4
try:
    f = open("test_file.txt")
#    var = bad_var # wł/wył dla sprawdzenia FileNotFoundError
except FileNotFoundError as e: # zdefiniowany wyjątek, PEP8- generalizować w dół
    print(e) #trackeback po zmiennej
except Exception as e: # wyjątek ogólnie
    print(e) #traceback po zmiennej
else:
    print(f.read()) # w przypadku braku wyjątku odczyta i zamknie plik
    f.close()
finally:
    print("sprawdzam finally")




#v.3
#try:
#    f = open("test_file.txt")
#    var = bad_var # wł/wył dla sprawdzenia FileNotFoundError
#except FileNotFoundError as e: # zdefiniowany wyjątek, PEP8- generalizować w dół
#    print(e) #trackeback po zmiennej
#except Exception as e: # wyjątek ogólnie
#    print(e) #traceback po zmiennej

#v.2
#try:
#    f = open("test_file.txt")
#    var = bad_var
#except FileNotFoundError: # zdefiniowany wyjątek, PEP8- generalizować w dół
#    print("This file does not exist.")
#except Exception: # wyjątek ogólnie
#    print("Something went wrong.")



#v.1
#try:
#    f =open("testfile.txt")
#except Exception:
#    print("error")
# else:
#   pass
# finally"
#    pass

#https://www.youtube.com/watch?v=NIWwJbo-9_8
