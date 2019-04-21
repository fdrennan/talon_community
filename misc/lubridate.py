from talon.voice import Context, Key

ctx = Context("lubridate")
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
    "import blooper": ["library(lubridate)"],
    "blooper package": ["lubridate::"],
    "blooper as date time": ["as_datetime()", Key("left")],
    "blooper YMD": ["ymd", Key("tab")],
    "blooper NDY": ["mdy", Key("tab")],
    "blooper DMY": ["dmy", Key("tab")],
    "blooper YDM": ["ydm", Key("tab")],
    "blooper why queue": ["yq()", Key("left")],
    "blooper HMS": ["hms()", Key("left")],
    "blooper decimal": ["date_decimal()", Key("left")],
    "blooper now": ["now()", Key("left")],
    "blooper today": ["today()", Key("left")],
    "blooper strip time": ["fast_strptime()", Key("left")],
    "blooper parse date": ["parse_date_time()", Key("left")],
    "blooper as date": ["as_date()", Key("left")],
    "blooper as HMS": ["as.hms()", Key("left")],
    "blooper date": ["date()", Key("left")],
    "blooper year": ["year()", Key("left")],
    "blooper so": ["iso", Key("tab")],
    "blooper eppie": ["epi", Key("tab")],
    "blooper hour": ["hour()", Key("left")],
    "blooper minute": ["minute()", Key("left")],
    "blooper second": ["second()", Key("left")],
    "blooper semester": ["semester()", Key("left")],
    "blooper quarter": ["quarter()", Key("left")],
    "blooper am": ["am()", Key("left")],
    "blooper pea": ["pm()", Key("left")],
    "blooper leap": ["leap_year()", Key("left")],
    "blooper update": ["update()", Key("left")],
    "blooper floor": ["floor_date()", Key("left")],
    "blooper round": ["round_date()", Key("left")],
    "blooper ceiling": ["ceiling_date()", Key("left")],
    "blooper roll back": ["rollback()", Key("left")],
    "blooper zones": ["OlsonNames()"],
    "blooper with": ["with_tz()", Key("left")],
    "blooper force": ["force_tz()", Key("left")],
    "blooper day light": ["dst()"],
    "blooper stamp": ["stamp",Key("tab")],
    "blooper period year": ["years()",Key("left")]

}

ctx.keymap(keymap)
