from concurrent.futures import ThreadPoolExecutor as terd
import os,time,string,random,json,uuid,sys,re,requests
try:import pycurl, io
except:os.system('pip install pycurl')
try:import mechanize;br = mechanize.Browser()
except:os.system('pip install mechanize')
