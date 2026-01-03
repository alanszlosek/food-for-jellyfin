import os
import re

start = "."

# TODO: replace "Nova" below with the name of your show. Or make this script smarter.


# Tweak the regexed below based on your file naming conventions
# Ideally you're using something like: "SHOW S01E03 EPISODE TITLE.mp4"

p_season = re.compile(r"Season (\d+)")
p_episode = re.compile(r"(Season \d+ Episode |S\d+E)(\d+) ")
p_title = re.compile(r"(-|S\d+E\d+) ([a-zA-Z0-9 ]+)\.mp4")

for root, dirs, files in os.walk(start):
    for file in files:
        if not file.endswith(".mp4"):
            continue
        filepath = os.path.join(root, file)

        season = None
        m = p_season.search(filepath)
        if m:
            season = m.group(1)

        title = None
        m = p_title.search(filepath)
        if m:
            title = m.group(2)

        episode = None
        m = p_episode.search(filepath)
        if m:
            episode = m.group(2)


        x = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<episodedetails>
    <title>{title}</title>
    <season>{season}</season>
    <showtitle>Nova</showtitle>
    <episode>{episode}</episode>
</episodedetails>
"""

        new_filepath = f"./Season {season}/Nova S{season}E{episode} {title}.mp4"
        if filepath != new_filepath:
            print(f"rename {filepath} to {new_filepath}")
            #os.rename(filepath, new_filepath)

        new_nfo = f"./Season {season}/Nova S{season}E{episode} {title}.nfo"
        #print("maybe " + new_nfo)
        with open(new_nfo, "w") as f:
            f.write(x)
