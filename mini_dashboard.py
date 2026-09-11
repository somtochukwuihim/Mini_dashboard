import json
import os

#////////CHANGES MADE-[Code n+3]//////////
# created the counter function to:
# loop through the tickets and compare: key to matching value condition
# Avoid repetitive code.

def counter (tickets, key, value):
    count = 0
    for ticket in tickets:
        if ticket.get(key, 'misising') == value:
            count += 1
    return count

def customer_with_most_open_ticket (tickets):
    most_open_ticket = {}
    highest_count  = 0
    winner = []
    for ticket in tickets:
        customer = ticket['customer']
        status = ticket['status']
        if status == 'open':
            most_open_ticket[customer] = most_open_ticket.get(customer, 0) + 1
        
    for customer, count in most_open_ticket.items():
        if count > highest_count:
            highest_count = count
            winner = [customer]
            
        elif count == highest_count:
           winner.append(customer)
    
    winner = ', '.join(winner)            
    return winner, highest_count

def print_dashboard (tickets=None):
    if tickets is None:
        return 'Error: No file/file-path was provided to the function.'
    
    if not os.path.exists(tickets):
        raise FileNotFoundError ('Error: File does not exist') 
    
    if os.path.isdir(tickets):
        return 'File only points to a directory'
    
    try:
        with open (tickets, 'r') as f:
            ticket_holder =  json.load(f)
            tickets = ticket_holder

            open_ticket = counter (tickets, 'status', 'open')
            closed_tickets = counter (tickets, 'status', 'closed')
            high_priority_tickets = counter (tickets, 'priority', 'high')
            customer, count = customer_with_most_open_ticket (tickets)
            print ('=========SUPPORT DASHBOARD===========\n')
            print (f'Open Tickets: {open_ticket}\n')
            print (f'Closed Tickets: {closed_tickets}\n')
            print (f'High Priority Tickets: {high_priority_tickets}\n')
            print (f'Customer with Most Ticket: \n{customer} ({count})')
            print('=====================================')
            return ''
    except json.JSONDecodeError:
        return 'Error: The file exists but does not contain valid JSON format.'


        

trial = print_dashboard ('mini_dashboard_practice_file.json')
print (trial)