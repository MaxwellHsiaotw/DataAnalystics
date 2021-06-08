import tkinter as tk
import csv
from tkinter import Tk,Frame
from tkinter import *
from tkinter.ttk import Treeview
from PIL import Image,ImageTk

c = ''
a = 'TOR'
b = 'BOS'
TEAM = 'CLE'

TOPIC_FONT = ("Times New Roman", 20)
LARGE_FONT = ("Verdana", 12)

temp = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\map.gif')
width = 1000
ratio = float(width) / temp.size[0]
height = int(temp.size[1] * ratio)


class NBABOOM(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("NBA BOOOM")
        self.geometry('1000x' + str(height))
        self.resizable(False, False)

        container = tk.Frame(self)

        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (StartPage, SearchPage, PageTwo, TeamMap, Results, Results2, Predictions):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 1, column = 1, sticky = "nsew")
        
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        return frame

#初始頁
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        bettinglabel = tk.Label(self, text = "BETTING ON THE NBA!", font = ("Times New Roman", 65))
        bettinglabel.place(x = 40, y = 100, anchor = "nw")


        #button = tk.Button(self, text = "Play now",
        #                   command = lambda: controller.show_frame(SearchPage))
        #button.pack()

        join = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\join-now.png')
        join1 = join.resize((300, 141), Image.ANTIALIAS)
        self.JOIN = ImageTk.PhotoImage(join1)
        self.JOINlogo = tk.Button(self, image = self.JOIN, bd = 0,
                                   command = lambda: controller.show_frame(SearchPage))
        self.JOINlogo.place (x = 350, y = 300, anchor = "nw")

#搜尋頁面
class SearchPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        join = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\NBA.png')
        join1 = join.resize((1000, 600), Image.ANTIALIAS)
        self.JOIN = ImageTk.PhotoImage(join1)
        self.JOINlogo = tk.Button(self, image = self.JOIN, bd = 0)
        self.JOINlogo.place(x = 0, y = 0)

        label = tk.Label(self, text = "  NBA Predictor  ", font = ("Times New Roman", 40) , bd = 0, bg = '#ffffff')
        label.place(x = 1, y = 80)

        button1 = tk.Button(self, text = "Search by teams", font = ("Times New Roman", 30), activebackground = '#e00700', bg = '#e00700',
                            command = lambda: controller.show_frame(TeamMap))
        button1.place(x = 50, y = 260)

        button2 = tk.Button(self, text = "  Search by date  ", font = ("Times New Roman", 30), activebackground = '#0067b0', bg = '#0067b0',
                            command = lambda: controller.show_frame(PageTwo))
        button2.place(x = 650, y = 260)    

