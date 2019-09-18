from talon.voice import Context, Key

ctx = Context("pandas")


keymap = {
    "import pandas": ["import pandas as pd"],
    "pandas": ["pd."],
    "pandas call names": [".columns"],
    "pandas group by": [".groupby(['Animals'])"],
    "pandas summarise": [".agg({'column': 'function'})"],
    "pandas apply": [".agg({'column': 'function'})"],
    "pandas eye": [".iloc[]", Key("left")]


}

ctx.keymap(keymap)
