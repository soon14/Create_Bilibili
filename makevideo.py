import subprocess,json
import os


class MakeVideo:
	def __init__(self, mp3_path,images_path,videos_dir):
		self.mp3_path = mp3_path
		self.images_path = images_path
		self.videos_dir = videos_dir

	def get_files(self):
		files_name = []
		files_path = []
		for file in os.listdir(mp3_path):
			file_name = file.split(".")[0]
			files_name.append(file_name)
			file_path = os.path.join(mp3_path,file)
			files_path.append(file_path)
			print(files_path)
		return files_path

	def getMp3Len(self,files_path):
		#images_path = "E:\\PR\\04\\image\\"
		print(files_path,"00")
		for each_file_path in files_path:
			command = ["D:\\Software\\ffmpeg\\bin\\ffprobe.exe","-loglevel","quiet","-print_format","json","-show_format","-show_streams","-i", each_file_path]
			result = subprocess.Popen(command,shell=True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
			out = result.stdout.read()
			#print(str(out))
			temp = str(out.decode('utf-8'))
			data = json.loads(temp)["format"]['duration']
			print(data,each_file_path)
			image_name_0 = os.path.basename(each_file_path).split(".")[0]
			#image_name_0 = each_file_path.split("/")[-1].split(".")[0]
			image_name = image_name_0 + ".jpg"
			image_path = os.path.join(images_path,image_name)
			#print(image_path)

			vframes = str(int(float(data)*30))
			video_name_0 = os.path.basename(each_file_path).split(".")[0]
			#video_name = os.path.join(os.path.basename(each_file_path).split(".")[0],".mp4")
			video_name = video_name_0 + ".mp4"
			#videos_dir = "E:\\PR\\04\\here"
			video_path = os.path.join(videos_dir,video_name)
			command2 = ["D:\\Software\\ffmpeg\\bin\\ffmpeg.exe" ,"-y", "-loop", "1", "-i",image_path,"-i",each_file_path,"-r","30","-b:v","2500k","-vframes",vframes,"-acodec","ac3","-ab","160k","-vcodec","mpeg4",video_path]
			subprocess.Popen(command2)


		#return float(data)

if __name__ == "__main__":
	mp3_path = "C:\\test\\mp3"
	images_path = "C:\\test\\mp3\\image\\"
	videos_dir = "C:\\test\\here"
	makevideo = MakeVideo(mp3_path, images_path, videos_dir)
	files_path1 = makevideo.get_files()
	timeoo = makevideo.getMp3Len(files_path=files_path1)


