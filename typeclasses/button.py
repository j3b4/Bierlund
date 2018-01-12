"""
This is a basic button or switch object. It has a single command in its cmdset
if a character activates that command a single effect takes place.
"""

from evennia import DefaultObject

# 
# Definition of the button
#


class BasicSwitch(DefaultObject):
    """
    This is a basic button or switch object. It has a single command in its
    cmdset if a character activates that command a single effect takes place.
    """

    def at_object_creation(self):
        """
        This function is called when creating a switch
        """

    desc = "A basic switch or button"
    desc += "You can \"push\" it."
    self.db.desc = desc

    # Might be lockable

    self.db.locked = False

    self.cmdset.add_default(CmdSetSwitch)


