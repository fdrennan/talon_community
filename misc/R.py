from talon.voice import Context, Key

ctx = Context("R")
#  this is a mapping for scrolling and other mouse utilities
#
# keymap = {

#     # scrolling
#     "scroll down": [Key("down")] * 30,
#     "scroll up": [Key("up")] * 30,
#     # NB home and end do not work in all apps
#     "(scroll way down | doomway)": Key("cmd-down"),
#     "(scroll way up | jeepway)": Key("cmd-up"),
#     "page up": [Key("pageup")],
#     "page down": [Key("pagedown")],
#     # searching
#     "(search | marco)": Key("cmd-f"),
#     "marneck": Key("cmd-g"),
#     "marpreev": Key("cmd-shift-g"),
#     "marthis": [Key("alt-right"), Key("shift-alt-left"), Key("cmd-f"), Key("enter")],
# }

keymap = {
    "our new script": [Key('cmd-shift-n')],
    "focus code": [Key('ctrl-1')],
    "focus console": [Key('ctrl-2')],
    "focus terminal": [Key('alt-shift-t')],

    "show history": [Key('cmd-up')],
    "clear console": [Key('ctrl-l')],
    "restart our session": [Key('ctrl-shift-f10')],

    "our run": [Key('ctrl-enter')],
    "our source": [Key('ctrl-enter')],
    "our comment": [Key('ctrl-shift-c')],
    "run above": [Key('alt-cmd-p')],
    "run chunk": [Key('cmd-shift-enter')],

    "our calm head": ["head()", Key("left")],
    "our calm call names": ["colnames()", Key("left")],
    "our calm some": ["sum()", Key("left")],
    "our calm deeput": ["dput()", Key("left")],
    "ourqual": [" = "],
    "ourdubqual": [" == "],
    "in a": ["na"],
    "are studio": ["rstudio"]

}

ctx.keymap(keymap)
