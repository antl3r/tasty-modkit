def yes_no_prompt(question):
    while True:
        answer = input(question + " (y/n): ").strip().lower()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")