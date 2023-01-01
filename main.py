from selenium import webdriver
import tkinter as tk
from tkinter import *
from tkinter.ttk import Button
from PIL import ImageTk, Image
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
import time

temp = "!" ### TO DO:  resize windows so you dont need to scroll
raceName = "" ###ADD QUIT BUTTON TO CONSTRUCTORS AND DRIVERS AND RACE REULTS WINDOWS
def quit():
    window.destroy()  #

def getPageID(passedName):## change quit to .withdraw(need to figure out why this breaks browser.get) and call .quit from this func
    global raceName #remove quit from lambda
    global temp
   # window.destroy() # window.remove() or window.quit()
    raceName = passedName
    temp = raceDic[passedName]
    raceResults() #needs to be called after browser.get


def constructors():
    listC = []
    browser.get("https://www.espn.com/f1/standings/_/group/constructors")
    team1 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[1]/td[1]/div/span[4]')
    team2 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[2]/td[1]/div/span[4]')
    team3 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[3]/td[1]/div/span[4]')
    team4 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[4]/td[1]/div/span[4]')
    team5 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[5]/td[1]/div/span[4]')
    team6 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[6]/td[1]/div/span[4]')
    team7 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[7]/td[1]/div/span[4]')
    team8 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[8]/td[1]/div/span[4]')
    team9 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[9]/td[1]/div/span[4]')
    team10 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[10]/td[1]/div/span[4]')

    points1 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[1]/td[2]/span')
    points2 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[2]/td[2]/span')
    points3 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[3]/td[2]/span')
    points4 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[4]/td[2]/span')
    points5 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[5]/td[2]/span')
    points6 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[6]/td[2]/span')
    points7 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[7]/td[2]/span')
    points8 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[8]/td[2]/span')
    points9 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[9]/td[2]/span')
    points10 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[10]/td[2]/span')

    cteam1 = Teams('1', team1.text, points1.text)
    cteam2 = Teams('2', team2.text, points2.text)
    cteam3 = Teams('3', team3.text, points3.text)
    cteam4 = Teams('4', team4.text, points4.text)
    cteam5 = Teams('5', team5.text, points5.text)
    cteam6 = Teams('6', team6.text, points6.text)
    cteam7 = Teams('7', team7.text, points7.text)
    cteam8 = Teams('8', team8.text, points8.text)
    cteam9 = Teams('9', team9.text, points9.text)
    cteam10 = Teams('10', team10.text, points10.text)

    listC.append(cteam1)
    listC.append(cteam2)
    listC.append(cteam3)
    listC.append(cteam4)
    listC.append(cteam5)
    listC.append(cteam6)
    listC.append(cteam7)
    listC.append(cteam8)
    listC.append(cteam9)
    listC.append(cteam10)

    window = Tk()
    # window.deiconify()
    window.configure(bg='#E33D1A')  # change to conw
    window.title("Constructor Standings")

    posLabel = Label(window, text="Position")
    posLabel.grid(row=0, column=0)

    driverLabel = Label(window, text="Team Name")
    driverLabel.grid(row=0, column=4)

    pointLabel = Label(window, text="Points")
    pointLabel.grid(row=0, column=6)

    posTxt = Text(window, width=25, height=10)
    posTxt.grid(row=2, column=0)

    pointTxt = Text(window, width=25, height=10)
    pointTxt.grid(row=2, column=6)

    nameTxt = Text(window, width=25, height=10)
    nameTxt.grid(row=2, column=4)

    k = 1
    while k <= 10:
        for obj in listC:
            if int(obj.tposition) == k:
                posTxt.insert(INSERT, obj.tposition + "\n")
                nameTxt.insert(INSERT, obj.teamName + "\n")
                pointTxt.insert(INSERT, obj.teamPoints + "\n")
            # print(obj.pos, obj.name, "\t", obj.points, "\n")

        k += 1
    window.mainloop()

