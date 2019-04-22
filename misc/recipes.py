
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
    "import pie": ['library(recipies)', Key("enter")],
    "pie package": ["recipes::"],
    "pie start": ["recipe()", Key("left")],
    "pie step": ["step_"],
    "pie all": ["all_"],
    "pie add": ["add_"],
    "pie prep": ["prep()"],
    "pie bake": ["bake()"],
    "pie check": ["check"],
}

ctx.keymap(keymap)