#地圖頁面
class TeamMap(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        im = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\map.gif')
        im = im.resize((width, height), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(im)
        cv = tk.Canvas(self,width = 1000,height = 630)
        cv.grid(row = 0, column = 0, rowspan = 5, columnspan = 5, sticky = 'nsew')
        cv.create_image(0, 0, image = self.photo, anchor = 'nw')

#Eastern-Atlantic
        tor = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\TOR.png')
        tor1 = tor.resize((57, 57), Image.ANTIALIAS)
        self.TOR = ImageTk.PhotoImage(tor1)
        self.TORlogo = tk.Button(self, image = self.TOR, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('TOR'))
        self.TORlogo.place(x = 755, y = 126, anchor = "nw")

        bos = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\BOS.png')
        bos1 = bos.resize((55, 55), Image.ANTIALIAS)
        self.BOS = ImageTk.PhotoImage(bos1)
        self.BOSlogo = tk.Button(self, image = self.BOS, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('BOS'))
        self.BOSlogo.place(x = 910, y = 120, anchor = "nw")

        phi = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\PHI.png')
        phi1 = phi.resize((55, 55), Image.ANTIALIAS)
        self.PHI = ImageTk.PhotoImage(phi1)
        self.PHIlogo = tk.Button(self, image = self.PHI, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('PHI'))
        self.PHIlogo.place(x = 785, y = 190, anchor = "nw")

        nyk = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\NYK.png')
        nyk1 = nyk.resize((55, 55), Image.ANTIALIAS)
        self.NYK = ImageTk.PhotoImage(nyk1)
        self.NYKlogo = tk.Button(self, image = self.NYK, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('NYK'))
        self.NYKlogo.place(x = 838, y = 156, anchor = "nw")

        bkn = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\BKN.png')
        bkn1 = bkn.resize((55, 55), Image.ANTIALIAS)
        self.BKN = ImageTk.PhotoImage(bkn1)
        self.BKNlogo = tk.Button(self, image = self.BKN, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('BKN'))
        self.BKNlogo.place(x = 888, y = 188, anchor = "nw")

#Eastern-Central
        cle = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\CLE.png')
        cle1 = cle.resize((55, 55), Image.ANTIALIAS)
        self.CLE = ImageTk.PhotoImage(cle1)
        self.CLElogo = tk.Button(self, image = self.CLE, width = 50, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('CLE'))
        self.CLElogo.place(x = 715, y = 200, anchor = "nw")

        ind = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\IND.png')
        ind1 = ind.resize((55, 55), Image.ANTIALIAS)
        self.IND = ImageTk.PhotoImage(ind1)
        self.INDlogo = tk.Button(self, image = self.IND, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('IND'))
        self.INDlogo.place(x = 670, y = 240, anchor = "nw")

        mil = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\MIL.png')
        mil1 = mil.resize((55, 55), Image.ANTIALIAS)
        self.MIL = ImageTk.PhotoImage(mil1)
        self.MILlogo = tk.Button(self, image = self.MIL, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('MIL'))
        self.MILlogo.place(x = 605, y = 120, anchor = "nw")

        det = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\DET.png')
        det1 = det.resize((55, 55), Image.ANTIALIAS)
        self.DET = ImageTk.PhotoImage(det1)
        self.DETlogo = tk.Button(self, image = self.DET, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('DET'))
        self.DETlogo.place(x = 680, y = 133, anchor = "nw")

        chi= Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\CHI.png')
        chi1 = chi.resize((55, 55), Image.ANTIALIAS)
        self.CHI = ImageTk.PhotoImage(chi1)
        self.CHIlogo = tk.Button(self, image = self.CHI, width = 30, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('CHI'))
        self.CHIlogo.place(x = 620, y = 218, anchor = "nw")

#Eastern-Southeast
        mia = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\MIA.png')
        mia1 = mia.resize((55, 55), Image.ANTIALIAS)
        self.MIA = ImageTk.PhotoImage(mia1)
        self.MIAlogo = tk.Button(self, image = self.MIA, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('MIA'))
        self.MIAlogo.place(x = 820, y = 540, anchor = "nw")

        was = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\WAS.png')
        was1 = was.resize((55, 55), Image.ANTIALIAS)
        self.WAS = ImageTk.PhotoImage(was1)
        self.WASlogo = tk.Button(self, image = self.WAS, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('WAS'))
        self.WASlogo.place(x = 840, y = 245, anchor = "nw")

        cha = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\CHA.png')
        cha1 = cha.resize((55, 55), Image.ANTIALIAS)
        self.CHA = ImageTk.PhotoImage(cha1)
        self.CHAlogo = tk.Button(self, image = self.CHA, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('CHA'))
        self.CHAlogo.place(x = 805, y = 318, anchor = "nw")

        orl = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\ORL.png')
        orl1 = orl.resize((55, 55), Image.ANTIALIAS)
        self.ORL = ImageTk.PhotoImage(orl1)
        self.ORLlogo = tk.Button(self, image = self.ORL, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('ORL'))
        self.ORLlogo.place(x = 788, y = 472, anchor = "nw")

        atl = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\ATL.png')
        atl1 = atl.resize((55, 55), Image.ANTIALIAS)
        self.ATL = ImageTk.PhotoImage(atl1)
        self.ATLlogo = tk.Button(self, image = self.ATL, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('ATL'))
        self.ATLlogo.place(x = 730, y = 360, anchor = "nw")

#Western-Northwest
        por = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\POR.png')
        por1 = por.resize((55, 55), Image.ANTIALIAS)
        self.POR = ImageTk.PhotoImage(por1)
        self.PORlogo = tk.Button(self, image = self.POR, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('POR'))
        self.PORlogo.place(x = 45, y = 95, anchor = "nw")

        okc = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\OKC.png')
        okc1 = okc.resize((55, 55), Image.ANTIALIAS)
        self.OKC = ImageTk.PhotoImage(okc1)
        self.OKClogo = tk.Button(self, image = self.OKC, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('OKC'))
        self.OKClogo.place(x = 455, y = 333, anchor = "nw")

        uta = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\UTA.png')
        uta1 = uta.resize((55, 55), Image.ANTIALIAS)
        self.UTA = ImageTk.PhotoImage(uta1)
        self.UTAlogo = tk.Button(self, image = self.UTA, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('UTA'))
        self.UTAlogo.place(x = 180, y = 221, anchor = "nw")

        min = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\MIN.png')
        min1 = min.resize((55, 55), Image.ANTIALIAS)
        self.MIN = ImageTk.PhotoImage(min1)
        self.MINlogo = tk.Button(self, image = self.MIN, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('MIN'))
        self.MINlogo.place(x = 513, y = 108, anchor = "nw")

        den = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\DEN.png')
        den1 = den.resize((55, 55), Image.ANTIALIAS)
        self.DEN = ImageTk.PhotoImage(den1)
        self.DENlogo = tk.Button(self, image = self.DEN, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('DEN'))
        self.DENlogo.place(x = 318, y = 253, anchor = "nw")

#Western-Pacific
        gsw = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\GSW.png')
        gsw1 = gsw.resize((55, 55), Image.ANTIALIAS)
        self.GSW = ImageTk.PhotoImage(gsw1)
        self.GSWlogo = tk.Button(self, image = self.GSW, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('GSW'))
        self.GSWlogo.place(x = 20, y = 255, anchor = "nw")

        lac = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\LAC.png')
        lac1 = lac.resize((55, 55), Image.ANTIALIAS)
        self.LAC = ImageTk.PhotoImage(lac1)
        self.LAClogo = tk.Button(self, image = self.LAC, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('LAC'))
        self.LAClogo.place(x = 90, y = 285, anchor = "nw")

        lal = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\LAL.png')
        lal1 = lal.resize((55, 55), Image.ANTIALIAS)
        self.LAL = ImageTk.PhotoImage(lal1)
        self.LALlogo = tk.Button(self, image = self.LAL, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('LAL'))
        self.LALlogo.place(x = 85, y = 340, anchor = "nw")

        phx = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\PHX.png')
        phx1 = phx.resize((55, 55), Image.ANTIALIAS)
        self.PHX = ImageTk.PhotoImage(phx1)
        self.PHXlogo = tk.Button(self, image = self.PHX, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('PHX'))
        self.PHXlogo.place(x = 180, y = 361, anchor = "nw")

        sac = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\SAC.png')
        sac1 = sac.resize((55, 55), Image.ANTIALIAS)
        self.SAC = ImageTk.PhotoImage(sac1)
        self.SAClogo = tk.Button(self, image = self.SAC, height = 50, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('SAC'))
        self.SAClogo.place(x = 52, y = 177, anchor = "nw")

#Western-Southwest
        hou = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\HOU.png')
        hou1 = hou.resize((55, 55), Image.ANTIALIAS)
        self.HOU = ImageTk.PhotoImage(hou1)
        self.HOUlogo = tk.Button(self, image = self.HOU, height = 35, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('HOU'))
        self.HOUlogo.place(x = 480, y = 480, anchor = "nw")

        nor = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\NOR.png')
        nor1 = nor.resize((55, 55), Image.ANTIALIAS)
        self.NOR = ImageTk.PhotoImage(nor1)
        self.NORlogo = tk.Button(self, image = self.NOR, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('NOR'))
        self.NORlogo.place(x = 608, y = 473, anchor = "nw")

        sas = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\SAS.png')
        sas1 = sas.resize((55, 55), Image.ANTIALIAS)
        self.SAS = ImageTk.PhotoImage(sas1)
        self.SASlogo = tk.Button(self, image = self.SAS, width = 40, height = 30, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('SAS'))
        self.SASlogo.place(x = 400, y = 492, anchor = "nw")

        dal = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\DAL.png')
        dal1 = dal.resize((55, 55), Image.ANTIALIAS)
        self.DAL = ImageTk.PhotoImage(dal1)
        self.DALlogo = tk.Button(self, image = self.DAL, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('DAL'))
        self.DALlogo.place(x = 445, y = 410, anchor = "nw")

        mem = Image.open ('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\MEM.png')
        mem1 = mem.resize((55, 55), Image.ANTIALIAS)
        self.MEM = ImageTk.PhotoImage(mem1)
        self.MEMlogo = tk.Button(self, image = self.MEM, bg = 'SlateGray1', activebackground = 'SlateGray1', bd = 0, command = lambda: self.f('MEM'))
        self.MEMlogo.place(x = 592, y = 333, anchor = "nw")

        button1 = tk.Button(self, text = "Back to Home", width = 15, command = lambda: controller.show_frame(StartPage))
        button1.place(x = 600, y = 10, anchor = 'nw')        

    def f(self, content):
        TEAM = content
        frame = self.controller.show_frame(Results2)
        frame.onChangePage(self.controller, TEAM)
        
#日期頁面
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "Choose your date", font = TOPIC_FONT)
        label.pack(pady = 10, padx = 10)

        label1 = tk.Label(self, text = "Month(MM)")
        self.E1 = tk.Entry(self, bd = 5)

        label2 = tk.Label(self, text = "Day(DD)")
        self.E2 = tk.Entry(self, bd = 5)

        label3 = tk.Label(self, text = "Year(YYYY)")
        self.E3 = tk.Entry(self, bd = 5)

        submit1 = tk.Button(self, text = "Submit", command = lambda: self.submit())

        label1.pack ()
        self.E1.pack ()
        label2.pack ()
        self.E2.pack ()
        label3.pack ()
        self.E3.pack ()
        submit1.pack ( )

        button1 = tk.Button(self, text = "Back to Home", command = lambda: controller.show_frame(StartPage))
        button1.pack()
        
    def submit(self):
        a = self.E1.get()
        b = self.E2.get()
        c = self.E3.get()
        date = c + '/' + a + '/' + b
        frame = self.controller.show_frame(Results)
        frame.onChangePage(self.controller, date) 
                
#日期的結果頁
class Results(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

#「固定」button-return to homepage
        button1 = tk.Button(self, text = "Return to Home Page", font = ('Papyrus',20), command = self.omg)
        button1.place(x = 700, y = 0, anchor = 'nw')        
        # self.onChangePage(controller)

#由回傳的日期去CSV檔裡撈資料
    def onChangePage(self, controller, _a):        
        fh = open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\file\\每日賽程.csv', 'r', newline = '', encoding = 'utf-8')
        reader = csv.DictReader(fh)
        date = []
        awayteam = []
        hometeam = []
        Team = {'Toronto Raptors': 'TOR', 'Boston Celtics': 'BOS', 'Philadelphia 76ers': 'PHI',
                'Cleveland Cavaliers': 'CLE', 'Indiana Pacers': 'IND', 'Miami Heat': 'MIA',
                'Milwaukee Bucks': 'MIL', 'Washington Wizards': 'WAS', 'Detroit Pistons': 'DET',
                'Charlotte Hornets': 'CHA', 'New York Knicks': 'NYK', 'Brooklyn Nets': 'BKN',
                'Chicago Bulls': 'CHI', 'Orlando Magic': 'ORL', 'Atlanta Hawks': 'ATL', 'Houston Rockets': 'HOU',
                'Golden State Warriors': 'GSW', 'Portland Trail Blazers': 'POR', 'Oklahoma City Thunder': 'OKC',
                'Utah Jazz': 'UTA', 'New Orleans Pelicans': 'NOR', 'San Antonio Spurs': 'SAS',
                'Minnesota Timberwolves': 'MIN', 'Denver Nuggets': 'DEN', 'Los Angeles Clippers': 'LAC',
                'Los Angeles Lakers': 'LAL', 'Sacramento Kings': 'SAC', 'Dallas Mavericks': 'DAL',
                'Memphis Grizzlies': 'MEM', 'Phoenix Suns': 'PHO'}
        j = 0
        for row in reader:
            if j == 5:
                break
            if row['Date'] == _a:
                date.append(row['Date'])
                awayteam.append(Team[row['Visitor/Neutral']])
                hometeam.append(Team[row['Home/Neutral']])
                j += 1

        fh.close ()
        i = len(date)

#結果=0場
        if i == 0 :
            self.label = tk.Label(self, text = "NO  RESULTS!", font = ('Times New Roman', 60))
            self.label.place(x = 200, y = 200, anchor = 'nw')

#結果=1場
        if i >= 1:

#label-time            
            time = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\time.jpg')
            time1 = time.resize((150, 60), Image.ANTIALIAS)
            self.TIME = ImageTk.PhotoImage(time1)
            self.TIMElogo = tk.Label(self, image = self.TIME, bd = 0)
            self.TIMElogo.place(x = 10, y = 40, anchor = "nw")

#label-event
            event = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\events.jpg')
            event1 = event.resize((150, 60), Image.ANTIALIAS)
            self.EVENT = ImageTk.PhotoImage(event1)
            self.EVENTlogo = tk.Label(self, image = self.EVENT, bd = 0)
            self.EVENTlogo.place(x = 200, y = 40, anchor = "nw")

#label-predictions
            predictions = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\predictions.jpg')
            predictions1 = predictions.resize((150, 60), Image.ANTIALIAS)
            self.PREDICTIONS = ImageTk.PhotoImage(predictions1)
            self.PREDICTIONSlogo = tk.Label(self, image = self.PREDICTIONS, bd = 0)
            self.PREDICTIONSlogo.place (x = 400, y = 40, anchor = "nw")

#button-predictions
            button2 = tk.Button(self, text = "Predictions", font = ('Papyrus', 20),
                                  command = lambda: self.click(awayteam[0], hometeam[0], date[0]))
            button2.place(x = 390, y = 130, anchor = 'nw')

# 2隊logo
            team1 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + awayteam[0] + '.png')
            team11 = team1.resize((57, 57), Image.ANTIALIAS)
            self.TEAM1 = ImageTk.PhotoImage(team11)
            self.TEAM1logo = tk.Label(self, image = self.TEAM1, bd = 0)
            self.TEAM1logo.place(x = 210, y = 140, anchor = "nw")

            team2 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + hometeam[0] + '.png')
            team22 = team2.resize((55, 55), Image.ANTIALIAS)
            self.TEAM2 = ImageTk.PhotoImage(team22)
            self.TEAM2logo = tk.Label(self, image = self.TEAM2, bd = 0)
            self.TEAM2logo.place(x = 280, y = 140, anchor = "nw")

