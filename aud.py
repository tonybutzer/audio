import eyed3

audiofile = eyed3.load("../a.mp3")

print(dir(audiofile))

print(dir(audiofile.info))

print(audiofile.info.time_secs)
