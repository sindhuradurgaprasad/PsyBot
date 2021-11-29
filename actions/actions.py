# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import builtins
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         print("I am Rasa built Imposter Syndrome chatbot")
         dispatcher.utter_message(text="Hello!")

         return []

class ActionService(Action):

    def name(self) -> Text:
        return "action_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        buttons=[
           {"payload":'/yesQuiz{"quiz_selection":"yes"}', "title":"Yeah "},
           {"payload":'/noQuiz{"quiz_selection":"no"}', "title":"I understand now / I know  about it"}
        ]
        dispatcher.utter_message(text="Firstly, would you consider yourself to be suffering or have you ever suffered from impostor syndrome?If you need help to answer this question, why not take this small test", buttons=buttons)

        return []
