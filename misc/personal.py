from talon.voice import Context, Key

ctx = Context("personal")
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
    "jeera": ["JIRA"],
    "our site": ["drenr.com"],
    "sequel": ["SQL"],
    "jet pole": ["git pull "],
    "our double down": [Key("down"), Key("down")],
    "prog our": ["R"],
    "our pipe": [Key("cmd-shift-m"), Key("enter")],
    "our pipe line": [Key("cmd-right"), Key("cmd-shift-m"), Key("enter")],
    "our chunk": ["```{r, message=FALSE, warning=FALSE}", Key("enter"), Key("enter"), "```", Key("up")],
    "pie chunk": ["```{python}", Key("enter"), Key("enter"), "```", Key("up")],
    "our pat": [Key("space"), "<-", Key("enter")],
    "curly bracket": ["{}", Key("left"), Key("enter")],

}

ctx.keymap(keymap)
