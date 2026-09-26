device_list = []

def add_device():
    name = input("Enter device name: ")
    ip = input("Enter ip: ")
    status = input("Enter device status: ")
    full = name + ip + status
    device_list.append(full)

def view_device():
    for devices in device_list:
        print(devices)

def count_active_inactive(device_list):
    for devices in device_list:
        if(devices == "Active"):
            print(devices)

def find_device(device_list):
    pass

def display_menu():
    print("=== Network Device Inventory ===")
    print(" 1. Add a device\n 2. View all devices \n 3. Count active vs inactive devices\n 4. Find a device by name\n 5. Exit")

def main():
    running = True
    while running:
        display_menu()
        userinp = input("Choose an option: ") 
        if(userinp == "1"):
            add_device()
        elif(userinp == "2"):
            view_device()
        elif(userinp == "3"):
            count_active_inactive()
        elif(userinp == "4"):
            find_device()
        elif(userinp == "5"):
            running = False
            print("You have exited the program")
        else:
            print("Invalid Input!")
main()