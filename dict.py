def fizzbuzz():
  print "fizzbuzz"
def fizz():
  print "fizz"
def buzz():
  print "buzz"
def other():
  print i 
dictionary={0:fizzbuzz,
            1:other,
            2:other,
            3:fizz,
            4:other,
            5:buzz,
            6:fizz,
            7:other,
            8:other,
            9:fizz,
            10:buzz,
            11:other,
            12:fizz,
            13:other,
            14:other}
for i in range(1,10000001):
  dictionary[i%15]()
