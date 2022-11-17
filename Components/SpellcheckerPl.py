from rasa.nlu.components import Component

from symspellpy.symspellpy import SymSpell
from typing import List, Type


class SpellcheckerPl(Component):
    """A custom spell checking component"""
    name = "SpellcheckerPl"
    provides = ["text"]

    @classmethod
    def required_components(cls) -> List[Type[Component]]:
        """Specify which components need to be present in the pipeline."""
        return []

    defaults = {}
    language_list = None
    print('initialised the class')

    def __init__(self, component_config=None):
        super(SpellcheckerPl, self).__init__(component_config)
        self.processor = SymSpell(2)
        self.processor.load_dictionary('./sjp/pol_keywords.txt', term_index=1, count_index=0)

    def process(self, message, **kwargs):
        """Fix spelling and print given message."""

        suggestions = self.processor.lookup_compound(message.text, max_edit_distance=2, transfer_casing=True,
                                                     ignore_non_words=True)

        message.text = suggestions[0].term
        print(message.text)
