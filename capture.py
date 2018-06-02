#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys, os, subprocess, tempfile
from time import sleep
from PIL import Image
from io import StringIO

class Capture:
  ## assign after set_camera
  ffmpeg_command = None

  ## assign after set_crop
  crop = None
  
  ## init create
  platform = None
  temp_dir = None

  def __init__(self):
    self.platform = sys.platform
    self.temp_dir = tempfile.mkdtemp()

  def string_to_int(self, string):
    return (int)(string)

  def fetch_image(self):
    return subprocess.check_output(self.ffmpeg_command, stderr=subprocess.DEVNULL)
    # return subprocess.check_output(self.ffmpeg_command)

  def open_image(self, imgfile):
    if self.platform == "linux":
      subprocess.call(["xdg-open", imgfile])
    elif self.platform == "win32":
      subprocess.call(["cmd", "/c", "start",  "mspaint", imgfile])
    return 

  def save_image(self, image_binary):
    temp_image_file = os.path.join(self.temp_dir, "tmp.jpg")
    # print("temp file is : %s" % temp_image_file)
    saveFile = open(temp_image_file, "wb")
    saveFile.write(image_binary)
    saveFile.close()
    return temp_image_file

  def set_camera(self):
    self.ffmpeg_command = ["ffmpeg"]

    if self.platform == "linux":
      subprocess.call(["v4l2-ctl", "--list-devices"])
      device = input("input video device (/dev/video0): ")
      if device == "":
        device = "/dev/video0"
      self.ffmpeg_command += ["-f", "v4l2", "-i", device]

    elif self.platform == "win32":
      subprocess.call(["ffmpeg", "-list_devices", "true", "-f", "dshow", "-i", "dummy"])
      device = input("input video device name: ")
      if device == "":
        device = "USB 視訊裝置"

      self.ffmpeg_command += [ "-f", "dshow", "-i", "video=%s" % device]

    elif self.platform == "macos":
      subprocess.call("ffmpeg", "-f", "avfoundation", "-list_devices","true","-i")
      raise Exception("no code")

    else:
      raise Exception("unknown platform")

    self.ffmpeg_command += ["-vframes", "1", "-f", "image2", "-"]
    return self.ffmpeg_command

  def set_crop(self):
    self.crop = (0,0,0,0)

    # print("ffmpeg command: " + " ".join(ffmpeg_command))
    image_binary = self.fetch_image()
    image_file = self.save_image(image_binary)
    self.open_image(image_file)

    while True:
      img = Image.open(image_file)

      adjust_position_input = input("input crop start position (x, y): ")
      try:
        adjust_position = tuple(map(self.string_to_int, adjust_position_input.split(",")))
      except:
        print("wrong position, retry")
        continue

      print("max crop size: %d, %d" % tuple(map(lambda x, y: x - y, img.size, adjust_position)))
      adjust_size_input = input("input crop size (width, height): ")
      try:
        adjust_size = tuple(map(self.string_to_int, adjust_size_input.split(",")))
      except:
        print("wrong size, retry")
        continue

      self.crop = adjust_position + adjust_size
      print("preview crop: left %d, up %d, righ %d, down %d" % self.crop)

      with img.crop(self.crop) as croped_image:
        try:
          # print(croped_image)
          croped_file = os.path.join(self.temp_dir, "croped.jpg")
          croped_image.save(croped_file)
        except:
          print("wrong size, rety")
          continue
        self.open_image(croped_file)
      
      if input("preview OK (y/N): ").upper() == "Y":
        break

    return self.crop
  
  def timer(self, task, delay_time = 0, count = None):    
    if self.ffmpeg_command == None:
      raise Exception("camera not set")

    if self.crop == None:
      raise Exception("no crop set")

    current_count = 0
    while True:
      image_binary = self.fetch_image()
      image_file = self.save_image(image_binary)

      with Image.open(image_file) as img:
        with img.crop(self.crop) as croped_image:
          with croped_image.convert(mode="L") as grayscaled_image:
            task(self, grayscaled_image)
            current_count += 1
            if count != None and current_count >= count:
              break
            if (delay_time > 0):
              sleep(delay_time)
