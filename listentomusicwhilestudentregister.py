import webbrowser

students = []

while True:
    print("\n1. Add student\n2. List students\n3. Find student\n4. Calculate average age\n5. Remove student\n6. Exit\n7. Listen to music")
    option = input("Please select option: ")

    if option == "1":
        name = input("Name: ")
        try:
            age = int(input("Age: "))
            students.append({"name": name, "age": age})
            print(f"{name} has been added.")
        except:
            print("Age must be a number.")
            input("Press Enter to return to Menu...")
    
    elif option == "2":
        if students:
            print("\nAll students:")
            for s in students:
                print(s["name"], s["age"])
        else:
            print("No students registered")
        input("Press Enter to return to menu...")

    elif option == "3":
        n = input("Submit name: ")
        registered = False
        for s in students:
            if s["name"].lower() == n.lower():
                print("Found:", s["name"], s["age"])
                registered = True
        if not registered:
            print("Student not found.")
        input("Press Enter to return to menu...")
    
    elif option == "4":
        if students:
            print("Average age:", sum(s["age"] for s in students)/len(students))
        else:
            print("No students registered.")
        input("Press Enter to return to menu...")
    
    elif option == "5":
        n = input("Name to remove: ")
        new = [s for s in students if s["name"].lower() != n.lower()]
        if len(new) < len(students): 
            students = new
            print(n, "have been removed.")
        else:
            print("Student not found.")
        input("Press Enter to return to menu...")

    elif option == "6":
        print("Thank you for using my studentlist system, have a nice day!")
        break

    elif option == "7":
        playlist_url = "https://open.spotify.com/playlist/5zY8rz559jQmq2rPMUKhSO"  # Some of my favourite songs
        print("Opening Saids favourite playlist on his Spotify...")
        webbrowser.open(playlist_url)
        input("Press Enter to return to menu...")

    else:
        print("Invalid choice")
        input("Press Enter to return to menu...")
