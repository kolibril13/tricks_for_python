from pathlib import Path
import os
suffix = ".mp4"
input_path= Path.home() / "Downloads"
file_paths= [subp for subp in input_path.rglob('*') if  suffix == subp.suffix]
file_paths.sort()

output_path =  Path.home() / "Downloads/SmallVideos"
output_path.mkdir(parents=True, exist_ok=True)


for file_p in file_paths:
	input = str(file_p)
	output = str(  output_path / file_p.name  ) 
	command = f"ffmpeg -i {input} -vf scale='720:480' {output}"
	print(command)
	os.system(command)
	