#2隊time
            time1 = tk.Label(self, text = date[0], font = ('Papyrus', 20))
            time1.place(x = 10, y = 130, anchor = 'nw')

#結果=2場
        if i >= 2:
            button3 = tk.Button(self, text = "Predictions", font = ('Papyrus', 20),
                                  command = lambda: self.click(awayteam[1], hometeam[1], date[1]))
            button3.place(x = 390, y = 230, anchor = 'nw')

#2隊logo
            team3 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + awayteam[1] + '.png')
            team33 = team3.resize((57, 57), Image.ANTIALIAS)
            self.TEAM3 = ImageTk.PhotoImage(team33)
            self.TEAM3logo = tk.Label(self, image = self.TEAM3, bd = 0)
            self.TEAM3logo.place(x = 210, y = 240, anchor = "nw")

            team4 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + hometeam[1] + '.png')
            team44 = team4.resize((55, 55), Image.ANTIALIAS)
            self.TEAM4 = ImageTk.PhotoImage(team44)
            self.TEAM4logo = tk.Label(self, image = self.TEAM4, bd = 0)
            self.TEAM4logo.place(x = 280, y = 240, anchor = "nw")

# 2隊time
            time1 = tk.Label(self, text = date[1], font = ('Papyrus', 20))
            time1.place(x = 10, y = 230, anchor = 'nw')

