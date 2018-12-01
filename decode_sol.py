import numpy as np
from PIL import Image

def main():
  # Load the Image
  img = Image.open( "output.png" )
  img.load()
  data = np.asarray( img, dtype="int32" )

  # Get the message in binary
  m, n, d = data.shape
  message_in_bin = []
  for count in range(m*n):
    i = int(count / n)
    j = count % n
    if(data[i, j, 2] % 2 == 0):
      message_in_bin.append(0)
    else:
      message_in_bin.append(1)

  # Get the number of letters in the message
  message_len = ""
  for i in range(4):
    cur_letter = 0
    for j in range(8):
      cur_letter += message_in_bin[(i*8)+j] * 2**(7-j)
    message_len += chr(cur_letter)
  num_letters = int(message_len)

  # Get the secret message
  secret_message = ""
  for i in range(num_letters+4):
    cur_letter = 0
    for j in range(8):
      cur_letter += message_in_bin[(i*8)+j] * 2**(7-j)
    secret_message += chr(cur_letter)
  print(secret_message)