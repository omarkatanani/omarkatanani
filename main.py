import datetime
import os
#create local list 
tickets = []

#https://www.freecodecamp.org/news/file-handling-in-python/
#func for display admin menu
def display_admin_menu():
    print("--- Admin Menu: ---")
    print("1. Display Statistics")
    print("2. Book a Ticket")
    print("3. Display all Tickets")
    print("4. Change Ticket Priority")
    print("5. Disable Ticket")
    print("6. Run Events")
    print("7. Exit")

#func for display user menu
def display_user_menu():
    print("--- User Menu: ---")
    print("1. Book a ticket")
    print("2. Exit")

#func for choices related to administator 
def admin_menu(choice):
    if choice == 1:
        print("------- Statistics Display -------")
        display_statistics(tickets)
    elif choice == 2:
        book_a_ticket(tickets)
    elif choice == 3:
        print("------- All Tickets Display -------")
        display_all_tickets(tickets)
    elif choice == 4:
        print("------- Change Ticket Priority -------")
        change_ticket_priority(tickets)
    elif choice == 5:
        print("------- Disable Ticket -------")
        disable_ticket(tickets)
    elif choice == 6:
        print("------- Runing Events For Ticket ID -------")
        run_events(tickets)
    elif choice == 7:
        exit_program()
    else:
        print("Invalid choice. Please try again.")
#func for user login 
def user_menu(choice):
    if choice == 1:
        book_a_ticket(tickets)
    elif choice == 2:
        save_and_exit(tickets)
    else:
        print("Invalid choice. Please try again.")
      
# this function to show the event ID with the highest number of tickets.
# searching by the maximum of the number of tickets entered from admin and user
def display_statistics(tickets):
  counts = {}
  for ticket in tickets:
    event_id = ticket['event_id']
    if event_id not in counts:
      counts[event_id] = 0
    counts[event_id] += 1
  max= 0
  max_event_id = None
  for event_id, count in counts.items():
    if count > max:
      max = count
      max_event_id = event_id
  print("The highest number of events is:", max_event_id, "with", max, "tickets.")
  
# func for add the tickets from admin and user , and stored in list under name 'ticket'
def book_a_ticket(tickets):
  event_id= int(input("enter the event ID: "))
  username =str(input("Enter the your username: "))
  priority = int(input("enter the priority: "))
  ticket_id = len(tickets) + 1
  ticket ={
    'tick' : ticket_id,
    'event_id' : event_id,
    'username': username, 
    'timestamp' : datetime.datetime.today().strftime("%Y-%m-%d"),
    'priority' : priority,
  }
  tickets.append(ticket)
  print("Ticket booked successfully!")
  print(tickets)
  # https://www.programiz.com/python-programming/datetime/current-datetime

# func for display all tickets stored in list
def display_all_tickets(tickets):
  # The lambda function is applied to each item in the list, and the resulting values are used to determine the sort order.
  # https://blogboard.io/blog/knowledge/python-sorted-lambda/
  tickets.sort(key=lambda ticket: (ticket['timestamp'], ticket['event_id']))
  for ticket in tickets:
    print(ticket)
#func for change the priority number of event this option for admin only 
def change_ticket_priority(tickets):
    ticket_id = int(input("Enter the ticket ID: "))
    new_priority = int(input("Enter the new priority: "))

    for ticket in tickets: 
     if ticket['tick'] == ticket_id:
       ticket['priority'] = new_priority
       print("The priority number has been changed !!")
       break
# func for allow the admin to remove a ticket from the system by providing the ticket ID       
def disable_ticket(tickets):
  ticket_id = int(input("Enter the ID to disable: "))
  tickets.sort(key=lambda ticket: (ticket['timestamp'], ticket['event_id']))
  for ticket in tickets:
    if ticket['tick'] == ticket_id:
      tickets.remove(ticket)
      print("\nThe ticket disabled successfully! ..!")
      break
  else:
    print("\nthis ticket not found ..!")
    
    
# func for display today's events found in the list
def run_events(tickets):
  for ticket in tickets:
        if ticket['timestamp']== datetime.datetime.today().strftime("%Y-%m-%d"):
            print(ticket)
        else:
          print("the ticket is not found")
          #(%Y-%m-%d)===>(YYYY-MM-DD)

# func for user only when he exit the prgramme ,the system will be automaticaly save the data in file    
def save_and_exit(tickets):
  # https://bobbyhadz.com/blog/python-save-user-input-to-file
  # create file under name 'tickets1.txt'
    file_ticket = 'tickets1.txt'
    with open(file_ticket, 'w', encoding='utf-8') as my_file_tickets:
      my_file_tickets.write(str(tickets))
    print("tickets saved in file tickets1.txt")
    exit()
# func for close the system
def exit_program():
    print("------ Thank you ------ .")
    exit()

# Main function
def main():
  print("------Welcome to the Ticketing System-----")
  #Adminstration validation code for login
  attempts = 0
  while attempts < 5: 
    user_name =input("Enter Your Username To login :")
    password =input("Enter the password :")
    if user_name == "admin" and password == "admin123123":
      print("Your Welcome admin !!")
      while True:
        display_admin_menu()
        admin_choice = int(input("chooes a number: "))
        admin_menu(admin_choice)
    elif user_name == "user" and password == '':
      print("Welcome TO User Menu!! ")
      while True:
        display_user_menu()
        user_menu1 =int(input("chooes a number: "))
        user_menu(user_menu1)
    else:
      print("Incorrect username or password")
      attempts += 1 #counts 5 times
  if attempts == 5:
    print("You tried 5 times....")
    
    
if __name__ == "__main__":
   main()
