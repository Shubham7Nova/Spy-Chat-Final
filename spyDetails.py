#importing datetime library for using date and time in code.
from datetime import datetime

#Declaring Spy class.Every spy (user) and his/her friends(other spies) will be objects of this class.
class Spy:
       def __init__(self,name,salutation,age,rating):
              self.name = name
              self.salutation = salutation
              self.age = age
              self.rating = rating
              self.availability = True
              self.chats = []
              self.current_status_message = None
#Variable for managing average words.
              self.average_words = 0
#Variable for managing the total messages sent for calculating average.
              self.total_messages_sent = 0

#Class for making each message an object and adding time to it.
class ChatMessage:
       def __init__(self,message,sent_by_me):
              self.message = message
              self.time = datetime.now()
              self.sent_by_me = sent_by_me

#Default spy details as object of Spy class
spy = Spy('Bond','Mr.',24,4.7)

#Adding default friends
friend_one = Spy('Jane', 'Ms.', 4.9, 27)
friend_two = Spy('Catelyn', 'Ms.', 4.39, 21)
friend_three = Spy('X', 'Dr.', 4.95, 37)

#List for maintaing a spy's friends.
friends = [friend_one, friend_two, friend_three]


