# TEORIA 
# new = zaistuje vytvorenie objektu
# init = zaistuje inicializovanie objektu

# REGEX ---------------------------------------------------------------------------------------------------------------------------

# ?= | ?<= positive look ahead | behind
# ?! | ?<! negative 
#.*   any character
#.{4,16}

import re

camel_re = '(?=[A-Z])(?<=[a-z])'

fruits = 'AppleOrangeBananaStrawberryPeach'
print(re.sub(camel_re, ' ', fruits))

-----------------------------


# DICTIONARIES -----------------------------------------------------------------------------------------------------------------------

# LAMBDA

# Je dán slovník, jehož klíče jsou uspořádané trojice znaků a hodnoty představují různě velké seznamy.
# Za pomoci funkcí sort/sorted seřaďte slovník tak, aby byl seřazen podle délky polí na místě hodnot 
# (tj. prvek, jehož hodnotu tvoří nejdelší seznam, bude na konci). 
# V případě stejně dlouhých polí na místě hodnot seřaďte prvky sestupně podle třetího prvku v klíči, 
# který tvoří uspořádaná trojice. Pokud dojde ke kolizi i v tomto případě, seřaďte dané prvky vzestupně podle druhých prvků v klíčích.
# Na velikostech znaků v uspořádaných trojicích nezáleží.
mydict = {("a", "B", "b"):[2, 0], ("A", "c", "b"):[2,1], ("d", "a", "C"):[0, 0, 0], ("A", "A", "A"):[2], ("e", "e", "t"):[2, 3]}


print(sorted(sorted(sorted(mydict.items(), key=lambda i: i[0][1].lower()), key=lambda i: i[0][2].lower(), reverse=True), key=lambda i: len(i[1])))


# STANDARD FUNCTIONS

mydict = {("a", "B", 5):[2, 0], ("A", "c", 5):[2,1], (6, "a", "C"):[0, 0, 0], ("A", "A", "A"):[2], ("e", "e", "t"):[2, 3]}

# Klice na serazeni ziskany pomoci standardnich funkci,
# pomoci lambda viz ISJ_2019.py
def sort_by_second_key(item):
    if isinstance(item[0][1], str):
        return ord(item[0][1].lower())
    else:
        return item[0][1]

def sort_by_third_key(item):
    if isinstance(item[0][2], str):
        return ord(item[0][2].lower())
    else:
        return item[0][2]

def sort_by_len_key(item):
    return len(item[1])

# Sorted radi stabilne, takze muzeme radit od posledniho kriteria.
#    |-------------------------------------------3. seradime podle velikosti pole na miste hodnot ------------------------------------------|
#           |---------------------------2. seradime sestupne podle tretiho prvku klice-------------------------------|
#                  |------1. seradime sestupne podle druheho prvku klice-------|
print(sorted(sorted(sorted(mydict.items(), key=sort_by_second_key, reverse=True), key=sort_by_third_key, reverse=True), key=sort_by_len_key))


# MyBool(int) ------------------------------------------------------------------------------------------------------------------------

# Priklad 2 (thx @Sebastian#7464)
class MyBool(int):
    def __new__(cls, value):
        return super().__new__(cls, bool(value))

    def __repr__(self):
        return "MyBool." + ["True", "False"][self]

x = MyBool(2)
print(x == 1)


# IT, HEADER, FOR -----------------------------------------------------------------------------------------------------------------------     
it = iter(f)
header = next(it)
for v in it:
  line = v.rstrip()
  print(line)
  

 # VYPISOVANIE -----------------------------------------------------------------------------------------------------------------------
def ng(a, n):
    z = (a[i:] for i in range(n))
    return zip(*z)

print(list(ng([1,2,3,4,5,6], 4)))

# RESULT = [(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)]

# ------------------------------------------------ ------------------------------------

# Pri s.add(1) se vypise:
# Prvni se vola metoda add v IntList, ktera vypise "enter IntList".
# Volanim "super().add(item)" se program dostane do metody add v SortedList(),
# vypise se "enter SortedList". Tam se opet vola super().add(item), cimz
# se dostaneme do metody add ve tride ListWAdd a vypise se "enter ListWAdd".
# Nakonec se postupne bude vystupovat z jednotlivych metod.
#
# Tedy:
# "enter IntList"
# "enter SortedList"
# "enter ListWAdd"
# "leave ListWAdd"
# "leave SortedList"
# "leave IntList"

# Pri s.add('a') se vypise:
# vyjimka "TypeError: SortedIntList only supports int" (ne IntList!)

# Co by se stalo, kdyby tridy SortedList a IntList mely misto rodice ListWAdd
# primo tridu list?
# Nebyl by dostupny atribut self._items. Nemohly by volat super().add(item),
# protoze tuto metodu list neimplementuje. TL;DR: crash

# ----------------------------------------------------------------------------------------------------

# Priklad 3
# Vypise se postupne:
#   Third starts
#   First starts
#   Second starts
#   Second ends
#   First ends
#   Third ends
#
#   Proc? Konstruktory se volaji postupne v poradi, v jakem jsou uvedeny.
#   Tedy prvni se v konstruktoru tridy Third vypise "Third starts"
#   a funkci super().__init__() se spusti konstruktor First,
#   ktery vypise "First starts". Nasledne se funkci super().__init__() spusti
#   konstruktor Second, vypise se "Second starts". Pote se vykona zbytek konstruktoru
#   Second ("Second ends"), First ("First ends") a Third ("Third ends").





# PRIKLAD 7 --------------------------------------------------------------------------------------------------------------------------
import collections

def log_and_count(num_of_calls=None, error_message_tail=None):
  def outer(func):
    def inner(*args, **kwargs):
      inner.cntr[func.__name__] += 1
      
      if inner.cntr[func.__name__] > num_of_calls:
        print(error_message_tail)
      else:
        return func(*args, **kwargs)
      
    inner.cntr = collections.Counter
    return inner
  return outer


# PRIKLAD 8.1 ----------------------------------------------------------------------------------------------------------------

def dupl_with_given_key(iterable, key=lambda x: x):
  processed = set()
  
  for item in iterable:
    if key(item) in processed:
      yield item
    else:
      processed.add(key(item))
      
      
 # PRIKLAD 8.2 ----------------------------------------------------------------------------------------------------------------
def first_with_given_key(iterable, key=lambda x: x):
    processed = set()

    for item in iterable:
        if key(item) not in processed:
            processed.add(key(item))
            yield item

print(list(first_with_given_key([1,2,3,1,2,3])))
                 
            
            
  

