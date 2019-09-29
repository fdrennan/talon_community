from talon.voice import Context, Key

ctx = Context("plumber")


keymap = {
    "plumbr new": ["#' @", Key("tab")]

}

ctx.keymap(keymap)
