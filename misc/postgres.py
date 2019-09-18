from talon.voice import Context, Key

ctx = Context("postgres")

keymap = {
    "posty create dex": ["create index __ on something(salary)"]
}

ctx.keymap(keymap)
