from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'dialogues.txt')).read()

mask = np.array(Image.open(path.join(d, "images/steve_jobs.jpeg")))
stopwords = set(STOPWORDS)

wc = WordCloud(width=1000, height=600, background_color="black", max_words=2000, mask=mask,
               stopwords=stopwords, max_font_size=90, random_state=42)
# generate word cloud
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(mask)

# show
# fig, axes = plt.subplots(1, 3)
# axes[0].imshow(wc, interpolation="bilinear")
# # recolor wordcloud and show
# # we could also give color_func=image_colors directly in the constructor
# axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
# axes[2].imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
# for ax in axes:
#     ax.set_axis_off()
# plt.show()

plt.figure(figsize=[7,7])
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
_=plt.show()