def raceResults():
    global list2
    global raceName
    browser.get(
        temp)  ##move to getPageID or create seperate func so this doesnt run if constructor results are seleceted
    # time.sleep(.5)
    Name1 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]/section/div/h2/span/span/span[2]')
    Name2 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[2]/td[2]/section/div/h2/span/span/span[2]')
    Name3 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[3]/td[2]/section/div/h2/span/span/span[2]')
    Name4 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[4]/td[2]/section/div/h2/span/span/span[2]')
    Name5 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[5]/td[2]/section/div/h2/span/span/span[2]')
    Name6 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[6]/td[2]/section/div/h2/span/span/span[2]')
    Name7 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[7]/td[2]/section/div/h2/span/span/span[2]')
    Name8 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[8]/td[2]/section/div/h2/span/span/span[2]')
    Name9 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[9]/td[2]/section/div/h2/span/span/span[2]')
    Name10 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[10]/td[2]/section/div/h2/span/span/span[2]')
    Name11 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[11]/td[2]/section/div/h2/span/span/span[2]')
    Name12 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[12]/td[2]/section/div/h2/span/span/span[2]')
    Name13 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[13]/td[2]/section/div/h2/span/span/span[2]')
    Name14 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[14]/td[2]/section/div/h2/span/span/span[2]')
    Name15 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[15]/td[2]/section/div/h2/span/span/span[2]')
    Name16 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[16]/td[2]/section/div/h2/span/span/span[2]')
    Name17 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[17]/td[2]/section/div/h2/span/span/span[2]')
    Name18 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[18]/td[2]/section/div/h2/span/span/span[2]')
    Name19 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[19]/td[2]/section/div/h2/span/span/span[2]')
    if (raceName != "Saudi Arabia"):
        Name20 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[20]/td[2]/section/div/h2/span/span/span[2]')

    # print(Name19.text)
    Team1 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[1]/td[3]')
    Team2 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[2]/td[3]')
    Team3 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[3]/td[3]')
    Team4 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[4]/td[3]')
    Team5 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[5]/td[3]')
    Team6 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[6]/td[3]')
    Team7 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[7]/td[3]')
    Team8 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[8]/td[3]')
    Team9 = browser.find_element('xpath',
                                 '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[9]/td[3]')
    Team10 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[10]/td[3]')
    Team11 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[11]/td[3]')
    Team12 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[12]/td[3]')
    Team13 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[13]/td[3]')
    Team14 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[14]/td[3]')
    Team15 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[15]/td[3]')
    Team16 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[16]/td[3]')
    Team17 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[17]/td[3]')
    Team18 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[18]/td[3]')
    Team19 = browser.find_element('xpath',
                                  '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[19]/td[3]')
    if(raceName != "Saudi Arabia"):
        Team20 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[20]/td[3]')

    P1 = Races('1', Name1.text, Team1.text)
    P2 = Races('2', Name2.text, Team2.text)
    P3 = Races('3', Name3.text, Team3.text)
    P4 = Races('4', Name4.text, Team4.text)
    P5 = Races('5', Name5.text, Team5.text)
    P6 = Races('6', Name6.text, Team6.text)
    P7 = Races('7', Name7.text, Team7.text)
    P8 = Races('8', Name8.text, Team8.text)
    P9 = Races('9', Name9.text, Team9.text)
    P10 = Races('10', Name10.text, Team10.text)
    P11 = Races('11', Name11.text, Team11.text)
    P12 = Races('12', Name12.text, Team12.text)
    P13 = Races('13', Name13.text, Team13.text)
    P14 = Races('14', Name14.text, Team14.text)
    P15 = Races('15', Name15.text, Team15.text)
    P16 = Races('16', Name16.text, Team16.text)
    P17 = Races('17', Name17.text, Team17.text)
    P18 = Races('18', Name18.text, Team18.text)
    P19 = Races('19', Name19.text, Team19.text)
    if (raceName != "Saudi Arabia"):
        P20 = Races('20', Name20.text, Team20.text)

    list2 = []
    list2.append(P1)
    list2.append(P2)
    list2.append(P3)
    list2.append(P4)
    list2.append(P5)
    list2.append(P6)
    list2.append(P7)
    list2.append(P8)
    list2.append(P9)
    list2.append(P10)
    list2.append(P11)
    list2.append(P12)
    list2.append(P13)
    list2.append(P14)
    list2.append(P15)
    list2.append(P16)
    list2.append(P17)
    list2.append(P18)
    list2.append(P19)
    if (raceName != "Saudi Arabia"):
        list2.append(P20)
    browser.close()

    window = Tk()
    #window.deiconify()
    window.configure(bg='#E33D1A') #change to conw
    window.title("Race Results for " + raceName + " Grand Prix\n")

    posLabel = Label(window, text="Position")
    posLabel.grid(row=0, column=0)

    driverLabel = Label(window, text="Driver Name")
    driverLabel.grid(row=0, column=4)

    pointLabel = Label(window, text="Team")
    pointLabel.grid(row=0, column=6)

    posTxt = Text(window, width=25, height=20)
    posTxt.grid(row=2, column=0)

    teamTxt = Text(window, width=25, height=20)
    teamTxt.grid(row=2, column=6)

    nameTxt = Text(window, width=25, height=20)
    nameTxt.grid(row=2, column=4)

    j = 1
    if (raceName != "Saudi Arabia"):
        o = 20
    else:
        o = 19
    while j <= o:
        for obj in list2:
            posTxt.insert(INSERT, obj.position + "\n")
            teamTxt.insert(INSERT, obj.team + "\n")
            nameTxt.insert(INSERT, obj.driverName + "\n")
            print(obj.position, obj.driverName, "\t", obj.team)
            j += 1
    window.mainloop()


