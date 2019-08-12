import csv
import argparse

parser = argparse.ArgumentParser(description='Create tex file from spreadsheet; tex creates genealogy graphis.')
parser.add_argument("spreadsheet_name")
my_arguments = parser.parse_args()
 
spreadsheet_name = my_arguments.spreadsheet_name + ".csv"

header=r"""
\documentclass[final, 12pt]{beamer}
%\usepackage[size=custom,width=200,height=107,scale=.5,orientation=portrait]{beamerposter}
%\usepackage[scale=1.24]{beamerposter} % Use the beamerposter package for laying out the poster
\usepackage[width=36in,scale=.5,orientation=landscape]{beamerposter}

\usepackage{pst-slpe}
\usepackage{pst-grad}
\usepackage{pst-node}
\usepackage{pst-blur}
 
\definecolor{teacher}{HTML}{0000FF}  
\definecolor{hostile}{HTML}{FF0000}  
\definecolor{influence}{HTML}{808080}  
\definecolor{colleagues}{RGB}{64 200 0}
\definecolor{other}{RGB}{255 255 255} 


\definecolor{anthropologist1}{HTML}{FFB3B3}  
\definecolor{anthropologist2}{HTML}{FFE6E6}
\definecolor{anthropologist3}{HTML}{CCCC00}
 
\definecolor{linguist1}{HTML}{DBA909}  
\definecolor{linguist2}{HTML}{F8EDCB} % EDBB99
\definecolor{linguist3}{HTML}{533419}
\definecolor{linguist-line}{HTML}{D2691E}

\definecolor{linguist-fill2}{RGB}{255 255 0}
\definecolor{linguist-fill3}{RGB}{255 255 0}
\definecolor{linguist-fill4}{RGB}{255 255 0}
 
\definecolor{philosopher1}{HTML}{66FF66} 
\definecolor{philosopher2}{HTML}{EBFCF3}
\definecolor{philosopher3}{HTML}{00FF00} 
 

\definecolor{psychologist1}{HTML}{00FFFF}
\definecolor{psychologist2}{HTML}{EBFCF3} % aqua (BLUE)
\definecolor{psychologist3}{HTML}{269900}
\definecolor{psychologist-fill3}{HTML}{00FF00}
 
\definecolor{sociologist1}{HTML}{DDFF00}  
\definecolor{sociologist2}{HTML}{DDFFCC}
\definecolor{sociologist3}{HTML}{ACCC00}
\definecolor{sociologist-line}{HTML}{D2691E}

\definecolor{logician1}{HTML}{73AE9D}  
\definecolor{logician2}{HTML}{DDFFCC}
\definecolor{logician3}{HTML}{ACCC00}


 

\definecolor{linglog1}{HTML}{FF7F24} % for barhillel 
\definecolor{linglog2}{HTML}{FFE6E3}
\definecolor{linglog3}{HTML}{FF0000}
 
\definecolor{mathematician1}{HTML}{BCA9F5}  
\definecolor{mathematician2}{HTML}{E0ECF8}
\definecolor{mathematician3}{HTML}{0000FF}

 
\definecolor{other-fill}{HTML}{D3D3D3}  
 

  

%-----------------------------------------------------------
% Define the column widths and overall poster size
% To set effective sepwid, onecolwid and twocolwid values, first choose how many columns you want and how much separation you want between columns
% In this template, the separation width chosen is 0.024 of the paper width and a 4-column layout
% onecolwid should therefore be (1-(# of columns+1)*sepwid)/# of columns e.g. (1-(4+1)*0.024)/4 = 0.22
% Set twocolwid to be (2*onecolwid)+sepwid = 0.464
% Set threecolwid to be (3*onecolwid)+2*sepwid = 0.708
\setlength{\paperwidth}{54in} % A0 width: 46.8in
\setlength{\paperheight}{36in} % A0 height: 33.1in
 \setlength{\topmargin}{-0.5in} % Reduce the top margin size
\usepackage{graphicx}  % Required for including images
\usepackage{booktabs} % Top and bottom rules for tables 
\begin{document}
  
\begin{frame}[t] % The whole poster is enclosed in one beamer frame
 
\psset{xunit=1.6cm,yunit=.4cm,linewidth=3pt}
\psset{gradangle=135,gradmidpoint=0.5,framesep=6pt}  

\begin{pspicture}(-5, 80)(120, 240)
%\begin{pspicture}(-25, 80)(135, 240)
 

\psset{fillstyle=solid,fillcolor=linguist-fill4,framearc=0.5}
\psset{linecolor=linguist-line}
\psset{shadow=true}
 
  
 
\psframe[fillcolor=linguist-fill2,linestyle=none,framearc=0.5](-5,150)(25,245)   % Chicago sociology
\psframe[fillcolor=linguist-fill2,linestyle=none,framearc=0.5](27,150)(45,245)   % Columbia sociology
\psframe[fillcolor=linguist-fill2,linestyle=none,framearc=0.5](47,150)(65,245)   % Harvard sociology
\psframe[fillstyle=none,linecolor=black,linestyle=solid,framearc=0.5](58,180)(70,220)   % Harvard soc rel
%\psellipse[shadow=true,fillstyle=solid](-5,180)(10,10)  % Columbia ellipse
%\psellipse[shadow=true,fillstyle=solid](10.4,19)(3,10)  % Harvard ellipse
%\psellipse[shadow=true,fillstyle=solid](-15,160)(3,8)  % UChicago ellipse
%\psellipse[shadow=true,fillstyle=solid](-15,186)(3,4)  % bernard ogburn and chapin


%\psset{shadow=false}

   

"""


 

