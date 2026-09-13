import json
import os
import sys

#////////CHANGES MADE-[Code n+5]//////////
# Fixed bugs and made sure the error handling is responsive so the script doesn't crash

def counter (tickets, key, value):
    count = 0
    for ticket in tickets:
        if ticket.get(key, 'missing') == value:
            count += 1
    return count

def customer_with_most_open_ticket (tickets):
    most_open_ticket = {}
    highest_count  = 0
    winner = []
    for ticket in tickets:
        customer = ticket.get('customer', 'missing')
        status = ticket.get('status', 'missing')
        if status == 'open':
            most_open_ticket[customer] = most_open_ticket.get(customer, 0) + 1
        
    for customer, count in most_open_ticket.items():
        if count > highest_count:
            highest_count = count
            winner = [customer]
            
        elif count == highest_count:
           winner.append(customer)

    else:
        if not winner:
            return "None", 0
    
    winner = ', '.join(winner)            
    return winner, highest_count

def print_dashboard (file_path):
    
    if not os.path.exists(file_path):
        print('Error: File does not exist')  
        print('Check if the file name is correct')  
        print('Also check if the file extension is correct')
        print('If all is correct then make sure the file path is correct')
        return " "   
    if os.path.isdir(file_path):
        print('File only points to a directory')
        print('Add a file name to the path')
        return " "
    
    try:
        with open (file_path, 'r') as f:
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

if __name__=='__main__':
    if len(sys.argv)<2:
        print('ERROR: Missing inputs')
        print('Usage: python script.py <path_to_log_file>')
        sys.exit(1)

file_path = sys.argv[1]
print_dashboard (file_path)
