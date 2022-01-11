'''Simple Spaced Repetition'''

import inspect as _inspect
from pathlib import Path as _Path
from vinca._cardlist import Cardlist as _Cardlist
from vinca._card import Card as _Card
from vinca._config import config as _config
from vinca._generators import generators_dict as _generators_dict
from vinca._tag_caching import tags_cache as _tags_cache

# load the card generators into the module
for _hotkey, _generator_func in _generators_dict.items():
	globals()[_generator_func.__name__] = _generator_func
	globals()[_hotkey] = _generator_func

# create a collection (cardlist) out of all the cards
col = collection = _Cardlist.from_directory(_config.cards_path)
# import all the methods of the collection object directly into the module's namespace
# this is so that ```vinca col filter``` can be written more shortly as ```vinca filter```
for _method_name, _method in _inspect.getmembers(col):
	if _method_name == '__getitem__':
		continue
	if _method_name.startswith('_'):
		continue
	globals()[_method_name] = _method

# create a few utility collections
# by writing them as lambda functions they are only evaluated if I need them
new = lambda: col.filter(new= True)
new.__doc__ = 'Your new cards'
deleted = lambda: col.filter(deleted= True)
deleted.__doc__ = 'Your deleted cards'
due = lambda: col.filter(due= True)
due.__doc__ = 'Your due cards'
recent = rs  = lambda: col.sort('seen')
recent.__doc__ = 'Your cards sorted with the most recently seen ones at the top.'
recent_created = rc = lambda: col.sort('created')
recent_created.__doc__ = 'Your cards sorted with the most recently created ones at the top.'

# utility functions
version = 120
globals()['-v'] = globals()['--version'] = version
help = '''\
vinca --help              general help
vinca filter --help       help on a specific subcommand
man vinca                 vinca tutorial
vinca online_help	  online man page'''
online_help = 'https://oscarlaird.github.io/vinca-SRS/vinca.1.html'
about = '''
                               ┌─────────────┐
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┥ ABOUT VINCA ┝━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                              └─────────────┘                              ┃
┃  Who is vinca for?                                                        ┃
┃  • The student who wants to remember.                                     ┃
┃                                                                           ┃
┃  What is vinca for?                                                       ┃
┃  • Books (semantic knowledge)                                             ┃
┃  • Poetry (verbal knowledge)                                              ┃
┃                                                                           ┃
┃  What does vinca mean?                                                    ┃
┃  • The vi inspired card application                                       ┃
┃  • A scrambled portmanteau of vi and Anki                                 ┃
┃  • A binding plant; a chain: for the memory and the student.              ┃
┃                                                                           ┃
┃  Why is Anki better than vinca?                                           ┃
┃  • Anki is better for anyone beginning with spaced repetition.            ┃
┃  • Anki has a GUI, addons, and a large community.                         ┃
┃  • Anki represents cards as html and can incorporate images, latex, &c.   ┃
┃                                                                           ┃
┃  Support                                                                  ┃
┃  • olaird25@gmail.com                                                     ┃
┃                                                                           ┃
┃  Read the tutorial! Consult man vinca.                                    ┃
┃                                                                           ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
'''

# quick reference to the most recent card
_lcp = _config.last_card_path
_lcp_exists = isinstance(_lcp, _Path) and _lcp.exists()
lc = last_card = _Card(path = _lcp) if _lcp_exists else 'no last card'

# move config.set_cards_path into globals
set_cards_path = set_path = scp = _config.set_cards_path
cards_path = path = cp = _config.cards_path

class Advanced:
	''' A set of rarely used advanced commands '''
	def update_tags(self):
		tags = collection.tags
		_tags_cache.update(tags)
		return tags

'''
Add the following code to the ActionGroup object in helptext.py of fire to get proper aliasing
A better way would be to go back further into the code and check if two functions share the same id

  def Add(self, name, member=None):
    if member and member in self.members:
      dupe = self.members.index(member)
      self.names[dupe] += ', ' + name
      return
    self.names.append(name)
    self.members.append(member)
'''
'''
Make this substitution on line 458 of core.py to allow other iterables to be accessed by index

    # is_sequence = isinstance(component, (list, tuple))
    is_sequence = hasattr(component, '__getitem__') and not hasattr(component, 'values')
'''
'''
And make a corresponding change in generating the help message

  is_sequence = hasattr(component, '__getitem__') and not hasattr(component, values)
  # if isinstance(component, (list, tuple)) and component:
  if is_sequence and component:
'''
