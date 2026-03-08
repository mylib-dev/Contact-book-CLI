import json

try:
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = {}
 
def save():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)
while True:
    user_input = input("You: ")
    if "bye" in user_input or "break" in user_input:
        break
    elif user_input in contacts:
        print(contacts[user_input])
    elif "create new contact" in user_input or "new" in user_input or "create" in user_input:
        create = input("Do you want to create a new contact: ").lower().strip()
        if create == "yes":
          name = input("Enter the name of the new contact").strip().lower()
          phone = input("Enter the phone number of the contact").strip()
          contacts[name] = phone
          save()
    elif "delete" in user_input or "delete contact" in user_input:
       query = input("Do you want to delete a contact? \n ").strip().lower()
       if query == "yes":
           identity = input("Enter the name of the contact you want to delete ").lower().strip()
           if identity in contacts:
               del contacts[identity]
               save()
    elif "all" in user_input:
      print(contacts)