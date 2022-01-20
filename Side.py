import threading

var = ""


def varadd(hi):
    global var
    var = hi


t = threading.Thread(target=varadd, args="12")
t.start()
print(var)
