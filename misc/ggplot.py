from talon.voice import Context, Key

ctx = Context("ggplot")
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
    "library GG plot": ['library(ggplot', Key("right"), Key("enter")],
    "GG plot": ["ggplot() +", Key("enter")],
    "GG aesthetics": ["aes() +", Key("left"), Key("left"), Key("left")],
    "geom line": ["geom_line()", Key("left")]
}

ctx.keymap(keymap)
