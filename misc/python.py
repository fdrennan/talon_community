from talon.voice import Context, Key

ctx = Context("python")
#  this is a mapping for scrolling and other mouse utilities

keymap = {
    "import none pie": ["import numpy as np"],
    "none pie": ["np."],
    "import pandas": ["import pandas as pd"],
    "pandas": ["pd."],
    "import mat plot": ["import matplotlib.pyplot as plt"],
    "mat plot": ["plt."],
    "pandas call names": [".columns"],
    "pandas group by": [".groupby(['Animals'])"],
    "pandas summarise": [".agg({'column': 'function'})"],
    "pandas apply": [".agg({'column': 'function'})"]
}

ctx.keymap(keymap)
