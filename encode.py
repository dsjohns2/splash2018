import numpy as np
from PIL import Image

img = Image.open( "in.jpg" )
img.load()
data = np.asarray( img, dtype="int32" )

message = "test"
message_in_bin = []
for letter in message:
  for digit in (bin(ord(letter))[2:]):
      message_in_bin.append(digit)

print(message_in_bin)

m, n, d = data.shape
for digit in message_in_bin:
	for i in range(m):
		for j in range(n):
			for k in range(d):
				new_val_list = list(bin(data[i, j, k]))
				if(new_val_list[-1] == str(digit)):
