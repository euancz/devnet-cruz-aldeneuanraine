device_list = []

def add_device():
    name = input("Enter device name: ")
    ip = input("Enter ip: ")
    status = input("Enter device status: ")
    full = name + ip + status
    device_list.append(full)
    print(device_list)

def view_device():
    for devices in device_list:
        print (devices)

def count_active_inactive(device_list):
    for devices in device_list:
        if(devices == "Active"):
            print(devices)

def find_device(device_list):
    pass

def display_menu():
    pass

def main(): 
    while True:
       print("=== Network Device Inventory ===")
       print(" 1. Add a device\n 2. View all devices \n 3. Count active vs inactive devices\n 4. Find a device by name\n 5. Exit")
       userinp = input("Choose an option: ")

main()
