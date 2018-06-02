#!/usr/bin/env python
# coding: utf8
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
  

elif plaform == "windows":
  subprocess.call(["ffmpeg", "-y", "-f", "vfwcap", "-i", " list"])

elif plaform == "macos":
  subprocess.call("ffmpeg", "-f", "avfoundation", "-list_devices","true","-i")

ffmpeg_command += ["-vframes", "1", "-f", "image2", "-"]

while True:
  res = subprocess.check_output(ffmpeg_command, stderr=subprocess.DEVNULL)

  saveFile = open("tmp.jpg", "wb")
  saveFile.write(res)

  print("ffmpeg command: " + " ".join(ffmpeg_command))
  