from talon.voice import Context, Key

ctx = Context("stringr")
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
    "import stringer": ["library(stringr)"],
    "stringer package": ["stringr::"],

    "stringer detect": ["str_detect()", Key("left")],
    "stringer which": ["str_which()", Key("left")],
    "stringer count": ["str_count()", Key("left")],
    "stringer locate": ["str_locate()", Key("left")],
    "stringer locate all": ["str_locate_all()", Key("left")],
    "stringer sub": ["str_sub()", Key("left")],
    "stringer subset": ["str_subset()", Key("left")],
    "stringer extract": ["str_extract()", Key("left")],
    "stringer extract all": ["str_extract_all()", Key("left")],
    "stringer match": ["str_match()", Key("left")],
    "stringer match all": ["str_match_all()", Key("left")],
    "stringer length": ["str_length()", Key("left")],
    "stringer pad": ["str_pad()", Key("left")],
    "stringer trunk": ["str_trunc()", Key("left")],
    "stringer trim": ["str_trim()", Key("left")],
    "stringer replace": ["str_replace()", Key("left")],
    "stringer replace all": ["str_replace_all()", Key("left")],
    "stringer to upper": ["str_to_upper()", Key("left")],
    "stringer to lower": ["str_to_lower()", Key("left")],
    "stringer to title": ["str_to_title()", Key("left")],
    "stringer cat": ["str_c()", Key("left")],
    "stringer dupe": ["str_dup()", Key("left")],
    "stringer split fixed": ["str_split_fixed()", Key("left")],
    "stringer glue": ["str_glue()", Key("left")],
    "stringer glue data": ["str_glue_data()", Key("left")],
    "stringer order": ["str_order()", Key("left")],
    "stringer sort": ["str_sort()", Key("left")],
    "stringer convert": ["str_conv()", Key("left")],
    "stringer view": ["str_view()", Key("left")],
    "stringer view all": ["str_view_all()", Key("left")],
    "stringer wrap": ["str_wrap()", Key("left")]

}

ctx.keymap(keymap)
