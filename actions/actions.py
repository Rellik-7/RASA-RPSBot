# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import random
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionPlayRPS(Action):

    def name(self) -> Text:
        return "action_play_rps"

    def bot_choice(self):
        generated = random.randint(1,3)
        if generated == 1:
            botchoice = 'rock'
        elif generated == 2:
            botchoice = 'paper'
        elif generated == 3:
            botchoice = 'scissor'

        return(botchoice)



    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_choice = tracker.get_slot("choice")
        dispatcher.utter_message(text=f"You chose {user_choice}")

        bot_choice = self.bot_choice()
        dispatcher.utter_message(text=f"Bot chose {bot_choice}")

        if user_choice == "rock" and bot_choice == "scissor":
            dispatcher.utter_message(text="Congrats, you won!")
        elif user_choice == "rock" and bot_choice == "paper":
            dispatcher.utter_message(text="The computer won this round.")
        elif user_choice == "paper" and bot_choice == "rock":
            dispatcher.utter_message(text="Congrats, you won!")
        elif user_choice == "paper" and bot_choice == "scissor":
            dispatcher.utter_message(text="The computer won this round.")
        elif user_choice == "scissor" and bot_choice == "paper":
            dispatcher.utter_message(text="Congrats, you won!")
        elif user_choice == "scissor" and bot_choice == "rock":
            dispatcher.utter_message(text="The computer won this round.")
        else:
            dispatcher.utter_message(text="It was a tie!")

        return []
