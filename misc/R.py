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

    "our view": ["View()", Key("left")],
    "our glimpse": ["glimpse()", Key("left")],
    "deplyr glimpse": ["glimpse()", Key("left")],

    "our new script": [Key('cmd-shift-n')],
    "focus code": [Key('ctrl-1')],
    "focus code only": [Key('ctrl-shift-1')],
    "focus console": [Key('ctrl-2')],
    "focus console only": [Key('ctrl-shift-2')],
    "focus term": [Key('alt-shift-t')],
    "focus all": [Key('ctrl-shift-0')],

    "focus code full": [Key('shift-ctrl-1')],
    "focus console full": [Key('shift-ctrl-2')],

    "show history": [Key('cmd-up')],
    "clear console": [Key('ctrl-l')],
    "restart our session": [Key('ctrl-shift-f10')],
    "our next": [Key('cmd-right'), ",", Key("enter")],
    "our down": [Key('cmd-right'),  Key("enter")],
    "our line": [Key('alt-enter')],
    "our run": [Key('ctrl-enter')],
    "our source": [Key('ctrl-enter')],
    "our comment": [Key('ctrl-shift-c')],
    "run above": [Key('alt-cmd-p')],
    "run chunk": [Key('cmd-shift-enter')],
    "our dim": ["dim()", Key("left")],
    "our head": ["head()", Key("left")],
    "our call names": ["colnames()", Key("left")],
    "our deeput": ["dput()", Key("left")],
    "ourqual": [" = "],
    "ourdubqual": [" == "],
    "in a": ["na"],
    "are studio": ["rstudio"],
    "pasta oh": ["paste0()", Key("left")],
    "pasta": ["paste()", Key("left")],

    "our structure": ["str()", Key("left")],
    "our class": ["class()", Key("left")],
    "our install": ["install.packages()", Key("left")],
    "our library": ["library()", Key("left")],
    "our data": ["data()", Key("left")],
    "our get": ["getwd()", Key("left")],
    "our set": ["setwd()", Key("left")],
    "our cat": ["c()", Key("left")],
    "our sequence": ["seq()", Key("left")],
    "our repeat": ["rep()", Key("left")],
    "our sort": ["sort()", Key("left")],
    "our table": ["table()", Key("left")],
    "our reverse": ["rev()", Key("left")],
    "our unique": ["unique()", Key("left")],
    "our for": ["for () {}",Key("left"),Key("enter"), Key("left"), Key("left"), Key("left"), Key("left"), Key("left")],
    "our while": ["while () {}", Key("left"),Key("enter"), Key("left"), Key("left"), Key("left"), Key("left"), Key("left")],
    "our if": ["if () {}", Key("left"),Key("enter"), Key("left"), Key("left"), Key("left"), Key("left"), Key("left")],
    "our else if": [" else if () {}", Key("left"),Key("enter"), Key("left"),Key("left"), Key("left"), Key("left"), Key("left")],
    "our else": [" else {}", Key("left"),Key("enter")],
    "our function": [" function(){}", Key("left"),Key("enter"), Key("left"), Key("left"), Key("left"),  Key("left"), Key("left")],
    "our as logical": ["as.logical()", Key("left")],
    "our as character": ["as.character()", Key("left")],
    "our as numeric": ["as.numeric()", Key("left")],
    "our as factor": ["as.factor()", Key("left")],
    "our log": ["log()", Key("left")],
    "our sum": ["sum()", Key("left")],
    "our exponent": ["exp()", Key("left")],
    "our mean": ["mean()", Key("left")],
    "our max": ["max()", Key("left")],
    "our median": ["median()", Key("left")],
    "our min": ["min()", Key("left")],
    "our quantile": ["quantile()", Key("left")],
    "our round": ["round()", Key("left")],
    "our rank": ["rank()", Key("left")],
    "our variance": ["var()", Key("left")],
    "our var": ["var()", Key("left")],
    "our correlation": ["cor()", Key("left")],
    "our SD": ["sd()", Key("left")],
    "our standard": ["sd()", Key("left")],
    "our list environment": ["ls()", Key("left")],
    "our LS": ["ls()", Key("left")],
    "our remove": ["rm()", Key("left")],
    "our remove all": ["rm(list = ls())"],
    "our assign": [" <- "],
    "our assign line": [" <- ", Key("enter")]

}

ctx.keymap(keymap)
