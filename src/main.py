
from htmlnode import *
from textnode import *
from function.text_extract_links import *

text = "you can see how cute is my rocky ![A dog sleeping](./'my dog sleeping'.png) ![my dog running](./'dog_running'.png)"
image1 = ("a dog sleeping", "./'my dog sleeping'.png")
image2 = ("my dog running", "./'dog_running'.png")
list_of_images = extract_markdown_images(text)
print(list_of_images)

