from talon.voice import Context, Key

ctx = Context("dplyr")
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
    "tidy filter": ["filter()", Key("left"), Key("enter")],
    "tidy mutate": ["mutate()", Key("left"), Key("enter")],
    "tidy select": ["select()", Key("left"), Key("enter")],
    "tidy summarize": ["summarise()", Key("left"), Key("enter")],
    "tidy rename": ["rename()", Key("left"), Key("enter")],
    "tidy group by": ["group_by()", Key("left"), Key("enter")],

    "tidy filter if": ["filter_if()", Key("left"), Key("enter")],
    "tidy mutate if": ["mutate_if()", Key("left"), Key("enter")],
    "tidy select if": ["select_if()", Key("left"), Key("enter")],
    "tidy summarize if": ["summarise_if()", Key("left"), Key("enter")],
    "tidy rename if": ["rename_if()", Key("left"), Key("enter")],
    "tidy group by if": ["group_by_if()", Key("left"), Key("enter")],

    "tidy filter at": ["filter_at()", Key("left"), Key("enter")],
    "tidy mutate at": ["mutate_at()", Key("left"), Key("enter")],
    "tidy select at": ["select_at()", Key("left"), Key("enter")],
    "tidy summarize at": ["summarise_at()", Key("left"), Key("enter")],
    "tidy rename at": ["rename_at()", Key("left"), Key("enter")],
    "tidy group at": ["group_by_at()", Key("left"), Key("enter")],

    "tidy filter all": ["filter_all()", Key("left"), Key("enter")],
    "tidy mutate all": ["mutate_all()", Key("left"), Key("enter")],
    "tidy select all": ["select_all()", Key("left"), Key("enter")],
    "tidy summarize all": ["summarise_all()", Key("left"), Key("enter")],
    "tidy rename all": ["rename_all()", Key("left"), Key("enter")],
    "tidy group by all": ["group_by_all()", Key("left"), Key("enter")],
}

ctx.keymap(keymap)