#結果=3場
        if i >= 3:
            button4 = tk.Button(self, text = "Predictions", font = ('Papyrus', 20),
                                  command = lambda: self.click(awayteam[2], hometeam[2], date[2]))
            button4.place(x = 390, y = 330, anchor = 'nw')

# 2隊logo
            team5 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + awayteam[2] + '.png')
            team55 = team5.resize((57, 57), Image.ANTIALIAS)
            self.TEAM5 = ImageTk.PhotoImage(team55)
            self.TEAM5logo = tk.Label(self, image = self.TEAM5, bd = 0)
            self.TEAM5logo.place(x = 210, y = 340, anchor = "nw")

            team6 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + hometeam[2] + '.png')
            team66 = team6.resize((55, 55), Image.ANTIALIAS)
            self.TEAM6 = ImageTk.PhotoImage(team66)
            self.TEAM6logo = tk.Label(self, image = self.TEAM6, bd = 0)
            self.TEAM6logo.place(x = 280, y = 340, anchor = "nw")

# 2隊time
            time1 = tk.Label(self, text = date[2], font = ('Papyrus', 20))
            time1.place(x = 10, y = 330, anchor = 'nw')

#結果=4場
        if i >= 4:
            button5 = tk.Button(self, text = "Predictions", font = ('Papyrus', 20),
                                  command = lambda: self.click(awayteam[3], hometeam[3], date[3]))
            button5.place(x = 390, y = 430, anchor = 'nw')

