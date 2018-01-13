"""
For now, this contains a set of buttons which do different things.
"""

from evennia import DefaultObject
from commands.button import ButtonCmdSet
from commands.button import TeleSwitchCmdSet

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

        self.cmdset.add_default(ButtonCmdSet)


class TeleSwitch(BasicSwitch):
    """
    My idea is that this inherits the fatueres of the basic switch but
    specifically teleports the character pushing the button/switch to
    a destination. "destination" is settable by the builder.

    problem is, its the command set that needs to be different.
    """

    def at_object_creation(self):
        super(TeleSwitch, self).at_object_creation()

        # new features added
        # first create a property called destination
        self.cmdset.add_default(TeleSwitchCmdSet)


# not blank and end
