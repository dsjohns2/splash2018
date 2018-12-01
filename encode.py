import numpy as np
from PIL import Image

def main():
  # Load the Image
  img = Image.open( "in.jpg" )
  img.load()
  data = np.asarray( img, dtype="int32" )

  # Get the message in binary
  message = "test"
  message_len = str(len(message))
  while(len(message_len) < 4):
    message_len = "0" + message_len
  message = message_len + message
  message_in_bin = []
  for letter in message:
    cur_letter = []
    for digit in bin(ord(letter))[2:]:
      cur_letter.append(int(digit))
    while(len(cur_letter)<8):
      cur_letter.insert(0, 0)
    message_in_bin += cur_letter

  # Encode the message into the image
  m, n, d = data.shape
  for count, digit in enumerate(message_in_bin):
    i = int(count / n)
    j = count % n
    lsb = data[i, j, 2] % 2
    if(lsb == 0 and digit == 0):
      # What do we put here?
    elif(lsb == 0 and digit == 1):
      # What do we put here?
    elif(lsb == 1 and digit == 0):
      # What do we put here?
    elif(lsb == 1 and digit == 1):
      # What do we put here?

  # Save the image
  result = Image.fromarray(data.astype(np.uint8))
  result.save("./output.png")
  print("Saving " + message + " into output.png")
