import json
import codecs

def CreateOpenSong(books, chapters, verses):
    data = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n"
    data = data + "<bible>\n"
    for b in books:
        print(b['name'])
        data = data + "\t<b n=\"" + b['name'] + "\">\n"
        fChapters = [c for c in chapters if(b['bid'] == c['bid'])]
        for c in fChapters:
            data = data + "\t\t<c n=\"" +  str(c['chapter']) + "\">\n"
            fVerses = [v for v in verses if(c['cid'] == v['cid'])]
            for v in fVerses:
                data = data + "\t\t\t<v n=\"" + v['verse'] + "\">" + v['text'] + "</v>\n"
            data = data + "\t\t</c>\n"
        data = data + "\t</b>\n"
    data = data + "</bible>\n"

    outputFile = codecs.open("BYSB.xmm", "w", "utf-8")
    outputFile.write(data)
    outputFile.close()

def CreateZefania(books, chapters, verses):
    data = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n"
    data = data + "<XMLBIBLE xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:noNamespaceSchemaLocation=\"zef2005.xsd\" version=\"2.0.1.18\" status=\"v\" biblename=\"Bibiliya Yera\" revision=\"1\" type=\"x-bible\">\n"
    data = data + "\t<INFORMATION>\n"
    data = data + "\t\t<title>Bibiliya Yera</title>\n"
    data = data + "\t\t<creator>\n"
    data = data + "\t\t</creator>\n"
    data = data + "\t\t<subject>bible</subject>\n"
    data = data + "\t\t<description>Bibiliya Yera 2011</description>\n"
    data = data + "\t\t<publisher>Société Biblique au Rwanda</publisher>\n"
    data = data + "\t\t<contributors></contributors>\n"
    data = data + "\t\t<date>2020-05-03</date>\n"
    data = data + "\t\t<type>Bible</type>\n"
    data = data + "\t\t<format>Zefania XML Bible Markup Language</format>\n"
    data = data + "\t\t<identifier>KIN</identifier>\n"
    data = data + "\t\t<source>ftp://unboundftp.biola.edu/pub/kinyarwanda_utf8.zip</source>\n"
    data = data + "\t\t<language>KIN</language>\n"
    data = data + "\t\t<coverage>provide the Bible to the nations of the world</coverage>\n"
    data = data + "\t\t<rights>\n"
    data = data + "\t\t</rights>\n"
    data = data + "\t</INFORMATION>\n"
    for b in books:
        print(b['name'])
        data = data + "\t<BIBLEBOOK bnumber=\"" + str(b['bid']) + "\" bname=\"" + b['name'] + "\" bsname=\"" + b['short-name'] + "\">\n"
        fChapters = [c for c in chapters if(b['bid'] == c['bid'])]
        for c in fChapters:
            data = data + "\t\t<CHAPTER cnumber=\"" +  str(c['chapter']) + "\">\n"
            fVerses = [v for v in verses if(c['cid'] == v['cid'])]
            for v in fVerses:
                data = data + "\t\t\t<VERS vnumber=\"" + v['verse'] + "\">" + v['text'] + "</VERS>\n"
            data = data + "\t\t</CHAPTER>\n"
        data = data + "\t</BIBLEBOOK>\n"
    data = data + "</XMLBIBLE>\n"

    outputFile = codecs.open("KIN.xml", "w", "utf-8")
    outputFile.write(data)
    outputFile.close()


books = []
chapters = []
verses = []
print("Starting ...................")
with open('books.json', encoding='utf-8') as booksFile:
    books  = json.load(booksFile)

with open('chapters.json', encoding='utf-8') as chaptersFile:
    chapters  = json.load(chaptersFile)

with open('verses.json', encoding='utf-8') as versesFile:
    verses  = json.load(versesFile)


CreateOpenSong(books, chapters, verses)
CreateZefania(books, chapters, verses)