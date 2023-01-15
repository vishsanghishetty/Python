def format_name(fname, lname):
    # first_name = input("Enter your first name\n")
    # last_name = input("Enter your first name\n")
    # return print(f"{first_name.title()}  {last_name.title()}")
    return fname.title() + " " + lname.title()


output = format_name('VISHALI', 'SANGHISHETTY')
print(output)