footer = """
\end{pspicture}
\end{frame}
\end{document}

"""

lastName = "lastName"
thisKey = "thisKey"
firstName = "firstName"
thisKey  = "thisKey"
xcoor = "xcoor"        
born = "born"
died = "died"
myLineColor = "myLineColor"
myProfession = "myProfession"

angleA="angleA"
armA="armA"
offsetA="offsetA"
angleB="angleB"
armB="armB"
offsetB="offsetB"
fromNode = "fromNode"
toNode = "toNode"


class People:
        def __init__(self):
                self.peopleList = list()
        def addPerson(self, thisPerson):
                self.peopleList.append(thisPerson)
         
       
class Person:

      
        
 
        def __init__ (self, facts):
                
                self.data = dict()
                for i in range(len(facts)):
                        fact = facts[i]
                        if fact[:4] == "key:":
                                self.data[thisKey] = fact[4:]
                                
                        else:
                                self.data[thisKey] = facts[2]  
                #print facts      
                #print self.data[thisKey], row, 228	
                self.data[firstName] = row[1]
                self.data[lastName] = row[2]
                self.data[born] = int(row[3])
                if len(row[4].strip()) > 0:
                        self.data[died] = int(row[4])
                else:
                        self.data[died] = ""
		#print row
                self.data[xcoor] = int(row[5])
                self.data[myProfession] = row[6]
                
class Links:
        def __init__(self):
                self.linkList = list()
        def addLink(self,thisLink):
                self.linkList.append(thisLink)

class Link:

        def __init__(self, facts):
                self.data=dict()
                self.data[fromNode] = row[1]
                self.data[toNode] = row[2]
                self.data[angleA]=row[3]
                self.data[armA]=row[4]
                self.data[offsetA]=row[5]
                self.data[angleB]=row[6]
                self.data[armB]=row[7]
                self.data[offsetB]=row[8]
                if len(facts) > 8 and False:
                        self.data[myLineColor]= row[9] 
                else:
                        self.data[myLineColor] = "black"

 


myPeople = People()
myLinks = Links()

with open (spreadsheet_name, 'r') as infile:
        genealogies = csv.reader(infile)
        for row in genealogies:
                if row[0]=="!":
                        outfile_name = row[1]
                if row[0]=="#":
                        continue
                if row[0] == "P":
                        p = Person(row)
                        myPeople.addPerson(p)
                elif row[0] == "L":
                        l = Link(row)
                        myLinks.addLink(l)

