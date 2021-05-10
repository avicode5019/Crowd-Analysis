import json

from commons import get_model

# Custom Imports 
import numpy as np
import PIL.Image as Image
from torchvision import transforms
import matplotlib.pyplot as plt
import random

# Access commons
def CrowdDetection(input_img,detected_img):
	model = get_model()
# Standard RGB transform
	transform=transforms.Compose([transforms.ToTensor(),transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),])
	image_path = ("C:\\Users\\Adhisha\\Projects\\Anemoi Technologies\\Django_Project\\visionai\\media\\"+ str(input_img))
    
	def get_prediction(image_path,detected_img):
		global prediction
		img = transform(Image.open(image_path).convert('RGB'))
		img = img.cpu()
		output = model(img.unsqueeze(0))
		prediction = int(output.detach().cpu().sum().numpy())
		density = ("C:\\Users\\Adhisha\\Projects\\Anemoi Technologies\\Django_Project\\visionai\\media\\"+ detected_img)
		plt.imsave(density, output.detach().cpu().numpy()[0][0]) 

      
    
	get_prediction(image_path,detected_img)

	return input_img,detected_img,prediction