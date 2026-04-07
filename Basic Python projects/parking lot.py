def parking_lot():
    parking_slots = {1: None, 2: None, 3: None, 4: None, 5: None}

    while True:
        print("\nWelcome To Parking Lot")
        print("1= Park Vehicle")
        print("2= Remove Vehicle")
        print("3= Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("❌ Invalid input! Enter a number.")
            continue

        if choice == 1:
            if None not in parking_slots.values():
                print("Parking is full")
                continue
            vehicle_id = input("Enter Vehicle ID: ")
            try:
                hours = int(input("Enter Parking Time (hours): "))
            except ValueError:
                print("❌ Enter a valid number of hours")
                continue

            for slot in parking_slots:
                if parking_slots[slot] is None:
                    parking_slots[slot] = (vehicle_id, hours)
                    print(f"✅ Vehicle parked in slot {slot}")
                    break

        elif choice == 2:
            vehicle_id = input("Enter Vehicle ID to remove: ")
            found = False
            for slot, info in parking_slots.items():
                if info is not None and info[0] == vehicle_id:
                    hours = info[1]
                    fee = hours * 2
                    parking_slots[slot] = None
                    print(f"✅ Vehicle removed from slot {slot}")
                    print(f"💰 Total fees: ${fee}")
                    found = True
                    break
            if not found:
                print("❌ Vehicle not found!")

        elif choice == 3:
            print("Exiting Parking Lot...")
            break

        else:
            print("❌ Choose a valid option")

print(parking_lot())