# 2隊logo
            team7 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + awayteam[3] + '.png')
            team77 = team7.resize((57, 57), Image.ANTIALIAS)
            self.TEAM7 = ImageTk.PhotoImage(team77)
            self.TEAM7logo = tk.Label(self, image = self.TEAM7, bd = 0)
            self.TEAM7logo.place(x = 210, y = 440, anchor = "nw")

            team8 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + hometeam[3] + '.png')
            team88 = team8.resize((55, 55), Image.ANTIALIAS)
            self.TEAM8 = ImageTk.PhotoImage(team88)
            self.TEAM8logo = tk.Label(self, image = self.TEAM8, bd = 0)
            self.TEAM8logo.place(x = 280, y = 440, anchor = "nw")

# 2隊time
            time1 = tk.Label(self, text = date[3], font = ('Papyrus', 20))
            time1.place(x = 10, y = 430, anchor = 'nw')

#結果=5場
        if i >= 5:
            button6 = tk.Button(self, text = "Predictions", font = ('Papyrus', 20),
                                  command = lambda: self.click(awayteam[4], hometeam[4], date[4]))
            button6.place(x = 390, y = 530, anchor = 'nw')

#2隊logo
            team9 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + awayteam[4] + '.png')
            team99 = team9.resize((57, 57), Image.ANTIALIAS)
            self.TEAM9 = ImageTk.PhotoImage(team99)
            self.TEAM9logo = tk.Label(self, image = self.TEAM9, bd = 0)
            self.TEAM9logo.place(x = 210, y = 540, anchor = "nw")

            team10 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + hometeam[4] + '.png')
            team101 = team10.resize((55, 55), Image.ANTIALIAS)
            self.TEAM10 = ImageTk.PhotoImage(team101)
            self.TEAM10logo = tk.Label(self, image = self.TEAM10, bd = 0)
            self.TEAM10logo.place(x = 280, y = 540, anchor = "nw")

