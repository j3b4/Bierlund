"""
Defines the basic commands on a switch or buttons
"""

from evennia import Command, CmdSet


class CmdPush(Command):
    """
    Push the button. See what happens.

    Usage:
        push button

    Alias:
        pb

    This will depress the button.  Then you'll find out what
    happens next. 
    """

    key = "push button"
    aliases = ["push", "switch", "activate", "pb"]


    def func(self):
        """
        activate the button
        need to be able to customize the actual effect.
        or at least create a library of effects builders can use
        like "teleport buttons" with a customizable teleport destination.

        """
        self.caller.msg("You did it! You pushed the button.")

# -----------------
# Command Set
# -----------------

class ButtonCmdSet(CmdSet):

    key = "ButtonCommands"
    mergetype = "Union"

    def at_cmdset_creation(self):
        self.add(CmdPush())
