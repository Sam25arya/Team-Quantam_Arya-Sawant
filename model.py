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
  
def detect_document(path):
  #convert grayscale to check contrast
  image = Image.open(path).convert("L")
  stat = ImageStat.Stat(image)
  std_dev = stat.stddev[0]

if std_dev > 65:
  return "📄Document Detected"
else:
  return "🖼️Standard Image"
