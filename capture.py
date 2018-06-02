#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys, os, subprocess, tempfile
from time import sleep
from PIL import Image
from io import StringIO

def save_image(tmp, image_binary):
  temp_image_file = os.path.join(tmp, "tmp.jpg")
  # print("temp file is : %s" % temp_image_file)
  saveFile = open(temp_image_file, "wb")
  saveFile.write(image_binary)
  saveFile.close()
  return temp_image_file

def open_image(imgfile = None):
  if platform == "linux":
    subprocess.call(["xdg-open", imgfile])
  elif platform == "win32":
    subprocess.call(["cmd", "/c", "start",  "mspaint", imgfile])

  return 

def set_camera(platform):
  if platform == "linux":
    subprocess.call(["v4l2-ctl", "--list-devices"])
    device = input("input video device (/dev/video0): ")
    if device == "":
      device = "/dev/video0"
    # subprocess.call(["ffmpeg", "-f", "v4l2", "-list_formats", "all", "-i" , device])
    return(["-f", "v4l2", "-i", device])

  elif platform == "win32":
    subprocess.call(["ffmpeg", "-list_devices", "true", "-f", "dshow", "-i", "dummy"])
    device = input("input video device name: ")
    if device == "":
      device = "USB 視訊裝置"

    return([ "-f", "dshow", "-i", "video=%s" % device])

  elif platform == "macos":
    subprocess.call("ffmpeg", "-f", "avfoundation", "-list_devices","true","-i")
    raise Exception("no code")

  else:
    raise Exception("unknown platform")

def fetch_image(command):
  return subprocess.check_output(command, stderr=subprocess.DEVNULL)

def string_to_int(string):
  return (int)(string)

def set_crop(ffmpeg_command):
  adjusted = False
  adjust_crop = (0,0,0,0)

  # print("ffmpeg command: " + " ".join(ffmpeg_command))
  image_binary = fetch_image(ffmpeg_command)
  image_file = save_image(tempDir, image_binary)
  open_image(image_file)

  while adjusted == False:
    img = Image.open(image_file)

    adjust_position_input = input("input crop start position (x, y): ")
    adjust_position = tuple(map(string_to_int, adjust_position_input.split(",")))

    print("max crop size: %d, %d" % tuple(map(lambda x, y: x - y, img.size, adjust_position)))
    adjust_size_input = input("input crop size (width, height): ")
    try:
      adjust_size = tuple(map(string_to_int, adjust_size_input.split(",")))
    except:
      print("wrong input, retry")
      continue

    adjust_crop = adjust_position + adjust_size
    print("preview crop: left %d, up %d, righ %d, down %d" % adjust_crop)

    with img.crop(adjust_crop) as croped_image:
      # print(croped_image)
      croped_file = os.path.join(tempDir, "croped.jpg")
      croped_image.save(croped_file)
      open_image(croped_file)
    
    adjusted = True if input("preview OK (y/N): ").upper() == "Y" else False

  print("crop adjust done")
  return adjust_crop


## main
global tempDir
tempDir = tempfile.mkdtemp()

platform = sys.platform
ffmpeg_command = ["ffmpeg"]

ffmpeg_command += set_camera(platform)
ffmpeg_command += ["-vframes", "1", "-f", "image2", "-"]

adjust_crop = set_crop(ffmpeg_command)

while True:
  image_binary = fetch_image(ffmpeg_command)
  image_file = save_image(tempDir, image_binary)

  with Image.open(image_file) as img:
    with img.crop(adjust_crop) as croped_image:
      with croped_image.convert(mode="L") as grayscaled_image:
        gray_file = os.path.join(tempDir, "gray.jpg")
        grayscaled_image.save(gray_file)
        open_image(gray_file)