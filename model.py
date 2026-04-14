from PIL import Image, ImageStat
import numpy as np

def detect_image(path):
  image = image.open(path)
  arr = np.array(image)
  mean = arr.mean()

if mean < 120:
  return "✅Real"
elif mean < 180:
  return "⚠️Suspicious"
else:
  return "❌AI Generated"
