from talon.voice import Context, Key

ctx = Context("githelpers")


keymap = {
    "jet lazy": ["git add --all", Key("enter"), ["git commit -m 'update'"], Key("enter")]
}

ctx.keymap(keymap)
