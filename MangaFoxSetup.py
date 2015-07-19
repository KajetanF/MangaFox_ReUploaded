from MangaFoxGUI import *
from urllib import urlopen, urlretrieve
from distutils.core import setup
import re,webbrowser,os,py2exe,sys

def MangaFoxChecker(url,MangaList):
    with open("C:\MangaFox\TodayMangaList.html","w") as MangaWipe:        #Wipes previous Manga List
        MangaWipe.write("")
        MangaWipe.close()
    
    webpage = urlopen(url).read()

    patFinderSeries = re.compile('                        <dl><dt><em>.*</em><span class="chapter nowrap"><a href=".*" class="chapter">(.*)\s\d+</a>')
    patFinderTitle = re.compile('                        <dl><dt><em>.*</em><span class="chapter nowrap"><a href=".*" class="chapter">(.*\s\d+)</a>')
    patFinderLink = re.compile('                        <dl><dt><em>.*</em><span class="chapter nowrap">(<a href=".*)" class="chapter">.*\s\d+</a>')


    findPatTitle = re.findall(patFinderTitle,webpage)
    findPatLink = re.findall(patFinderLink,webpage)
    findPatSeries = re.findall(patFinderSeries,webpage)

    try:
        for i in range(1,len(findPatTitle)+1):
            if findPatSeries[i] in MangaList:
                with open("C:\MangaFox\TodayMangaList.html", "a") as myManga:
                    myManga.write(findPatLink[i]+'">' + findPatTitle[i] + "</a><br>")
                    myManga.close()
    except IndexError:
        pass
    
    
def MultipleChapters():
    patFinderSecondTitle = re.compile('                        <dl><dt><em>.*</em><span class="chapter nowrap"><a href=".*class="chapter">(.*)</a></span></dt><dt><em>.*</em><span class="chapter nowrap"><a href=".*" class="chapter">')
    patFinderSecondLink = re.compile('                        <dl><dt><em>.*</em><span class="chapter nowrap"><a href=".*" class="chapter">.*</a></span></dt><dt><em>.*</em><span class="chapter nowrap"><a href="(.*)" class="chapter">(.*)</a>')

    

def PageChecker(Manga,pages):

    print "LOADING PAGES"
    MangaFoxChecker("http://mangafox.me/releases/",Manga)       #scans first page   
    URL = "http://mangafox.me/releases/2.htm"
    for page in reversed(xrange(2,pages+1)):
            MangaFoxChecker(URL.replace("2",str(page)),Manga)   #scans second page onwards
           
    print "Pages %s have been scanned. Results have been added to document" %(pages)
    print "Setup now complete"
    new = 2
    webbrowser.open("file:///C:/MangaFox/TodayMangaList.html",new=new)

if __name__ == '__main__' :

    newpath = r'C://MangaFox//'
    if not os.path.exists(newpath): os.makedirs(newpath)

    try:
        app = MangaGUI(None)
        app.mainloop()
        if (Address  == "") or (pages  == ""):
            raise AttributeError

    except (AttributeError,NameError,ValueError) as e:    
        MangaList = []          

    PageChecker(app.MangaList,int(app.Page))
    with open("C:\MangaFox\ScriptInfo.txt","w") as ScriptInfo:
        ScriptInfo.write("Pages = " + str(app.Page))
    sys.argv.append("py2exe")
    setup(windows=["C:\Python27\MangaFox\MangaFoxScript.pyw"])
    os._exit(-1)
