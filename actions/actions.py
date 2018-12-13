from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionGetPokemonType(Action):
	def name(self):
		return "action_get_pokemon_type"
	
	def run(self, dispatcher, tracker, domain):
		pokemon_name = tracker.get_slot('pokemon')
		result = "%s is a psychic type Pokemon." % (pokemon_name)
		
		dispatcher.utter_message(result)
		return []