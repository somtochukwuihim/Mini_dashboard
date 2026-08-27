import json 
import os 

# Code Zero

def count_open_tickets (tickets): 
    open_count = 0 
    with open (tickets, 'r') as f: 
        ticket_holder = json.load(f) 
        for ticket in ticket_holder: 
            status = ticket['status'] 
            if status == 'open':
                open_count +=1 
        return open_count 
        
def count_closed_tickets(tickets): 
    closed_count = 0 
    with open (tickets, 'r') as f: 
        ticket_holder = json.load(f) 
        for ticket in ticket_holder: 
            status = ticket['status'] 
            if status == 'closed': 
                closed_count += 1 
        return closed_count 
        
def count_high_priority (tickets): 
    high_priority = 0 
    with open (tickets, 'r') as f: 
        ticket_holder = json.load(f) 
        for ticket in ticket_holder: 
            priority = ticket['priority'] 
            if priority == 'high': 
                high_priority += 1 
        return high_priority 

def customer_with_most_open_ticket (tickets): 
    most_open_ticket = {} 
    highest_count = 0 
    with open (tickets, 'r') as f: 
        ticket_holder = json.load(f) 
        for ticket in ticket_holder: 
            customer = ticket['customer'] 
            status = ticket['status'] 
            if status == 'open': 
                most_open_ticket[customer] = most_open_ticket.get(customer, 0) + 1 

        for customer, count in most_open_ticket.items(): 
            if count > highest_count: 
                highest_count = count 
                winner = customer 
        return winner, highest_count 
    
def print_dashboard (tickets=None): 
    if tickets is None: return 'Error: No file/file-path was provided to the function.' 
    # Wanted to try raise instead of return 
    if not os.path.exists(tickets): 
        raise FileNotFoundError ('Error: File does not exist') 
    if os.path.isdir(tickets): return 'File only points to a directory' 
    
    try: 
        open_ticket = count_open_tickets (tickets) 
        closed_tickets = count_closed_tickets (tickets) 
        high_priority_tickets = count_high_priority (tickets) 
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