#2隊time
            time1 = tk.Label(self, text = date[4], font = ('Papyrus', 20))
            time1.place(x = 10, y = 530, anchor = 'nw')
            
    def omg(self):
        self.controller.show_frame(StartPage)

    def click(self, tm1, tm2, tm3):
        a = tm1
        b = tm2
        c = tm3        
        frame = self.controller.show_frame(Predictions)
        frame.onPredictionsPage(self.controller, a, b, c)

#team的結果頁
class Results2 (tk.Frame):

    def __init__(self , parent , controller):
        tk.Frame.__init__ (self, parent)
        self.controller = controller
        # self.onChangePage(controller)
        
    def onChangePage(self, controller, _TEAM):
        fh= open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\file\\每日賽程.csv', 'r', newline = '', encoding = 'utf-8')
        reader = csv.DictReader(fh)
        date1 = ['2018/11/17'] * 5
        awayteam1 = ['TOR'] * 5
        hometeam1 = ['BOS'] * 5
        Team = {'Toronto Raptors': 'TOR', 'Boston Celtics': 'BOS', 'Philadelphia 76ers': 'PHI',
                'Cleveland Cavaliers': 'CLE', 'Indiana Pacers': 'IND', 'Miami Heat': 'MIA',
                'Milwaukee Bucks': 'MIL', 'Washington Wizards': 'WAS', 'Detroit Pistons': 'DET',
                'Charlotte Hornets': 'CHA', 'New York Knicks': 'NYK', 'Brooklyn Nets': 'BKN',
                'Chicago Bulls': 'CHI', 'Orlando Magic': 'ORL', 'Atlanta Hawks': 'ATL', 'Houston Rockets': 'HOU',
                'Golden State Warriors': 'GSW', 'Portland Trail Blazers': 'POR', 'Oklahoma City Thunder': 'OKC',
                'Utah Jazz': 'UTA', 'New Orleans Pelicans': 'NOR', 'San Antonio Spurs': 'SAS',
                'Minnesota Timberwolves': 'MIN', 'Denver Nuggets': 'DEN', 'Los Angeles Clippers': 'LAC',
                'Los Angeles Lakers': 'LAL', 'Sacramento Kings': 'SAC', 'Dallas Mavericks': 'DAL',
                'Memphis Grizzlies': 'MEM', 'Phoenix Suns': 'PHX'}
        Team1 = {'TOR': 'Toronto Raptors', 'BOS': 'Boston Celtics', 'PHI': 'Philadelphia 76ers',
                'CLE': 'Cleveland Cavaliers', 'IND': 'Indiana Pacers', 'MIA': 'Miami Heat',
                'MIL': 'Milwaukee Bucks', 'WAS': 'Washington Wizards', 'DET': 'Detroit Pistons',
                'CHA': 'Charlotte Hornets', 'NYK': 'New York Knicks', 'BKN': 'Brooklyn Nets',
                'CHI': 'Chicago Bulls', 'ORL': 'Orlando Magic', 'ATL': 'Atlanta Hawks', 'HOU': 'Houston Rockets',
                'GSW': 'Golden State Warriors', 'POR': 'Portland Trail Blazers', 'OKC': 'Oklahoma City Thunder',
                'UTA': 'Utah Jazz', 'NOR': 'New Orleans Pelicans', 'SAS': 'San Antonio Spurs',
                'MIN': 'Minnesota Timberwolves','DEN': 'Denver Nuggets',  'LAC': 'Los Angeles Clippers', 'LAL': 'Los Angeles Lakers',
                 'SAC': 'Sacramento Kings', 'DAL': 'Dallas Mavericks', 'MEM': 'Memphis Grizzlies', 'PHX': 'Phoenix Suns'}
        i = 0
                
        TEAM1 = Team1[_TEAM]        
        for row in reader:
            if i == 5:
                break
            if row['Visitor/Neutral'] == TEAM1 or row['Home/Neutral'] == TEAM1:
                date1[i] = row['Date']
                awayteam1[i] = Team[row['Visitor/Neutral']]
                hometeam1[i] =  Team[row['Home/Neutral']]
                i += 1
        fh.close ()

