
from talon.voice import Context, Key

ctx = Context("recipes")
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
    "import cake": ['library(recipies)', Key("enter")],
    "cake package": ["recipes::"],
    "cake start": ["recipe()", Key("left")],
    "cake step": ["step_"],
    "cake all": ["all_"],
    "cake add": ["add_"],
    "cake prep": ["prep()"],
    "cake bake": ["bake()"],
    "cake check": ["check"],
}

ctx.keymap(keymap)
