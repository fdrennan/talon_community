from talon.voice import Context, Key

ctx = Context("python")
#  this is a mapping for scrolling and other mouse utilities

keymap = {
    "import none pie": ["import numpy as np"],
    "none pie": ["np."],
    "import pandas": ["import pandas as pd"],
    "pandas": ["pd."],
    "import mat plot": ["import matplotlib.pyplot as plt"],
    "mat plot": ["plt."]
}

ctx.keymap(keymap)
