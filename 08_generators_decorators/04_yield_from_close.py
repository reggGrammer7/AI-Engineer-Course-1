def local_chai():
    yield "masala chai"
    yield "ginger chai"


def imported_chai():
    yield "matcha"
    yield "oolong"


def full_menu():
    yield from local_chai()
    yield from imported_chai()


for chai in full_menu():
    print(chai)






# Controling it to stop midway
def chai_stall():
    try:
        while True:
            order = yield "Waiting for order"
    except:
        print("Stall closed, No more chai")


stall = chai_stall()
next(stall)
stall.close()# close and cleanup memory