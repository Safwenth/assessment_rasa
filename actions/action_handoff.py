from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHandoff(Action):
    def name(self) -> Text:
       return "action_handoff"
 
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
       # Add logic here for the confirm_recap
       dispatcher.utter_message(response="utter_more_help_needed_handoff_pattern")
       # Add API to human connection / MCP for tool running ..

       return []