outfile_name_tex = outfile_name + ".tex"  
print "Outfile name", outfile_name_tex
outfile = file (outfile_name_tex, "w")
svg_outfile_name = outfile_name + ".html"
svg_outfile = file(svg_outfile_name, "w")
print >>outfile, header 
 

 
svgFormat = "<rect x=\"{0}\" y=\"{1}\" width=\"50\" height = \"50\", style=\"fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)\" /> " 
print >>svg_outfile, """<!DOCTYPE html>
<html>
<body>"""
print >>svg_outfile, "<svg width=\"2500\" height = \"2000\" >"


print >>outfile, "\\psset{fillstyle=gradient,gradmidpoint=.5,gradangle=45}" 
formatstring = "\\rput({0:>4},{1:<3}) {{\\rnode{{{2:13}}} {{\\psframebox[{3:25}]{{ \\begin{{tabular}}{{c}}   {4:>13} {5:<13} \\\\ {6}--{7} \\end{{tabular}} }} }} }} "
for person in myPeople.peopleList:    

        if len(person.data[thisKey])  == 0:
                person.data[thisKey] = person.data[lastName]
        #print person.data[lastName]
        ycoor = (person.data[born] - 1700)
        thisLastName = person.data[lastName]
        thisLastName =  "\Large{\\textsc{" + thisLastName + "} }"
        if person.data[myProfession]=="philosopher":
                color_string = "gradbegin=philosopher1,gradend=philosopher2,linecolor=philosopher3" 
        elif person.data[myProfession]=="psychologist":
                color_string = "gradbegin=psychologist1,gradend=psychologist2,linecolor=psychologist3" 
        elif person.data[myProfession]=="philpsych":
                color_string = "gradbegin=philosopher1,gradend=psychologist2,linecolor=psychologist3"
        elif  person.data[myProfession]=="sociologist":
                color_string = "gradbegin=sociologist1,gradend=sociologist2,linecolor=sociologist3"
        elif  person.data[myProfession] == "anthropologist":
                color_string = "gradbegin=anthropologist1, gradend=anthropologist2,linecolor=white"                
        elif  person.data[myProfession] == "mathematician":
                color_string = "gradbegin=mathematician1,gradend=mathematician2,linecolor=white"         
        elif  person.data[myProfession] == "logician":
                color_string = "gradbegin=logician1,gradend=logician2,linecolor=white"       
                #print person.data         
        else:
                color_string = "gradbegin=linguist1,gradend=linguist2,linecolor=linguist3"       
 
        print >>outfile, formatstring.format(person.data[xcoor],ycoor, person.data[thisKey], color_string,person.data[firstName],thisLastName,person.data[born], person.data[died])
        
       
        svgOut = svgFormat.format(str(float(person.data[xcoor])*20.0), ycoor*7)
        print >>svg_outfile, svgOut


print >>svg_outfile, "</svg>" 
print >>svg_outfile, "</body>"
print >>svg_outfile, "</html>"  

angleA="angleA"
armA="armA"
offsetA="offsetA"
angleB="angleB"
armB="armB"
offsetB="offsetB"
 
 
 
 

print >>outfile, "\\psset{linearc=0.5,linecolor=teacher}"

print >>outfile, "\\psset{fillstyle=none}"
 
for link in myLinks.linkList:
        thisAngleA = link.data[angleA]
        thisArmA = link.data[armA]
        thisOffsetA = link.data[offsetA]
        thisAngleB = link.data[angleB]
        thisArmB = link.data[armB]
        thisOffsetB = link.data[offsetB]
        thisLineStyle = "solid"
        thisLineColor = link.data[myLineColor]
        if thisLineColor=="postDoc":
                thisLineColor ="teacher"
                thisLineStyle = "dashed"
        formatstring = "\\ncangle[angleA={0:<3},armA={1:<4},offsetA={2:<5},angleB={3:<3},armB={4:<3},offsetB={5:<5},linecolor={6:<10},linestyle={7}]{{{8}}}{{{9}}}"
        print >>outfile, formatstring.format(thisAngleA, thisArmA,thisOffsetA,thisAngleB, thisArmB, thisOffsetB,thisLineColor,thisLineStyle,link.data[fromNode], link.data[toNode]) 


print >>outfile, footer
outfile.close()
