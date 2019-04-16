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
    "deplyr package": ["dplyr::"],
    "deplyr filter": ["filter()", Key("left"), Key("enter")],
    "deplyr mutate": ["mutate()", Key("left"), Key("enter")],
    "deplyr select": ["select()", Key("left"), Key("enter")],
    "deplyr summarize": ["summarise()", Key("left"), Key("enter")],
    "deplyr rename": ["rename()", Key("left"), Key("enter")],
    "deplyr group by": ["group_by()", Key("left"), Key("enter")],

    "deplyr filter if": ["filter_if()", Key("left"), Key("enter")],
    "deplyr mutate if": ["mutate_if()", Key("left"), Key("enter")],
    "deplyr select if": ["select_if()", Key("left"), Key("enter")],
    "deplyr summarize if": ["summarise_if()", Key("left"), Key("enter")],
    "deplyr rename if": ["rename_if()", Key("left"), Key("enter")],
    "deplyr group by if": ["group_by_if()", Key("left"), Key("enter")],

    "deplyr filter at": ["filter_at()", Key("left"), Key("enter")],
    "deplyr mutate at": ["mutate_at()", Key("left"), Key("enter")],
    "deplyr select at": ["select_at()", Key("left"), Key("enter")],
    "deplyr summarize at": ["summarise_at()", Key("left"), Key("enter")],
    "deplyr rename at": ["rename_at()", Key("left"), Key("enter")],
    "deplyr group at": ["group_by_at()", Key("left"), Key("enter")],

    "deplyr filter all": ["filter_all()", Key("left"), Key("enter")],
    "deplyr mutate all": ["mutate_all()", Key("left"), Key("enter")],
    "deplyr select all": ["select_all()", Key("left"), Key("enter")],
    "deplyr summarize all": ["summarise_all()", Key("left"), Key("enter")],
    "deplyr rename all": ["rename_all()", Key("left"), Key("enter")],
    "deplyr group by all": ["group_by_all()", Key("left"), Key("enter")],

    "reader right": ["write_"],
    "reader read": ["read_"]
}

ctx.keymap(keymap)
