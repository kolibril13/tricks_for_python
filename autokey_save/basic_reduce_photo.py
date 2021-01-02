from pathlib import Path
import os
suffix = ".jpg"
input_path= Path.home() / "Downloads"
file_paths= [subp for subp in input_path.rglob('*') if  suffix == subp.suffix]
file_paths.sort()

output_path =  Path.home() / "Downloads/processed"
output_path.mkdir(parents=True, exist_ok=True)


for file_p in file_paths:
	input = str(file_p)
	output = str(  output_path / file_p.name  ) 
	command = f"ffmpeg -i {input} -q:v 10 {output}"
	os.system(command)
	
