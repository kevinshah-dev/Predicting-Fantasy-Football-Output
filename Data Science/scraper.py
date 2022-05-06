#!/usr/bin/env 
import csv
import base64
from bs4 import BeautifulSoup
import http.cookiejar
import urllib.request


# do file output
dataset = []
outfile = open('ff_data21.csv','w')
write = csv.writer(outfile)


# Store the cookies and create an opener that will hold them
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# Add our headers
opener.addheaders = [('User-agent', 'yahoo-test')]

# Install our opener (note that this changes the global opener to the one
# we just made, but you can also just call opener.open() if you want)
urllib.request.install_opener(opener)

# The action/ target from the form
authentication_url = 'https://login.yahoo.com/config/login?.src=spt&.intl=us&.lang=en-US&.done=http://football.fantasysports.yahoo.com/'

# Input parameters we are going to send
payload = {
  'login': 'login',
  'passwd': 'passwd'
  }

# Use urllib to encode the payload
data = urllib.parse.urlencode(payload).encode('utf-8')

# Build our Request object (supplying 'data' makes it a POST)
req = urllib.request.Request(authentication_url, data)

# Make the request and read the response
resp = urllib.request.urlopen(req)
contents = resp.read()



def getpage(player_page):
    
    handle = urllib.request.urlopen(player_page)
    
    
    html = handle.read()
    soup=BeautifulSoup(html, "html5lib")
    
    
    # get names
    l_names=[]
    
    # get position and team
    l_pos=[]
    l_team=[]
    temp_split=[]
    
    p_names = soup.findAll('div', attrs={'class' : 'ysf-player-name Nowrap Grid-u Relative Lh-xs Ta-start'})
    for row in p_names:
        l_names.append(str(row.find('a').string))
        print (str(row.find('a').string))
        temp_split.append(str(row.find('span', attrs={'class' : 'Fz-xxs'}).string))
        print (str(row.find('span', attrs={'class' : 'Fz-xxs'}).string))
        
    for i in temp_split:
        temp=i.split(" - ")
        l_team.append(temp[0])
        l_pos.append(temp[1])
          
    
    # get stats
    l_gp=[]
    l_points = []
    l_preranking = []
    l_actual=[]
    l_owners=[]
    l_passyds=[]
    l_passtd=[]
    l_passint=[]
    l_rushyds=[]
    l_rushtd=[]   
    l_recepts=[]
    l_recyds=[]
    l_rectd=[]
    l_returntd=[]
    l_2pt = []
    l_fumble=[]
    
    #find class using soup
    p_stats = soup.findAll('td', attrs={'class' : 'Alt Bdrend'})
    
    #iterate stats per row
    for row in p_stats:
      l_gp.append(str(row.nextSibling.nextSibling.string))
      l_points.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_preranking.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_actual.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_owners.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))

      l_passyds.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_passtd.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_passint.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      
      # rush att
      l_rushyds.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_rushtd.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))

      l_recepts.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_recyds.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_rectd.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_returntd.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      
      l_2pt.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
      l_fumble.append(str(row.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.string))
         
      
     
    
    transposer = zip(l_names, l_team, l_pos, l_gp, l_preranking, l_points, l_owners, l_actual, l_passyds, l_passtd, l_passint, l_rushyds, l_rushtd, l_recepts, l_recyds, l_rectd, l_returntd, l_2pt, l_fumble)
    
    for i in transposer:
        dataset.append(i)
    
    return 0

# call function
getpage("https://football.fantasysports.yahoo.com/f1/42524/players?&sort=AR&sdir=1&status=ALL&pos=O&stat1=S_S_2021&jsenabled=1")
getpage("https://football.fantasysports.yahoo.com/f1/42524/players?status=ALL&pos=O&cut_type=9&stat1=S_S_2021&myteam=0&sort=AR&sdir=1&count=25")
getpage("https://football.fantasysports.yahoo.com/f1/42524/players?status=ALL&pos=O&cut_type=9&stat1=S_S_2021&myteam=0&sort=AR&sdir=1&count=50")
getpage("https://football.fantasysports.yahoo.com/f1/42524/players?status=ALL&pos=O&cut_type=9&stat1=S_S_2021&myteam=0&sort=AR&sdir=1&count=75")
getpage("https://football.fantasysports.yahoo.com/f1/42524/players?status=ALL&pos=O&cut_type=9&stat1=S_S_2021&myteam=0&sort=AR&sdir=1&count=100")
getpage("https://football.fantasysports.yahoo.com/f1/42524/players?status=ALL&pos=O&cut_type=9&stat1=S_S_2021&myteam=0&sort=AR&sdir=1&count=125")
getpage("https://football.fantasysports.yahoo.com/f1/42524/players?status=ALL&pos=O&cut_type=9&stat1=S_S_2021&myteam=0&sort=AR&sdir=1&count=150")
getpage("https://football.fantasysports.yahoo.com/f1/42524/players?status=ALL&pos=O&cut_type=9&stat1=S_S_2021&myteam=0&sort=AR&sdir=1&count=175")
getpage("https://football.fantasysports.yahoo.com/f1/42524/players?status=ALL&pos=O&cut_type=9&stat1=S_S_2021&myteam=0&sort=AR&sdir=1&count=200")
getpage("https://football.fantasysports.yahoo.com/f1/42524/players?status=ALL&pos=O&cut_type=9&stat1=S_S_2021&myteam=0&sort=AR&sdir=1&count=225")
getpage("https://football.fantasysports.yahoo.com/f1/42524/players?status=ALL&pos=O&cut_type=9&stat1=S_S_2021&myteam=0&sort=AR&sdir=1&count=250")
getpage("https://football.fantasysports.yahoo.com/f1/42524/players?status=ALL&pos=O&cut_type=9&stat1=S_S_2021&myteam=0&sort=AR&sdir=1&count=275")


# write rows and close file
for i in dataset:
    write.writerow(i)
outfile.close()