def ticket_check(ticket):
    if len(ticket) != 6 or not ticket.isdigit():
        print('Enter the correct ticket number!')
    else:
        first_part = ticket[:3]
        second_part = ticket[3:]

        first_sum = int(first_part[0]) + int(first_part[1]) + int(first_part[2])
        second_sum = int(second_part[0]) + int(second_part[1]) + int(second_part[2])

        if first_sum == second_sum:
            print('Lucky')
        else:
            print('Normal')


if __name__ == '__main__':
    ticket = input('Enter the ticket number: ')
    ticket_check(ticket)