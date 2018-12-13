from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionGetPokemonType(Action):
	def name(self):
		return "action_get_pokemon_type"
	
	def run(self, dispatcher, tracker, domain):
		pokemon = tracker.get_slot('POKEMON')
		result = "%s is a psychic type Pokemon." % (pokemon)
		
		dispatcher.utter_message(result)
		return []