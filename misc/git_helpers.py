from talon.voice import Context, Key

ctx = Context("githelpers")


keymap = {
    "jet lazy": ["git add --all && git commit -m 'update'"]
}

ctx.keymap(keymap)
