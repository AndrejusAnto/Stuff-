import os
from subprocess import check_output, STDOUT

emu_abi = self.emulator_abi
system_images_output = self.command.subprocess.check_output(
				[os.fsdecode(self.sdkmanager_path), "--list"],
				stderr=subprocess.STDOUT,
				env=self.env,?
				check=True,?
			).decode().split("\n")

system_images = []
system_image = ""

for image in system_images_output:
	if "system" in image:
		img = image.split(" | ")
		if len(img) == 3:
			system_images_str, _, description = img
			_, android_version, default, arch = system_images_str.split(";")
			version = android_version.split("-")[1]
			if arch.strip() == emu_abi:
				if default == "default":
					system_image = system_images_str.strip()
				if version.isnumeric():
					if int(version) >= 26:
						system_images.append({system_images_str.strip():description.strip()})
				else:
					system_images.append({system_images_str.strip():description.strip()})

max_value = len(system_images)
print_switch = True
need_number = f"Just need number between 1 and {max_value}:\n"
default_print = f"Choose desired system image, just enter a number\nPress enter for default system image '{system_image}':\n"

while True:
	for idx, img_info in enumerate(system_images):
		for k ,v in img_info.items():
			print(f"{idx+1}) {k} ({v})")
	
	if print_switch:
		theprint = default_print
	else:
		theprint = need_number
	
	answer = input(theprint)
	
	if len(answer) > 0:
		if int(answer) < max_value and int(answer) >= 1:
			answer = int(answer)
			system_image = [key for key in system_images[answer-1].keys()][0]
			print("Ok, you chose:", system_image)
			break
		else:
			print_switch = False
	else:
		print("Ok, you chose:", system_image)
		break








# output_of_system_images_list = 