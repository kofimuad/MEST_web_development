class Chat:
    # Properties are qualities that a class would have
    # Methods are the behavior
    def __init__(self):
        self.chatee = input("Who the fuck are you chatting with?\n")
        self.last_message = input("What was your last message?\n")
        self.last_message_time =  input("When was the last message sent?\n")

        # The constructor __init__ is used to specify the properties that a class has.


    def __str__(self):
        return f"---> You're chatting with {self.chatee} about {self.last_message} at {self.last_message_time}"


    def open(self):
        return f"You just opened the chat with {self.chatee} with last message {self
        .last_message} that was sent at {self.last_message_time}"
    
class Gifty:
    