def driverStandings():
    global list
    window = Tk()
    #window.deiconify()
    window.configure(bg='#E33D1A') #change to conw
    window.title("Driver Standings")

    posLabel = Label(window, text="Position")
    posLabel.grid(row=0, column=0)

    driverLabel = Label(window, text="Driver Name")
    driverLabel.grid(row=0, column=4)

    pointLabel = Label(window, text="Points")
    pointLabel.grid(row=0, column=6)

    posTxt = Text(window, width=25, height=20)
    posTxt.grid(row=2, column=0)

    pointTxt = Text(window, width=25, height=20)
    pointTxt.grid(row=2, column=6)

    nameTxt = Text(window, width=25, height=20)
    nameTxt.grid(row=2, column=4)

    k = 1
    while k <= 22:
        for obj in list:
            if int(obj.pos) == k:
                posTxt.insert(INSERT, obj.pos + "\n")
                nameTxt.insert(INSERT, obj.name + "\n")
                pointTxt.insert(INSERT, obj.points + "\n")
               # print(obj.pos, obj.name, "\t", obj.points, "\n")

        k += 1
    window.mainloop()


#def constructors():

class F1:
    def __init__(self, pos, name, points):
        self.name = name
        self. points = points
        self.pos = pos
        #self.racePos = racePos
        #self.team = team

class Races:
    def __init__(self, position, driverName, team):
        self.driverName = driverName
        self. team = team
        self.position = position


class Teams:
    def __init__(self, tposition, teamName, teamPoints):
        self.tposition = tposition
        self.teamName = teamName
        self.teamPoints = teamPoints


## either make array/ dictionary for each race and grab data at runtime OR, make one single array/ dictionary and populate after taking user input
## ex, "What race do you want to see?" User enters Brazil, then the program goes to espn, fills the single dictionary/ array with that data and returns it

