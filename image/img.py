import warnings
warnings.filterwarnings("ignore")

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

device=torch.device("cuda" if torch.cuda.is_available() else "cpu")

processor=BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model=BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)

img=Image.open("picture.jpg").convert("RGB")
inputs=processor(img,return_tensors="pt").to(device)

with torch.no_grad():
    output=model.generate(**inputs,max_length=40,num_beams=5)

caption=processor.decode(output[0],skip_special_tokens=True)
print("Generated Caption:",caption)
