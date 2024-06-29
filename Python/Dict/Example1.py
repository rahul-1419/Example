countries = {
    "india":16,
    "usa":17,
    "japan":89
}

def add():
  add = input("Enter the country name: ")
  if add in countries:
    print("country already exists")
    return
  p = input("Enter the population")
  countries[add] = p
  print(countries)

def remove():
  remove = input("Enter the country name to remove: ")
  if remove in countries:
    del countries[remove]
    print_all()
  else:
    print("country not found")

def print_all():
  for key,value in countries.items():
    print(f"{key} ==> {value}")