if __name__ == '__main__':

    path = r'/Users/williamcassel/Desktop/CS_11_stuff/chromedriver'
    #from selenium.webdriver.chrome.service import Service

    #s = Service(path)
    #driver = webdriver.Chrome(service=s)
    #chrome_options = Options()
    #chrome_options.add_argument('--no-sandbox')
   # chrome_options.add_argument('--disable-dev-shm-usage')

    browser = webdriver.Chrome(path)
    browser.get("https://www.espn.com/f1/standings")
    #time.sleep()
    maxName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[1]/td[1]/div/span[4]')
    maxPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[1]/td[2]/span')
    maxPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[1]/td[1]/div/span[1]')
    #time.sleep(.5)
    charName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[2]/td[1]/div/span[4]')
    charPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[2]/td[2]/span')
    charPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[2]/td[1]/div/span[1]')

    sergName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[3]/td[1]/div/span[4]')
    sergPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[3]/td[2]/span')
    sergPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[3]/td[1]/div/span[1]')

    geoName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[4]/td[1]/div/span[4]')
    geoPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[4]/td[2]/span')
    geoPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[4]/td[1]/div/span[1]')

    carName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[5]/td[1]/div/span[4]')
    carPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[5]/td[2]/span')
    carPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[5]/td[1]/div/span[1]')

    lewName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[6]/td[1]/div/span[4]')
    lewPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[6]/td[2]/span')
    lewPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[6]/td[1]/div/span[1]')

    landName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[7]/td[1]/div/span[4]')
    landPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[7]/td[2]/span')
    landPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[7]/td[1]/div/span[1]')

    estName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[8]/td[1]/div/span[4]')
    estPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[8]/td[2]/span')
    estPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[8]/td[1]/div/span[1]')

    ferName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[9]/td[1]/div/span[4]')
    ferPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[9]/td[2]/span')
    ferPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[9]/td[1]/div/span[1]')

    botName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[10]/td[1]/div/span[4]')
    botPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[10]/td[2]/span')
    botPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[10]/td[1]/div/span[1]')

    pieName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[11]/td[1]/div/span[4]')
    piePoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[11]/td[2]/span')
    piePos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[11]/td[1]/div/span[1]')

    kevName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[12]/td[1]/div/span[4]')
    kevPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[12]/td[2]/span')
    kevPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[12]/td[1]/div/span[1]')

    sebName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[13]/td[1]/div/span[4]')
    sebPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[13]/td[2]/span')
    sebPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[13]/td[1]/div/span[1]')

    danName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[14]/td[1]/div/span[4]')
    danPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[14]/td[2]/span')
    danPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[14]/td[1]/div/span[1]')

    micName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[15]/td[1]/div/span[4]')
    micPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[15]/td[2]/span')
    micPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[15]/td[1]/div/span[1]')

    yukName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[16]/td[1]/div/span[4]')
    yukPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[16]/td[2]/span')
    yukPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[16]/td[1]/div/span[1]')

    guaName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[17]/td[1]/div/span[4]')
    guaPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[17]/td[2]/span')
    guaPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[17]/td[1]/div/span[1]')

    lanName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[18]/td[1]/div/span[4]')
    lanPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[18]/td[2]/span')
    lanPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[18]/td[1]/div/span[1]')

    aleName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[19]/td[1]/div/span[4]')
    alePoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[19]/td[2]/span')
    alePos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[19]/td[1]/div/span[1]')

    nycName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[20]/td[1]/div/span[4]')
    nycPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[20]/td[2]/span')
    nycPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[20]/td[1]/div/span[1]')

    nichName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[21]/td[1]/div/span[4]')
    nichPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[21]/td[2]/span')
    nichPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[21]/td[1]/div/span[1]')

    nicoName = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[22]/td[1]/div/span[4]')
    nicoPoints = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[22]/td[2]/span')
    nicoPos = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[3]/div/div/section/div/section/section/div[1]/div/div[2]/table/tbody/tr[22]/td[1]/div/span[1]')

    maxV = F1(maxPos.text, maxName.text, maxPoints.text)
    cha = F1(charPos.text, charName.text, charPoints.text)
    ser = F1(sergPos.text, sergName.text, sergPoints.text)
    geo = F1(geoPos.text, geoName.text, geoPoints.text)
    car = F1(carPos.text, carName.text, carPoints.text)
    lew = F1(lewPos.text, lewName.text, lewPoints.text)
    land = F1(landPos.text, landName.text, landPoints.text)
    est = F1(estPos.text, estName.text, estPoints.text)
    fer = F1(ferPos.text, ferName.text, ferPoints.text)
    bot = F1(botPos.text, botName.text, botPoints.text)
    bot = F1(botPos.text, botName.text, botPoints.text)
    pie = F1(piePos.text, pieName.text, piePoints.text)
    kev = F1(kevPos.text, kevName.text, kevPoints.text)
    seb = F1(sebPos.text, sebName.text, sebPoints.text)
    dan = F1(danPos.text, danName.text, danPoints.text)
    mic = F1(micPos.text, micName.text, micPoints.text)
    yuk = F1(yukPos.text, yukName.text, yukPoints.text)
    gua = F1(guaPos.text, guaName.text, guaPoints.text)
    lan = F1(lanPos.text, lanName.text, lanPoints.text)
    ale = F1(alePos.text, aleName.text, alePoints.text)
    nyc = F1(nycPos.text, nycName.text, nycPoints.text)
    nich = F1(nichPos.text, nichName.text, nichPoints.text)
    nico = F1(nicoPos.text, nicoName.text, nicoPoints.text)

    list = []
    list.append(maxV)
    list.append(cha)
    list.append(ser)
    list.append(geo)
    list.append(car)
    list.append(lew)
    list.append(land)
    list.append(est)
    list.append(fer)
    list.append(bot)
    list.append(pie)
    list.append(kev)
    list.append(seb)
    list.append(dan)
    list.append(mic)
    list.append(yuk)
    list.append(gua)
    list.append(lan)
    list.append(ale)
    list.append(nyc)
    list.append(nico)
    list.append(nich)

   # print("pos\tName\t\tPoints")
  #  i = 1
  #  while i <= 22:
  #      for obj in list:
  #          if int(obj.pos) == i:
   #             print(obj.pos, obj.name, "\t", obj.points)

   #     i += 1
    #browser.close()
    raceDic = { "Bahrain": "https://www.espn.com/f1/results?id=600014127",
                "Saudi Arabia": "https://www.espn.com/f1/results?id=600014128",
                "Australia": "https://www.espn.com/f1/results?id=600014129",
                "Emilia Romagna": "https://www.espn.com/f1/results?id=600014130",
                "Miami": "https://www.espn.com/f1/results?id=600014131",
                "Barcelona": "https://www.espn.com/f1/results?id=600014132", ####
                "Monaco": "https://www.espn.com/f1/results?id=600014133",  ####
                "Azerbaijan": "https://www.espn.com/f1/results?id=600014134",
                "Canada": "https://www.espn.com/f1/results?id=600014135",
                "Britian": "https://www.espn.com/f1/results?id=600014136",
                "Austrian": "https://www.espn.com/f1/results?id=600014137",
                "French": "https://www.espn.com/f1/results?id=600014138",
                "Hungarian": "https://www.espn.com/f1/results?id=600014139",
                "Belgian": "https://www.espn.com/f1/results?id=600014140",
                "Dutch": "https://www.espn.com/f1/results?id=600014141",
                "Italian": "https://www.espn.com/f1/results?id=600014142",
                "Russian": "https://www.espn.com/f1/results?id=600014143",
                "Singapore": "https://www.espn.com/f1/results?id=600014144",
                "Japan": "https://www.espn.com/f1/results?id=600014145",
                "United States": "https://www.espn.com/f1/results?id=600014146",
                "Mexico": "https://www.espn.com/f1/results?id=600014147",
                "Brazil": "https://www.espn.com/f1/results?id=600014148",
                "Abu Dhabi": "https://www.espn.com/f1/results?id=600014149"}

    window = Tk()
    window.configure(bg='#E33D1A')
    window.title("Formula 1 Races - 2022 Season")

    bahrainImage = Image.open("Bahrain.png")
    bahrainImageR = bahrainImage.resize((75, 75))
    bahrainImg = ImageTk.PhotoImage(bahrainImageR)

    saudiImage = Image.open("Saudi.png")
    saudiImageR = saudiImage.resize((75, 75))
    saudiImg = ImageTk.PhotoImage(saudiImageR)

    ausImage = Image.open("Australia.png") #set ausImage to the png
    ausImageR = ausImage.resize((75, 75)) #set ausImageR to the resized PNG
    ausImg = ImageTk.PhotoImage(ausImageR) #set ausImg to be a tkinter image

    emilImage = Image.open("Emilia.png")
    emilImageR = emilImage.resize((75, 75))
    emilImg = ImageTk.PhotoImage(emilImageR)

    miamiImage = Image.open("Miami.png")
    miamiImageR = miamiImage.resize((75, 75))
    miamiImg = ImageTk.PhotoImage(miamiImageR)

    barcImage = Image.open("Barcelona.png")
    barcImageR = barcImage.resize((75, 75))
    barcImg = ImageTk.PhotoImage(barcImageR)

    azeImage = Image.open("Azerbaijan.jpg")
    azeImageR = azeImage.resize((75, 75))
    azeImg = ImageTk.PhotoImage(azeImageR)

    canImage = Image.open("Canadian.png")
    canImageR = canImage.resize((75, 75))
    canImg = ImageTk.PhotoImage(canImageR)

    briImage = Image.open("Britian.png")
    briImageR = briImage.resize((75, 75))
    briImg = ImageTk.PhotoImage(briImageR) #austrian, fren, hung

    austImage = Image.open("Austrian2.png")
    austImageR = austImage.resize((75, 75))
    austImg = ImageTk.PhotoImage(austImageR)

    freImage = Image.open("French.png")
    freImageR = freImage.resize((75, 75))
    freImg = ImageTk.PhotoImage(freImageR)

    hunImage = Image.open("Hungarian.png")
    hunImageR = hunImage.resize((75, 75))
    hunImg = ImageTk.PhotoImage(hunImageR) #bel, dutch, ital

    belImage = Image.open("Belgian.png")
    belImageR = belImage.resize((75, 75))
    belImg = ImageTk.PhotoImage(belImageR)

    dutImage = Image.open("Dutch.jpg")
    dutImageR = dutImage.resize((75, 75))
    dutImg = ImageTk.PhotoImage(dutImageR)

    italImage = Image.open("Italian.png")
    italImageR = italImage.resize((75, 75))
    italImg = ImageTk.PhotoImage(italImageR)#rus, sing, japan

    rusImage = Image.open("Russian2.png")
    rusImageR = rusImage.resize((75, 75))
    rusImg = ImageTk.PhotoImage(rusImageR)

    sinImage = Image.open("Singapore.png")
    sinImageR = sinImage.resize((75, 75))
    sinImg = ImageTk.PhotoImage(sinImageR)

    jaImage = Image.open("Japan.jpg")
    jaImageR = jaImage.resize((75, 75))
    jaImg = ImageTk.PhotoImage(jaImageR) #us, mex, bra

    usImage = Image.open("US.png")
    usImageR = usImage.resize((75, 75))
    usImg = ImageTk.PhotoImage(usImageR)

    mexImage = Image.open("Mexico.png")
    mexImageR = mexImage.resize((75, 75))
    mexImg = ImageTk.PhotoImage(mexImageR)

    braImage = Image.open("Brazil.png")
    braImageR = braImage.resize((75, 75))
    braImg = ImageTk.PhotoImage(braImageR) #brit dutch us

    teamImage = Image.open("TeamGraphic.jpg")
    teamImageR = teamImage.resize((75, 75))
    teamImg = ImageTk.PhotoImage(teamImageR)

    BahrainButton = tk.Button(window, text="Bahrain",image=bahrainImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Bahrain")]) #command=nextLine add .image
    BahrainButton.grid(row=0, column=0, sticky="NSEW") # sticky=W
    SAButton = tk.Button(window, text="Saudi", image=saudiImg, compound=TOP, highlightthickness=0, bd=0, command=lambda:[quit(), getPageID("Saudi Arabia")])
    SAButton.grid(row=0, column=1, sticky="nsew")
    AusButton = tk.Button(window, text="Austrialia", image=ausImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Australia")])
    AusButton.grid(row=0, column=2, sticky="nsew")
    EmilButton = tk.Button(window, text ="Emilia", image=emilImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Emilia Romagna")])
    EmilButton.grid(row=0, column=3, sticky="nsew")
    MiamiButton = tk.Button(window, text="Miami", image=miamiImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Miami")])
    MiamiButton.grid(row=0, column=4, sticky="nsew")
    BarcButton = tk.Button(window, text = "Barcelona", image=barcImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Barcelona")])
    BarcButton.grid(row=1, column=0)


    #img = ImageTk.PhotoImage(Image.open(path))
    #originalImg = Image.open(currentphotofolderPath + file)
   # monacoImage = ImageTk.PhotoImage(Image.open('monaco.jpg')) #works
    monacoImage = Image.open("monaco.jpg")
    MonImgR = monacoImage.resize((75, 75))
    MonImg = ImageTk.PhotoImage(MonImgR)

    abuImage = Image.open("Abu.png")  #these three lines are for resizing the image so it fits properly
    abuImageR = abuImage.resize((75, 75))
    abuImg = ImageTk.PhotoImage(abuImageR)

    #MonButton = Button(window, text="Monaco", command=lambda: [getPageID("Monaco"), quit()]) #image="monaco.jpeg", compound=TOP
    MonButton = tk.Button(window, text="Monaco", image=MonImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Monaco")])
    MonButton.grid(row=1, column =1)

    AzeButton = tk.Button(window, text="Azerbaijan", image=azeImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Azerbaijan")])
    AzeButton.grid(row=1, column=2)
    CanButton = tk.Button(window, text="Canada", image=canImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Canada")])
    CanButton.grid(row=1, column=3)
    BritButton = tk.Button(window, text="Britian", image=briImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Britian")])
    BritButton.grid(row=1, column=4, sticky=W)
    AustButton = tk.Button(window, text="Austria", image=austImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Austrian")])
    AustButton.grid(row=2, column=0)
    FreButton = tk.Button(window, text="France", image=freImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("French")])
    FreButton.grid(row=2, column=1)
    hungButton = tk.Button(window, text="Hungary", image=hunImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Hungarian")])
    hungButton.grid(row=2, column=2)
    BelButton = tk.Button(window, text="Belgian", image=belImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Belgian")])
    BelButton.grid(row=2, column=3)
    DutchButton = tk.Button(window, text="Dutch",  image=dutImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Dutch")])
    DutchButton.grid(row=2, column=4, sticky=W)
    ItalButton = tk.Button(window, text="Italy", image=italImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Italian")])
    ItalButton.grid(row=3, column=0)
    RusButton = tk.Button(window, text="Russia", image=rusImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Russian")])
    RusButton.grid(row=3, column=1)
    SinButton = tk.Button(window, text="Singapore", image=sinImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Singapore")])
    SinButton.grid(row=3, column=2)
    jaButton = tk.Button(window, text="Japan", image=jaImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Japan")])
    jaButton.grid(row=3, column=3)
    USButton = tk.Button(window, text="U.S.", image=usImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("United States")])
    USButton.grid(row=3, column=4, sticky=W)
    MexButton = tk.Button(window, text="Mexico", image=mexImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Mexico")])
    MexButton.grid(row=4, column=0)
    BraButton = tk.Button(window, text="Brazil", image=braImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Brazil")])
    BraButton.grid(row=4, column=1)
    AbuButton = tk.Button(window, text="Abu Dhabi", image=abuImg, compound=TOP, highlightthickness=0, bd=0, command=lambda: [quit(), getPageID("Abu Dhabi")])
    AbuButton.grid(row=4, column=2)
    #quitButton = Button(window, text="Quit", command=quit)
    #quitButton.grid(row=4, column=4)
    TeamButton = tk.Button(window, text="Drivers", image=teamImg, compound=TOP, highlightthickness=0, bd=0,
                          command=lambda: [quit(), driverStandings()])
    TeamButton.grid(row=4, column=3)

    Team2Button = tk.Button(window, text="Teams", image=teamImg, compound=TOP, highlightthickness=0, bd=0,
                          command=lambda: [quit(), constructors()])
    Team2Button.grid(row=4, column=4)

    window.mainloop()
    """ 
    browser.get(temp) ##move to getPageID or create seperate func so this doesnt run if constructor results are seleceted
   # time.sleep(.5)
    Name1 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]/section/div/h2/span/span/span[2]')
    Name2 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[2]/td[2]/section/div/h2/span/span/span[2]')
    Name3 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[3]/td[2]/section/div/h2/span/span/span[2]')
    Name4 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[4]/td[2]/section/div/h2/span/span/span[2]')
    Name5 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[5]/td[2]/section/div/h2/span/span/span[2]')
    Name6 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[6]/td[2]/section/div/h2/span/span/span[2]')
    Name7 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[7]/td[2]/section/div/h2/span/span/span[2]')
    Name8 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[8]/td[2]/section/div/h2/span/span/span[2]')
    Name9 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[9]/td[2]/section/div/h2/span/span/span[2]')
    Name10 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[10]/td[2]/section/div/h2/span/span/span[2]')
    Name11 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[11]/td[2]/section/div/h2/span/span/span[2]')
    Name12 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[12]/td[2]/section/div/h2/span/span/span[2]')
    Name13 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[13]/td[2]/section/div/h2/span/span/span[2]')
    Name14 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[14]/td[2]/section/div/h2/span/span/span[2]')
    Name15 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[15]/td[2]/section/div/h2/span/span/span[2]')
    Name16 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[16]/td[2]/section/div/h2/span/span/span[2]')
    Name17 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[17]/td[2]/section/div/h2/span/span/span[2]')
    Name18 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[18]/td[2]/section/div/h2/span/span/span[2]')
    Name19 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[19]/td[2]/section/div/h2/span/span/span[2]')
   # try: #MUST FIX
    Name20 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[20]/td[2]/section/div/h2/span/span/span[2]')
    #except():
     #   pass #print("No 20th driver for this race\n")

   # print(Name19.text)
    Team1 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[1]/td[3]')
    Team2 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[2]/td[3]')
    Team3 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[3]/td[3]')
    Team4 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[4]/td[3]')
    Team5 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[5]/td[3]')
    Team6 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[6]/td[3]')
    Team7 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[7]/td[3]')
    Team8 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[8]/td[3]')
    Team9 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[9]/td[3]')
    Team10 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[10]/td[3]')
    Team11 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[11]/td[3]')
    Team12 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[12]/td[3]')
    Team13 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[13]/td[3]')
    Team14 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[14]/td[3]')
    Team15 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[15]/td[3]')
    Team16 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[16]/td[3]')
    Team17 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[17]/td[3]')
    Team18 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[18]/td[3]')
    Team19 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[19]/td[3]')
    Team20 = browser.find_element('xpath', '/html/body/div[1]/div/div/div/main/div[2]/div/div[5]/div/div/div[1]/section/div/div/div/div/div[2]/table/tbody/tr[20]/td[3]')
   # print(Team3.text)

    P1 = Races('1', Name1.text, Team1.text)
    P2 = Races('2', Name2.text, Team2.text)
    P3 = Races('3', Name3.text, Team3.text)
    P4 = Races('4', Name4.text, Team4.text)
    P5 = Races('5', Name5.text, Team5.text)
    P6 = Races('6', Name6.text, Team6.text)
    P7 = Races('7', Name7.text, Team7.text)
    P8 = Races('8', Name8.text, Team8.text)
    P9 = Races('9', Name9.text, Team9.text)
    P10 = Races('10', Name10.text, Team10.text)
    P11 = Races('11', Name11.text, Team11.text)
    P12 = Races('12', Name12.text, Team12.text)
    P13 = Races('13', Name13.text, Team13.text)
    P14 = Races('14', Name14.text, Team14.text)
    P15 = Races('15', Name15.text, Team15.text)
    P16 = Races('16', Name16.text, Team16.text)
    P17 = Races('17', Name17.text, Team17.text)
    P18 = Races('18', Name18.text, Team18.text)
    P19 = Races('19', Name19.text, Team19.text)
    P20 = Races('20', Name20.text, Team20.text)

    list2 = []
    list2.append(P1)
    list2.append(P2)
    list2.append(P3)
    list2.append(P4)
    list2.append(P5)
    list2.append(P6)
    list2.append(P7)
    list2.append(P8)
    list2.append(P9)
    list2.append(P10)
    list2.append(P11)
    list2.append(P12)
    list2.append(P13)
    list2.append(P14)
    list2.append(P15)
    list2.append(P16)
    list2.append(P17)
    list2.append(P18)
    list2.append(P19)
    list2.append(P20)
    browser.close()
    #print(list2)
    print("Race results for " + raceName + " Grand Prix\n")
    print("Pos\tName\t\tTeam")
    j = 1
    while j <= 20:
        for obj in list2:
            print(obj.position, obj.driverName, "\t", obj.team)
            j += 1
    #constructors()
"""
#window.deiconify()
   # quitButton = Button(window, text="Quit", command=quit)
    #quitButton.grid(row=5, column=6, sticky=E)
    #browser.close()
    #constructors()
## Finding Elements

#google_text = driver.find_element(By.CLASS_NAME, "MV3Tnb").text

#print(google_text)

#input_box = driver.find_element(By.NAME, "q")

## Typing and Clicking

#input_box.send_keys("Hi")

#input_box.send_keys(Keys.ENTER)

#home_link = driver.find_element(By.ID, "logo")

#home_link.click()

## Selectors

#tag_search = driver.find_element(By.TAG_NAME, "a").text

#print(tag_search)

#link_text = driver.find_element(By.LINK_TEXT, "About").text

#print(link_text)