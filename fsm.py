from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'birth'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'give bone'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'feed'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'give fish'

    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == 'big'

    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == 'die'




    def on_enter_state1(self, update):
        update.message.reply_text("I'm an egg,please give bone or give fish to me")
        

    def on_enter_state2(self, update):
        update.message.reply_text("I'm a puppy,feed me")

    def on_enter_state3(self, update):
        update.message.reply_text("I'm dog")

    def on_enter_state4(self, update):
        update.message.reply_text("I'm a kitten,let me big")

    def on_enter_state5(self, update):
        update.message.reply_text("I'm a cat")

    def on_enter_state6(self, update):
        update.message.reply_text("I'm dead,birth me again")
        self.go_back(update)		
      
