#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys,struct
 
class BMP:
 def __init__(self,path):
  f = open(path,"rb")
  data = f.read()
  f.close()
 
  names = ["magick","size_file","creator1","creator2","start_data","header_image","width","height","plan","colors","compression","raw_size","horizontal","vertical","color_palette","important_colors"]
 
  values = struct.unpack('<2sLHHLLLLHHLLLLLL',data[:54])
  self.data = data[54:]
 
  self.header = dict()
 
  for i in range(len(names)):
   self.header[names[i]] = values[i]
 
  # On stocke quelques éléments pour ne pas être obligé de toujours les calculer
  self.size_pixel = self.header['colors']/8
  self.padding_size = self.padding_size()
 
 # Retourne la taille du padding par ligne
 def padding_size(self):
  return ((4-(self.header['width']*self.size_pixel)%4)%4)
 
 # Retourne un tableau contenant le padding dans le fichier bmp
 def padding(self):
  r = []
 
  if self.padding_size != 0:
   start = 0
   for row in range(self.header['height']):
    start += (self.size_pixel*self.header['width'])
    r += struct.unpack('c'*self.padding_size,self.data[start:start+self.padding_size])
    start += self.padding_size
 
  return r
 
if len(sys.argv) != 2:
 print "Manque le fichier bmp"
 sys.exit(1)
 
bmp = BMP(sys.argv[1])
print "Taille padding : %i" % (bmp.padding_size*bmp.header["height"])
for e in bmp.padding():
 if e != 0:
  print "Padding non nul !"
  sys.exit(0)
 
print "Padding nul"
sys.exit(0) 