# button-return to homepage
        button1 = tk.Button(self, text = "Return to Home Page", font = ('Papyrus', 20),
                              command = lambda: controller.show_frame(StartPage))
        button1.place(x = 700, y = 0, anchor = 'nw')

#label-time
        time = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\time.jpg')
        time1 = time.resize((150, 60), Image.ANTIALIAS)
        self.TIME = ImageTk.PhotoImage(time1)
        self.TIMElogo = tk.Button(self, image = self.TIME, bd = 0)
        self.TIMElogo.place(x = 10, y = 40, anchor = "nw")

#label-event
        event = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\events.jpg')
        event1 = event.resize((150, 60), Image.ANTIALIAS)
        self.EVENT = ImageTk.PhotoImage(event1)
        self.EVENTlogo = tk.Button(self, image = self.EVENT, bd = 0)
        self.EVENTlogo.place(x = 200, y = 40, anchor = "nw")

#label-predictions
        predictions = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\predictions.jpg')
        predictions1 = predictions.resize((150, 60), Image.ANTIALIAS)
        self.PREDICTIONS = ImageTk.PhotoImage(predictions1)
        self.PREDICTIONSlogo = tk.Button(self, image = self.PREDICTIONS, bd = 0)
        self.PREDICTIONSlogo.place(x = 400, y = 40, anchor = "nw")

#button*5-predictions
        button2 = tk.Button(self, text = "Predictions", font = ('Papyrus', 20),
                              command = lambda: self.click(awayteam1[0], hometeam1[0], date1[0]))
        button2.place(x = 390, y = 130, anchor = 'nw')

        button3 = tk.Button(self, text = "Predictions", font = ('Papyrus', 20),
                              command = lambda: self.click(awayteam1[1], hometeam1[1], date1[1]))
        button3.place(x = 390, y = 230, anchor = 'nw')

        button4 = tk.Button(self, text = "Predictions", font = ('Papyrus', 20),
                              command = lambda: self.click(awayteam1[2], hometeam1[2], date1[2]))
        button4.place(x = 390, y = 330, anchor = 'nw')

        button5 = tk.Button(self, text = "Predictions", font = ('Papyrus', 20),
                              command = lambda: self.click(awayteam1[3], hometeam1[3], date1[3]))
        button5.place(x = 390, y = 430, anchor = 'nw')

        button6 = tk.Button ( self , text="Predictions" , font=('Papyrus' , 20) ,
                              command=lambda: self.click(awayteam1[4], hometeam1[4], date1[4]))
        button6.place ( x=390 , y=530 , anchor='nw' )


#logo
        team1 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + awayteam1[0] + '.png')
        team11 = team1.resize((57, 57), Image.ANTIALIAS)
        self.TEAM1 = ImageTk.PhotoImage(team11)
        self.TEAM1logo = tk.Label(self, image = self.TEAM1, bd = 0)
        self.TEAM1logo.place(x = 210, y = 140, anchor = "nw")

        team2 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + hometeam1[0] + '.png')
        team22 = team2.resize((55, 55), Image.ANTIALIAS)
        self.TEAM2 = ImageTk.PhotoImage(team22)
        self.TEAM2logo = tk.Label(self, image = self.TEAM2, bd = 0)
        self.TEAM2logo.place(x = 280, y = 140, anchor = "nw")

        team3 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + awayteam1[1] + '.png')
        team33 = team3.resize((55, 55), Image.ANTIALIAS)
        self.TEAM3 = ImageTk.PhotoImage(team33)
        self.TEAM3logo = tk.Label(self, image = self.TEAM3, bd = 0)
        self.TEAM3logo.place(x = 210, y = 240, anchor = "nw")

        team4 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + hometeam1[1] + '.png')
        team44 = team4.resize((55, 55), Image.ANTIALIAS)
        self.TEAM4 = ImageTk.PhotoImage(team44)
        self.TEAM4logo = tk.Label(self, image = self.TEAM4, bd = 0)
        self.TEAM4logo.place(x = 280, y = 240, anchor = "nw")

        team5 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + awayteam1[2] + '.png')
        team55 = team5.resize((55, 55), Image.ANTIALIAS)
        self.TEAM5 = ImageTk.PhotoImage(team55)
        self.TEAM5logo = tk.Label(self, image = self.TEAM5, bd = 0)
        self.TEAM5logo.place(x = 210, y = 340, anchor = "nw")

        team6 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + hometeam1[2] + '.png')
        team66 = team6.resize((55, 55), Image.ANTIALIAS)
        self.TEAM6 = ImageTk.PhotoImage(team66)
        self.TEAM6logo = tk.Label(self, image = self.TEAM6, bd = 0)
        self.TEAM6logo.place(x = 280, y = 340, anchor = "nw")

        team7 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + awayteam1[3] + '.png')
        team77 = team7.resize((55, 55), Image.ANTIALIAS)
        self.TEAM7 = ImageTk.PhotoImage(team77)
        self.TEAM7logo = tk.Label(self, image = self.TEAM7, bd = 0)
        self.TEAM7logo.place(x = 210, y = 440, anchor = "nw")

        team8 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + hometeam1[3] + '.png')
        team88 = team8.resize((55 , 55), Image.ANTIALIAS)
        self.TEAM8 = ImageTk.PhotoImage(team88)
        self.TEAM8logo = tk.Label(self, image = self.TEAM8, bd = 0)
        self.TEAM8logo.place(x = 280, y = 440, anchor = "nw")

        team9 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + awayteam1[4] + '.png')
        team99 = team9.resize((55, 55), Image.ANTIALIAS)
        self.TEAM9 = ImageTk.PhotoImage(team99)
        self.TEAM9logo = tk.Label(self, image = self.TEAM9, bd = 0)
        self.TEAM9logo.place(x = 210, y = 540, anchor = "nw")

        team10 = Image.open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + hometeam1[4] + '.png')
        team101 = team10.resize((55, 55), Image.ANTIALIAS)
        self.TEAM10 = ImageTk.PhotoImage(team101)
        self.TEAM10logo = tk.Label(self, image = self.TEAM10, bd = 0)
        self.TEAM10logo.place(x = 280, y = 540, anchor = "nw")

