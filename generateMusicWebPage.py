# read music from music.json

import json

def big2Small(song):
    return {"title": song['song']['title'],
            "artist": song['artist']['name'] }

def songListToHTMLTable(songs):
    answer =  "<table>\n" + songTableHeader()
    for song in songs:
        answer += song2HTMLTableRow(song)
    answer +=  "</table>\n"
    return answer

def songTableHeader():
    return ("<tr>\n" +
            "<th> Song Title </th>" +
            "<th> Artist Name </th>" +            
           "</tr>\n")


def song2HTMLTableRow(song):
    return ("<tr>\n" +
            "<td>" + song['song']['title'] + "</td>" +
            "<td>" + song['artist']['name'] + "</td>" +            
           "</tr>\n")


def writeWebPage(filename,content,title):
    with open(filename,'w') as webpage:
      webpage.write("<!DOCTYPE html>\n")
      webpage.write("<html>\n")
      
      webpage.write("<head>\n")
      styleElem = """
      <style>
       table {
        border-collapse: collapse;
       }

       table, th, td {
        border: 1px solid black;
       }
      </style>
      
      """
      webpage.write(styleElem)
      
      webpage.write("<title>" + title + "</title>\n")
      webpage.write("</head>\n")

      webpage.write("<body>\n")
      webpage.write(content)
      webpage.write("</body>\n")

      webpage.write("</html>\n")
      

if __name__=="__main__":
  with open('music.json') as json_data:
    songs = json.load(json_data)

  print("The variable songs now contains all the data")

  print("The variable songs is a list of big complicated dictionaries")
  print("We'd like a list of something easier to work with")

  print("The function big2Small(song) will turn a big song dictionary")
  print("into a smaller one")
  
  writeWebPage("fiveSongs.html",songListToHTMLTable(songs[5:10]),"five songs")
  
