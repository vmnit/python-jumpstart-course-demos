import os.path


def print_banner():
    print("--------------------------------------")
    print("------------ JOURNAL APP -------------")
    print("--------------------------------------")

def load_data(fname):
    if os.path.exists(fname):
        print("... loading from {} ...".format(fname))
        with open(fname, 'r') as f:
            data = f.readlines()
            print("... loaded {} entries ...".format(len(data)))
            return data
    else:
        print("... {} is empty ...".format(fname))
        return list()

def print_data(data):
    for i in range(len(data)):
        print ("{}. {}".format(i, data[i]))

def do_operation(data):
    while(True):
        choice = input("What do you want to do? [L]ist, [A]dd, or E[x]it? ")
        choice = choice.lower().strip()
        if (choice == 'l'):
            print_data(data)
        elif (choice == 'a'):
            new_data = input("Enter your journal entry:\n")
            data.append(new_data)
        elif (choice == 'x'):
            return data
        else:
            print("Wrong choice!!!")

def write_data(fname, data):
    dir = os.path.dirname(fname)
    if not os.path.exists(dir):
        os.makedirs(dir, exist_ok=True)

    print("... saving to {}".format(fname))
    with open(fname, 'w') as f:
        for i in range(len(data)):
            f.write(data[i])
        print("...saving complete...")


def main():
    print_banner()
    fname = "./data/default.jrn"
    data = load_data(fname)
    data = do_operation(data)
    write_data(fname, data)

main()