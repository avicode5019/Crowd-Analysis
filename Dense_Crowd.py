import torch
from models import vgg19
from PIL import Image
from torchvision import transforms
import cv2
import numpy as np
import scipy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

def Dense_Crowd(input_img,detected_img):
	model_path = "model_qnrf.pth"
#model_path = "C:/Users/Anudit/Downloads/model_sh_A.pth"

	device = torch.device('cpu')  # device can be "cpu" or "gpu"

	model = vgg19()
	model.to(device)
	model.load_state_dict(torch.load(model_path, device))
	model.eval()


	def predict(input_img,detected_img):
		global count
		image = mpimg.imread("C:\\Users\\Adhisha\\Projects\\Anemoi Technologies\\Django_Project\\visionai\\media\\"+ str(input_img))
		plt.imshow(image)
		plt.xticks([]); plt.yticks([])
		inp = np.array(Image.open("C:\\Users\\Adhisha\\Projects\\Anemoi Technologies\\Django_Project\\visionai\\media\\"+ str(input_img)))
		inp = Image.fromarray(inp.astype('uint8'), 'RGB')
		inp = transforms.ToTensor()(inp).unsqueeze(0)
		inp = inp.to(device)
		with torch.set_grad_enabled(False):
			outputs, _ = model(inp)
		count = torch.sum(outputs).item()
		vis_img = outputs[0, 0].cpu().numpy()
    # normalize density map values from 0 to 1, then map it to 0-255.
		vis_img = (vis_img - vis_img.min()) / (vis_img.max() - vis_img.min() + 1e-5)
		vis_img = (vis_img * 255).astype(np.uint8)
		vis_img = cv2.applyColorMap(vis_img, cv2.COLORMAP_JET)
		vis_img = cv2.cvtColor(vis_img, cv2.COLOR_BGR2RGB)
		img = Image.fromarray(vis_img, 'RGB')
		img.save("C:\\Users\\Adhisha\\Projects\\Anemoi Technologies\\Django_Project\\visionai\\media\\"+ detected_img)
		return int(count)


	predict(input_img,detected_img)

	return input_img,detected_img,int(count)