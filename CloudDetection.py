# Author - Quazi Rabbi
# Date Created - 5/29/2018
# Version - 1.0
# Description - 
# Detectes clouds from downloading image from website 



import numpy as np
import urllib , urllib2
import ImageProcessing as IPr
import date as dt


class cloud:

	def __init__(self,TimePST):
		self.PST = TimePST
		self.UTC = TimePST #should be changed later
		
		self.Image_Processing(self.UTC)
	
	def Image_Processing(self,TimeUTC):
		if self.Image_Download(TimeUTC):
			self.CloudValue = IPr.Image_Processing(TimeUTC)
			print self.CloudValue
		else:
			return 0
	
	def Image_Download(self,TimeUTC):
		
		date = dt.date()
		
		link = "https://weather.gc.ca/data/prog/regional/"+date+"00/"+date+"00_054_R1_north@america@northwest_I_ASTRO_nt_0"+str(TimeUTC).zfill(2)+".png"
		dowloadPic = "Images/Image"+str(TimeUTC)+".jpg"
		print TimeUTC
		try:
			urllib2.urlopen(link)
			urllib.urlretrieve(link, dowloadPic)
			return 1
		except:
			return 0
 


obj = [cloud(i) for i in range(49)]



