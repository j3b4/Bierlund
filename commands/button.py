"""
Defines the basic commands on a switch or buttons
"""

from evennia import Command, CmdSet
from evennia import default_cmds


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
        button = self.obj
        self.caller.msg("You did it! You pushed the %s." % button.key)


class CmdTelePush(Command):
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
        button = self.obj
        destination = button.db.telink
        if not destination:
            return
        else:
            room = self.caller.location
            self.caller.msg("You did it! You pushed the %s" % button.key)
            room.msg_contents("%s pushes the button." % self.caller)
            self.caller.msg("You get moved to a new place!")
            room.msg_contents("%s disapears from view!" % self.caller)
            self.caller.move_to(destination)


class CmdTeleLink(default_cmds.MuxCommand):
    """
    Links a teleport button to a particular destination.

    Usage:
        telelink <button> = <destination>
        telelink <button>

    Aliases:
        tlink, tl
    """

    key = "telelink"
    aliases = ["tlink", "tl"]
    locks = "cmd:perm(link) or perm(Builder)"
    help_category = "Building"

    def func(self):
        self.caller.msg("You used telelink")
        caller = self.caller

        if not self.args:
            caller.msg("Usage: telelink <object> = <target>")
            return

        object_name = self.lhs

        # get object
        obj = caller.search(object_name, global_search=True)
        if not obj:
            return

        #
        # this is messed up bc it will try to link other obj in room

        if self.rhs:
            # this means target supplied
            target = caller.search(self.rhs, global_search=True)
            if not target:
                return

            string = ""
            obj.db.telink = target
            string += "Pushing %s will teleport player to %s" % (
                obj.name, target.name)

        elif self.rhs is None:
            dest = obj.db.telink
            if dest:
                string = "%s teleports players to %s" % (obj.name,
                                                         dest.name)
            else:
                string = "%s is not linked to teleport anywhere." % obj.name

        caller.msg(string.strip())


# -----------------
# Command Sets
# -----------------


class ButtonCmdSet(CmdSet):

    key = "ButtonCommands"
    mergetype = "Union"

    def at_cmdset_creation(self):
        self.add(CmdPush())


class TeleSwitchCmdSet(CmdSet):
    """
    Command set that teleports the button pusher to the button's destination
    """
    key = "TeleSwitchCommands"
    mergetype = "Union"

    def at_cmdset_creation(self):
        self.add(CmdTelePush())
        self.add(CmdTeleLink())
    pass
