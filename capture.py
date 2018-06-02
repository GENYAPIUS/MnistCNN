#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys
import subprocess
from time import sleep

platform = sys.platform
ffmpeg_command = ["ffmpeg"]

if platform == "linux":
  subprocess.call(["v4l2-ctl", "--list-devices"])
  device = input("input video device (/dev/video0): ")
  if device == "":
    device = "/dev/video0"
  # subprocess.call(["ffmpeg", "-f", "v4l2", "-list_formats", "all", "-i" , device])
  ffmpeg_command += ["-f", "v4l2", "-i", device]
  

elif platform == "win32":
  subprocess.call(["ffmpeg", "-list_devices", "true", "-f", "dshow", "-i", "dummy"])
  device = input("input video device name: ")

  ffmpeg_command += [ "-f", "dshow", "-i", "video=%s" % device]

elif platform == "macos":
  subprocess.call("ffmpeg", "-f", "avfoundation", "-list_devices","true","-i")

  exit()
else:
  raise Exception("unknown platform")

ffmpeg_command += ["-vframes", "1", "-f", "image2", "-"]

adjusted = False

while True:
  print("ffmpeg command: " + " ".join(ffmpeg_command))
  res = subprocess.check_output(ffmpeg_command, stderr=subprocess.DEVNULL)

  saveFile = open("tmp.jpg", "wb")
  saveFile.write(res)
  saveFile.close()

  