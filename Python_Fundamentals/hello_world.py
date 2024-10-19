if __name__ == "__main__":
    print("Hello, World!")

    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")

    initials = first_name[0].upper() + last_name[0].upper()

    # print("Hello", first_name, "your initials are:", initials)
    # print("Hello " + first_name + " your initials are: " + initials)
    print(f"Hello {first_name} your initials are: {initials}")
