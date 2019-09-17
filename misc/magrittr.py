from talon.voice import Context, Key

ctx = Context("magrittr")
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
    "import mage": ["library(magrittr)"],
    "mage package": ["magrittr::"],
    "mage explode": [" %$% ", Key("enter")],
    "mage extract": ["extract()", Key("left")],
    "mage dub extract": ["extract2()", Key("left")],
    "mage in set": ["inset()", Key("left")],
    "mage dub in set": ["inset2()", Key("left")],
    "mage use series": ["use_series()", Key("left")],
    "mage add": ["add()", Key("left")],
    "mage subtract": ["subtract()", Key("left")],
    "mage multiply": ["multiply_by()", Key("left")],
    "mage raise": ["raise_to_power()", Key("left")],
    "mage matrix": ["multiply_by_matrix()", Key("left")],
    "mage divide": ["divide_by()", Key("left")],
    "mage integer": ["divide_by_int()", Key("left")],
    "mage mod": ["mod()", Key("left")],
    "mage is": ["is_in()", Key("left")],
    "mage and": ["and()", Key("left")],
    "mage or": ["or()", Key("left")],
    "mage equals": ["equals()", Key("left")],
    "mage great": ["is_greater_than()", Key("left")],
    "mage weak great": ["is_weakly_greater_than()", Key("left")],
    "mage less": ["is_less_than()", Key("left")],
    "mage weak less": ["is_weakly_less_than()", Key("left")],
    "mage not": ["not()", Key("left")]

}

ctx.keymap(keymap)
