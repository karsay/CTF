import matplotlib.pyplot as plt
import numpy as np

# img_gray = np.array([
#   [0,0,255],
#   [255,0,0],
#   [255,0,0]
# ], dtype = np.uint8)

def qr_drow():
  qr_data = np.loadtxt("qr_data.txt")
  #画像の表示
  plt.imshow(qr_data, cmap = 'gray', vmin = 0, vmax = 255, interpolation = 'none')
  plt.show()
