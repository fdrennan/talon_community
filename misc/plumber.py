from talon.voice import Context, Key

ctx = Context("plumber")


keymap = {
    "plumper new": ["#' @", Key("tab")],
    "plumper import": ["#' @import from", Key("tab")]
}

ctx.keymap(keymap)