#time
        time1 = tk.Label(self, text = date1[0], font = ('Papyrus', 20))
        time1.place(x = 10, y = 130, anchor = 'nw')
        
        time1 = tk.Label(self, text = date1[1], font = ('Papyrus', 20))
        time1.place(x = 10, y = 230, anchor = 'nw')
        
        time1 = tk.Label(self, text = date1[2], font = ('Papyrus', 20))
        time1.place(x = 10, y = 330, anchor = 'nw')
        
        time1 = tk.Label(self, text = date1[3], font = ('Papyrus', 20))
        time1.place(x = 10, y = 430, anchor = 'nw')
        
        time1 = tk.Label(self, text = date1[4], font = ('Papyrus', 20))
        time1.place(x = 10, y = 530, anchor = 'nw')

    def click(self, tm1, tm2, tm3):
        a = tm1
        b = tm2
        c = tm3
        frame = self.controller.show_frame(Predictions)
        frame.onPredictionsPage(self.controller, a, b, c)


class Predictions(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def onPredictionsPage(self, controller, _a, _b, _c):
        fh = open('C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\file\\betdata.csv', 'r', newline = '', encoding = 'utf-8')
        reader = csv.reader(fh)
        point1 = 0
        point2 = 0
        for row in reader:
            if row[0] == _c and row[1] == _a:
                point1 = float(row[4])
                continue
            if row[0] == _c and row[1] == _b:
                point2 = float(row[4])
                break
        fh.close ()

        size1 = size2 = locx1 = locx2 = locy1 = locy2 = 0
        if point1 < point2:
            size1 = 200
            size2 = 400
            locx1 = 190
            locy1 = 190
            locx2 = 500
            locy2 = 100
        elif point1 > point2:
            size1 = 400
            size2 = 200
            locx1 = 100
            locy1 = 100
            locx2 = 600
            locy2 = 190

        tt1 = _a
        picURL = 'C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + tt1 + '.png'
        t1 = Image.open(picURL)
        t1 = t1.resize((size1, size1), Image.ANTIALIAS)
        self.T1 = ImageTk.PhotoImage(t1)
        self.T1logo = tk.Label(self, image = self.T1, bd = 0)
        self.T1logo.place(x = locx1, y = locy1, anchor = "nw")

        tt2 = _b
        picURL = 'C:\\Users\\Maxwell\\Documents\\Python file\\NBA\\' + tt2 + '.png'
        t2 = Image.open(picURL)
        t2 = t2.resize((size2, size2), Image.ANTIALIAS)
        self.T2 = ImageTk.PhotoImage(t2)
        self.T2logo = tk.Label(self, image = self.T2, bd = 0)
        self.T2logo.place(x = locx2, y = locy2, anchor = "nw")

#顯示tt1、tt2的機率
        label1 = tk.Label(self, text = point1, font = ('Papyrus', 40))
        label1.place(x = 130, y = 500)

        label2 = tk.Label(self, text = point2, font = ('Papyrus', 40))
        label2.place(x = 530, y = 500)

# button-return to homepage
        button1 = tk.Button(self, text = "Return to Home Page", font = ('Papyrus', 20),
                              command = lambda: controller.show_frame(StartPage))
        button1.place(x = 700, y = 0, anchor = 'nw')

app = NBABOOM()
app.mainloop()