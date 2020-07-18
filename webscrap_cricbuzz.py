from webbrowser import open_new_tab
from bs4 import BeautifulSoup
import requests

result=requests.get("https://www.cricbuzz.com")
src=result.content
result=requests.get("https://www.cricbuzz.com")
soup=BeautifulSoup(result.content,"html.parser")

i=0
for MATCHES in soup.find_all('div',class_="cb-col cb-col-25 cb-mtch-blk"):
    Bat_team[i]=Matches.find("div",class_=" cb-ovr-flo cb-hmscg-tm-nm")
    Bowl_team[i]=Matches.find("div",class_="cb-ovr-flo cb-hmscg-tm-nm ")
    Bat_team_score[i]=Matches.find("div",class_="cb-ovr-flo")
    Bowl_team_name[i]=Matches.find('div',class_="cb-ovr-flo")
    result[i]=Matches.find("div",class_="cb-ovr-flo cb-text-complete")
    str[i]="The batting team is  "+Bat_team[i]+" the bowling team is "+Bowl_team[i]+ "the scores are "+ Bat_team_score[i]+ "and" + Bowl_team_name[i] + "respectively and the result is "+result[i]
    strtotal=str[i]+strtotal
    i=i+1
filename=webscraping +".html"
f=open(filename,w)

write="""
<html>
<head>
<title>Latest Scores</title>
<body>
"""+strtotal"""
</body>
<html>
"""
    f.close()
    open_new_tab(filename)


