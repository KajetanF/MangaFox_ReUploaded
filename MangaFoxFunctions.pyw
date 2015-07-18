from urllib import urlopen
import re,webbrowser,os

def MangaListAdjuster():
    with open("C:\MangaFox\TodayMangaList.html","w") as MangaWipe:        #Wipes previous Manga List
        MangaWipe.write("")
        MangaWipe.close()

    with open("C:\MangaFox\myMangaList.txt","r") as MangaInfo:           #Generates a new manga list to search from Manga List Document
        MangaStr = MangaInfo.read()
        print "Your novels are the following:\n %s" %(MangaStr)

    with open("C:\MangaFox\myMangaList.txt", 'r') as myManga:
        ListOfManga = myManga.read()
    MangaList = filter(None,ListOfManga.split("\n"))        #Creates List with added manga, while filtering out dead spaces
    print MangaList
    return MangaList

def MangaFoxChecker(url,MangaList):                    
    webpage = urlopen(url).read()

    patFinderSeries = re.compile('                        <dl><dt><em>.*</em><span class="chapter nowrap"><a href=".*" class="chapter">(.*)\s\d+</a>')
    patFinderTitle = re.compile('                        <dl><dt><em>.*</em><span class="chapter nowrap"><a href=".*" class="chapter">(.*\s\d+)</a>')
    patFinderLink = re.compile('                        <dl><dt><em>.*</em><span class="chapter nowrap">(<a href=".*)" class="chapter">.*\s\d+</a>')


    findPatTitle = re.findall(patFinderTitle,webpage)
    findPatLink = re.findall(patFinderLink,webpage)
    findPatSeries = re.findall(patFinderSeries,webpage)

    with open("C:\MangaFox\TodayMangaList.html", "a") as myManga:
        myManga.write('<a href="http://mangafox.com>MANGAFOX HOMEPAGE"</a><br><br>')

    try:
        for i in range(1,len(findPatTitle)+1):
            if findPatSeries[i] in MangaList:
                with open("C:\MangaFox\TodayMangaList.html", "a") as myManga:
                    myManga.write(findPatLink[i]+'">' + findPatTitle[i] + "</a><br>")
    except IndexError:
        pass
    
    
def PageChecker(Manga,pages):
    MangaFoxChecker("http://mangafox.me/releases/",Manga)       #scans first page   
    URL = "http://mangafox.me/releases/2.htm"
    MangaFoxChecker(URL,Manga)
    for page in reversed(xrange(2,int(pages)+1)):
            MangaFoxChecker(URL.replace("2",str(page)),Manga)    
    new = 2
    webbrowser.open("file:///C:/Users/Kajetan/Documents/TodayMangaList.html",new=new)

if __name__ == '__main__':
    with open("C:\MangaFox\ScriptInfo.txt") as ScriptInfo:
        pages = int(ScriptInfo.read().strip("Pages = "))
    Manga = MangaListAdjuster()                   #Creates the Manga List file
    PageChecker(Manga,pages)
    new = 2
    webbrowser.open("file:///C:/Users/Kajetan/Documents/TodayMangaList.html",new=new)
    os._exit(-1)
    
