import sys

sys.path.append('../Utility')

from Utility.CommonUtils import DatabaseUtils
from Utility import IdentityMatching, IntentMatching
import FlightTicketBooking
import QandA

print('---------Welcome to ChatGRP---------')
IdentityMatching.identity_matching()
while True:
    s = input()
    name = DatabaseUtils.get_last_visit_user()
    intent = IntentMatching.get_intent(s)
    if intent == 'greeting':
        print(f'Hi {name}, what can I do for you?')
    elif intent == 'id_matching':
        print(f'Yes! Your name is {name}!')
    elif intent == 'what_can_you_do':
        print('I can do small talking, remember your name, help you book a flight ticket, and also Q&A !')
    elif intent == 'Flight':
        FlightTicketBooking.FlightTicketBooking().process_flight_ticket_booking()
    elif intent == 'Small_talk':
        print('As long as you are using me, it is my good day!')
    elif intent == 'Q&A':
        QandA.process_with_user_said(s)
    else:
        print('I don\'t understand what you say, can you restate that?')
