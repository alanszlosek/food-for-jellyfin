import subprocess
import yaml

num = 1
with open("files.yaml") as stream:
    doc = yaml.safe_load(stream)

    for filename,times in doc.items():
        print(filename)
        for pair in times:
            start = pair[0]
            stop = pair[1]
            num = int(pair[2])
            out_filename = f"/home/user/Videos/out/Mecha Builders - S01E{num:02}.mp4"
            args = ["ffmpeg", "-y", "-ss", start, "-to", stop, "-i", filename, "-c", "copy", out_filename]
            print(f"Running: {args}")
            r = subprocess.run(args, capture_output=True)
            print(r)

print("done")