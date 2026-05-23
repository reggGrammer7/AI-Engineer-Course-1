def serve_chai():
    yield "Cup 1: Masala chai"
    yield "Cup 2: Elachai chai"
    yield "Cup 3: Green tea"
stall =serve_chai()
# for cup in stall:
#     print(cup  # Create a normal function 
def get_chai_list():
        return ["cup 1","cup2","cup3"]



def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"
chai = get_chai_gen()
print(next(chai)) 
print(next(chai)) 
print(next(chai)) 
   