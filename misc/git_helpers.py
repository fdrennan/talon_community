from talon.voice import Context, Key

ctx = Context("githelpers")


keymap = {
    "jet lazy commit": ["git add --all && git commit -m 'update'"],
    "jet lazy push": ["git push origin master"],
    "jet lazy pull": ["git pull origin master"],
}

ctx.keymap(keymap)
