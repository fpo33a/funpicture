# tested with python 3.7
# just write name binary representation around picture, in chronological order from top left

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

#--------------------------------------
# get an array of bits of a value ( letter of name in int ascii value )
def get_binary_array (value):
  binary_array = []
  binary_string=""
  for x in reversed(range(8)):
    pow2=2**x
    res=value&pow2
    if (res > 0):
      binary_string=binary_string+"1"
      binary_array.append (1)
    else:
      binary_string=binary_string+"0"
      binary_array.append (0)

  print ("bs: ", binary_string)
  return binary_array

bin_u = get_binary_array (117)
print ("u (117) = ",bin_u)
bin_a = get_binary_array (65)
print ("a (65) = ",bin_a)

#--------------------------------------

# load base image ( picture modified via https://photofunia.com/effects/sketch )
im = Image.open('source.jpg')


# Create figure and axes
fig, ax = plt.subplots()

# Display the image
ax.imshow(im)

# set image offset and "bit" rectangle size
small_rect_hoffset=15
small_rect_voffset=0
small_rect_width=10
small_rect_height=10
small_rect_height_1=10
small_rect_height_0=5

# the name we want to render
data_string = "FrankPolet"

# initialize range and position values
char_position=0
start=0
stop=8
step=1
direction="horizontal"

# loop on all characters of thte data string
for char in data_string:
  bin_val = get_binary_array (ord(char))
  index=0
  for bit in range(start,stop,step):
    if bin_val[bit] == 1:
      if direction=="horizontal":
        x=small_rect_hoffset+(index*(small_rect_width+5))
        y=small_rect_voffset
      else:
        x=small_rect_hoffset
        y=small_rect_voffset+(index*(small_rect_height+5))
      print (char," ",ord(char),"1 x= ",x," y=",y)
      rect = patches.Rectangle((x, y), small_rect_width, small_rect_height_1, linewidth=1, edgecolor='grey', facecolor='grey')
    else:
      if direction=="horizontal":
        x=small_rect_hoffset+(index*(small_rect_width+5))
        y=small_rect_voffset+(small_rect_height_1-small_rect_height_0)
      else:
        x=small_rect_hoffset
        y=small_rect_voffset+(index*(small_rect_height+5))
      print (char," ",ord(char),"0 x= ",x," y=",y)
      rect = patches.Rectangle((x, y), small_rect_width, small_rect_height_0, linewidth=1, edgecolor='grey', facecolor='grey')
    # Add the patch to the Axes
    ax.add_patch(rect)
    index=index+1
  char_position=char_position+1
  # two first characters on top, from left to right
  if char_position <= 2:
    small_rect_hoffset = x+(small_rect_width+5)
  # next three characters vertically, from top to bottom
  if char_position >= 2 and char_position <= 5:
    direction="vertical"
    small_rect_voffset = y+(small_rect_height+5)
  # two next characters on bottom, from right to left
  if char_position >= 5 and char_position < 7:
    direction="horizontal"
    start=7
    stop=-1
    step=-1
    small_rect_hoffset = small_rect_hoffset - (8 *(small_rect_width+5) )
  # next three characters vertically, from bottom to top
  if char_position >= 7 and char_position < 10:
    direction="vertical"
    start=7
    stop=-1
    step=-1
    small_rect_hoffset=0
    small_rect_voffset=small_rect_voffset - (8 *(small_rect_height+5) )

# remove axis
plt.axis('off')
# show result
plt.show()
# save result to file
fig.savefig('fp-nb.png')