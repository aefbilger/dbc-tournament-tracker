participants = []
count = 0

def setup():
    global count
    
    print("Welcome to Tournaments R Us\n============================")
    
    validated = False
    while not validated:
        num = input("Enter the number of participants: ")
        if not num.isnumeric():
            print("Error: Please enter a valid number of participants.")
            continue
        num = int(num)
        if num < 1:
            print("Error: Must have at least one participant.")
        else:
            validated = True
    
    count = num
    
    print(f"There are {count} participant slots ready for sign-ups.")
    
    menu()

def menu():
    done = False
    while not done:
        print("\n")
        print("Participant Menu\n================")
        print("1. Sign Up")
        print("2. Cancel Sign Up")
        print("3. View Participants")
        print("4. Search")
        print("5. Exit")

        choice = input("\nPlease select an option from the menu above, by number: ")
        
        if choice == '1':
            signup()

        elif choice == '2':
            if participants == []:
                print("Error: No participants are registered, so you cannot cancel registrations.")
            else:
                cancel()

        elif choice == '3':
            view()

        elif choice == '4':
            search()

        elif choice == '5':
            print("\n")
            print("Exit\n=====")
            print("Are you sure you want to exit?\nAll data will be lost.")
            sure = input("Exit? [y/n] ")
            if sure.lower() == 'y':
                done = True
        
        else:
            print("\nI'm sorry, I didn't recognize that response. Please try again.")

def signup():
    global participants
    print("\n")
    print("Participant Sign Up\n====================")

    participant_dict = {}
    name = input("Participant Name: ")
    
    participant_dict['name'] = name

    validated = False
    while not validated:
        slot = input(f"Desired starting slot #[1-{count}]: ")
        if not slot.isnumeric():
            print("Error: Please enter a valid slot number.")
            continue
        slot = int(slot)
        if slot < 1 or slot > count:
            print("Error: Slot number out of range. Please try again.")
        else:
            taken = False
            for participant in participants:
                if participant['slot'] == slot:
                    taken = True
                    print(f"Error: Slot #{slot} is filled. Please try again.")
                    break
            if not taken:
                validated = True
    
    participant_dict['slot'] = slot

    participants.append(participant_dict)

    print(f"{name} is signed up in starting slot #{slot}")

def cancel():
    print("\n")
    print("Participant Cancellation\n========================")

    participant_index = -1

    while participant_index == -1:
        slot = input(f"Starting slot #[1-{count}]: ")

        if not slot.isnumeric():
            print("Error: Invalid slot number!")
            continue
        slot = int(slot)
        if slot > count or slot < 1:
            print("Error: Slot number out of range!")
            continue

        name = input("Participant Name: ")

        for i in range(len(participants)):
            if participants[i]['name'] == name and participants[i]['slot'] == slot:
                participant_index = i
                break

        print(f"Error: {name} is not in that starting slot.")

    participants.pop(i)

    print(f"Success: {name} has been cancelled from starting slot #{slot}")

def view():
    print("\n")
    print("View Participants\n=================")

    valid = False
    while not valid:
        slot = input(f"Starting slot #[1-{count}]: ")
        if not slot.isnumeric():
            print("Error: Please enter a valid slot number.")
            continue
        slot = int(slot)
        if slot < 1 or slot > count:
            print("Error: Slot number out of range. Please try again.")
        else:
            valid = True

    # Ensure that the full view range is valid
    if slot - 5 < 1:
        start = 1
    else:
        start = slot - 5
    
    if slot + 5 > count:
        end = count
    else:
        end = slot + 5

    print("Starting slot: Participant")
    for i in range(start, end+1):
        print(f"{i}: ", end = '')
        found = False
        for participant in participants:
            if participant['slot'] == i:
                found = True
                print(participant['name'])
                break
        if not found:
            print("[empty]")

def search():
    print("\n")
    print("Search Participants\n===================")

    name = input("Participant Name: ")

    for participant in participants:
        if participant['name'] == name:
            print(f"{name} has starting slot #{participant['slot']}")
            return
    print(f"{name} was not found in the list of participants.")

setup()
        
            
    



