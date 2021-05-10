import cv2
import os
from Crowd_video import predict


def Crowd_Video_Analysis(input_video,file_name):

	global dir_name

	filename = str(file_name)
	dir_name = os.path.splitext(filename)[0]
	parent_dir = "C:\\Users\\Adhisha\\Projects\\Anemoi Technologies\\Django_Project\\visionai\\media\\Crowd_Video_Frames"
	directory = os.path.join(parent_dir, dir_name) 
	os.mkdir(directory)
	    
	seconds = 2
	cap = cv2.VideoCapture("C:\\Users\\Adhisha\\Projects\\Anemoi Technologies\\Django_Project\\visionai\\media\\"+str(input_video))

	# Get the frames per second
	fps = round(cap.get(cv2.CAP_PROP_FPS)) 
	#print("FPS :", fps)
	multiplier = fps*seconds

	# Get the total numer of frames in the video.
	frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
	#print("FC :", frame_count)

	#Get Images from video
	#filename = str(file_name)
	#dir_name = os.path.splitext(filename)[0]
	    
	cap = cv2.VideoCapture("C:\\Users\\Adhisha\\Projects\\Anemoi Technologies\\Django_Project\\visionai\\media\\"+str(input_video))
	count = -1
	seconds = 2
	fps = round(cap.get(cv2.CAP_PROP_FPS)) 
	multiplier = fps*seconds

	while cap.isOpened():
	    ret, frame = cap.read()

	    if ret:
	        #cv2.imwrite('F:/Output/%s/Frame{:f}.jpg'.format(count),frame)
	        cv2.imwrite('C:\\Users\\Adhisha\\Projects\\Anemoi Technologies\\Django_Project\\visionai\\media\\Crowd_Video_Frames\\%s\\Frame{:f}.jpg'.format(count)%(dir_name),frame)
	        count += multiplier 
	        cap.set(1, count)
	    else:
	        cap.release()
	        break




	def view_images():
		l = os.listdir('C:\\Users\\Adhisha\\Projects\\Anemoi Technologies\\Django_Project\\visionai\\media\\Crowd_Video_Frames\\'+str(dir_name))
	    #print(l)
		for m in l:
			image_path=('C:\\Users\\Adhisha\\Projects\\Anemoi Technologies\\Django_Project\\visionai\\media\\Crowd_Video_Frames\\'+str(dir_name)+"\\"+m)
			predict('C:\\Users\\Adhisha\\Projects\\Anemoi Technologies\\Django_Project\\visionai\\media\\Crowd_Video_Frames\\'+str(dir_name)+"\\"+m ,image_path)


	view_images()

	v_frames = os.listdir('C:/Users/Adhisha/Projects/Anemoi Technologies/Django_Project/visionai/media/Crowd_Video_Frames/'+str(dir_name))
	frame_no = len(v_frames)
	frames_data= {}
	for i in range(1,frame_no+1,1):
		frames_data['f' + str(i)] = "Crowd_Video_Frames/"+dir_name+"/"+v_frames[i-1]
 
	locals().update(frames_data)

	my_list = []
	key_list = []
	for key,value in frames_data.items() :
		my_list.append(value)
		key_list.append(key)


	return input_video,fps,frame_count,my_list,frame_no,key_list