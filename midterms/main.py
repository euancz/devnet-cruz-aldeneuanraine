device_list = []

def add_device():
    name = input("Enter device name: ")
    ip = input("Enter ip: ")
    status = input("Enter device status: ")
    full = name + ip + status
    device_list.append(full)
    print(device_list)

def view_device():
    pass

def count_active_inactive(device_list):
    pass

def find_device(device_list):
    pass

def display_menu():
    pass

#def main(): 
    #while True:
       #userinp = input("")

add_device()