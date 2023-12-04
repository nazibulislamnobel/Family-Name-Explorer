def relatives(persons, last_name):
    common_last_names = []
    for first_name, ln in persons.items():
        if ln == last_name:
            common_last_names.append(first_name)
    return common_last_names

def main():
    persons = {}
    names_input = input("Enter names: \n").split()

    for i in range(0, len(names_input), 2):
        first_name = names_input[i]
        last_name = names_input[i + 1]
        persons[first_name] = last_name

    print("\nFirst Name   Last NAME")
    for first_name, last_name in persons.items():
        print(f"{first_name.ljust(15)}{last_name}")

    family_name = input("\nEnter family name: ")

    common_last_names = relatives(persons, family_name)

    
    if common_last_names:
        print(f"\nPersons with the same last name, {family_name}:")
        for name in common_last_names:
            print(name)
    else:
        print("\nNo persons with the same last name.")

if __name__ == "__main__":
    main()