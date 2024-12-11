import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import Utility.CommonUtils as CommonUtils
from Utility.IntentMatching import yes_or_no


class FlightTicketBooking:
    def __init__(self):
        self.origin = ''
        self.destination = ''
        self.departure_time = ''

    def __str__(self):
        s = ''
        s += f"{'Origin':<20} {'Destination':<20} {'Departure Time':<15}\n"
        s += "-" * 55 + '\n'
        s += f"{self.origin:<20} {self.destination:<20} {self.departure_time:<15}\n"
        return s

    def process_flight_ticket_booking(self):
        """
        Main process of the ticket booking
        """
        self.data_collection()
        self.data_confirmation_and_correction()
        self.flight_search()
        self.provide_information()

    def data_collection(self):
        """
        Gather required inputs: origin, destination, and departure time.
        """
        # 1. origin
        FlightTicketBooking.generate_prompts('origin')
        self.origin = FlightTicketBooking.input_parsing('origin', input())

        # 2. destination
        FlightTicketBooking.generate_prompts('destination')
        self.destination = FlightTicketBooking.input_parsing('destination', input())

        # 3. departure time
        FlightTicketBooking.generate_prompts('departure_time')
        self.departure_time = FlightTicketBooking.input_parsing('departure_time', input())


    def data_confirmation_and_correction(self):
        """
        Confirm collected inputs with the user.
        """
        complete = False
        while not complete:
            print(self)
            print('This is your travel information. Is it correct? If not, which information you want to correct?')
            s = input()
            if yes_or_no(s):
                complete = True
                print('Ticket information confirmed.')
            else:
                if "origin" in s.lower():
                    print("Please input the origin")
                    self.origin = FlightTicketBooking.input_parsing('origin', input())
                elif "destination" in s.lower():
                    print("Please input the destination")
                    self.destination = FlightTicketBooking.input_parsing('destination', input())
                elif "date" in s.lower() or "time" in s.lower():
                    print("Please input the date")
                    self.departure_time = FlightTicketBooking.input_parsing('departure_time', input())
                else:
                    print("Correction detected, but field not specified.")

    def flight_search(self):
        """
        Once data is confirmed, the bot queries the Google Flights API to find available flights.
        """
        print("Start searching for flights...")
        # todo

    def provide_information(self):
        """
        1. let user choose the flight or go to data correction
        2. store the users trip
        3. ask if the user want to travel back next time he entered the system
        """
        # todo

    @staticmethod
    def input_parsing(keyword, res):
        """
        method to extract the key content from user's response
        """
        if keyword == 'origin':
            corpus = CommonUtils.get_corpus_from_file('../Data/corpus/answer_origin.data')
            return FlightTicketBooking.extract_target(corpus, res)
        elif keyword == 'destination':
            corpus = CommonUtils.get_corpus_from_file('../Data/corpus/answer_destination.data')
            return FlightTicketBooking.extract_target(corpus, res)
        elif keyword == 'departure_time':
            corpus = CommonUtils.get_corpus_from_file('../Data/corpus/answer_departure_time.data')
            return FlightTicketBooking.extract_target(corpus, res)

    @staticmethod
    def extract_target(corpus, res):
        pattern_with_placeholder = [pattern.replace("XXX", "(.*)").strip() for pattern in corpus]
        vectorizer = TfidfVectorizer()
        pattern_vectors = vectorizer.fit_transform(corpus)
        res_vector = vectorizer.transform([res])
        similarities = cosine_similarity(res_vector, pattern_vectors)
        best_pattern = pattern_with_placeholder[similarities.argmax()]

        match = re.search(best_pattern, res, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        else:
            return res

    @staticmethod
    def generate_prompts(keyword):
        """
        method to generate prompts for keyword
        """
        if keyword == 'origin':
            CommonUtils.randomly_get_from_file('../Data/corpus/ask_origin_corpus.data')
        elif keyword == 'destination':
            CommonUtils.randomly_get_from_file('../Data/corpus/ask_destination_corpus.data')
        elif keyword == 'departure_time':
            CommonUtils.randomly_get_from_file('../Data/corpus/ask_departure_time_corpus.data')
