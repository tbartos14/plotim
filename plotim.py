import tkinter as tk

def vertical_text(text):
    newtext = ""
    for character in text:
        newtext += character + "\n"
    return newtext

class linearplot(object):
    def __init__(self, windowx = 600, windowy = 400, bordernorth = 50, bordersouth = 50, bordereast = 30, borderwest = 50, title = "Linear Plot", draw_lines = True, draw_points = False, ytitle = "", xtitle = "", line_color = "#0000bb"):
        self.windowx = windowx
        self.windowy = windowy
        self.bordernorth = bordernorth
        self.bordersouth = bordersouth
        self.bordereast = bordereast
        self.borderwest = borderwest
        self.xpoints = []
        self.ypoints = []
        self.yaxistitle = vertical_text(ytitle)
        self.xaxistitle = xtitle
        self.yaxis = []
        self.xaxis = []
        self.title = title
        self.draw_lines = draw_lines
        self.draw_points = draw_points
        self.graphx = windowx - bordereast - borderwest
        self.graphy = windowy - bordernorth - bordersouth
        self.linecolor = line_color
    def set_data(self, x, y):
        for value in x:
            self.xpoints.append(value)
        for value in y:
            self.ypoints.append(value)
    def plot_data(self):
        self.master = tk.Tk()
        self.canvas = tk.Canvas(self.master, width = self.windowx, height = self.windowy)
        self.canvas.create_text(self.borderwest + self.graphx/2,self.bordernorth/2, text = self.title)
        self.canvas.create_text(self.borderwest/3, self.bordernorth + self.graphy/2, text = self.yaxistitle)
        self.canvas.create_text(self.borderwest + self.graphx/2, self.windowy - self.bordersouth/3, text = self.xaxistitle)
        self.master.title(self.title)
        self.canvas.create_rectangle(self.bordernorth, self.borderwest, (self.windowx - self.bordereast), (self.windowy - self.bordersouth), fill="white", outline="white")

        
        #finding limits for axis
        self.yaxis.append(min(self.ypoints))
        self.yaxis.append(max(self.ypoints))
        self.xaxis.append(min(self.xpoints))
        self.xaxis.append(max(self.xpoints))
        print(self.yaxis, self.xaxis)
        self.yrange = abs(self.yaxis[1] - self.yaxis[0])
        self.xrange = abs(self.xaxis[1] - self.xaxis[0])
        self.yrangefactor = 0
        self.xrangefactor = 0
        #choosing what kind of scale to use
        #y range factorization
        while self.yrange*(10**self.yrangefactor) > 10 or self.yrange*(10**self.yrangefactor) < 1:
            if self.yrange*(10**self.yrangefactor) < 1:
                self.yrangefactor = self.yrangefactor + 1
            elif self.yrange*(10**self.yrangefactor) > 10:
                self.yrangefactor = self.yrangefactor - 1
                
        #x range factorization
        while self.xrange*(10**self.xrangefactor) > 10 or self.xrange*(10**self.xrangefactor) < 1:
            if self.xrange*(10**self.xrangefactor) < 1:
                self.xrangefactor = self.xrangefactor + 1
            elif self.xrange*(10**self.xrangefactor) > 10:
                self.xrangefactor = self.xrangefactor - 1
                
        #determining how many lines need to be placed
        #minimums/maximums for ease of reading
        self.yrangemin = ((int((min(self.ypoints))*(10**(self.yrangefactor))))/(10**(self.yrangefactor)))
        self.xrangemin = ((int((min(self.xpoints))*(10**(self.xrangefactor))))/(10**(self.xrangefactor)))
        #determining increments
        self.tryyscale = (int((min(self.ypoints))*(10**(self.yrangefactor))))/(10**(self.yrangefactor))+((increment)*(10**(-1*self.yrangefactor)))
        self.tryxscale = (int((min(self.xpoints))*(10**(self.xrangefactor))))/(10**(self.xrangefactor))+((increment)*(10**(-1*self.xrangefactor)))
        #finding if scales are appropriate
        self.additionalscaley = 0
        self.addtiionalscalex = -0
        while True:
            if 
        while True:
            if
        self.yincrement = int(self.yrange*(10**self.yrangefactor)) + self.additionalscaley
        self.xincrement = int(self.xrange*(10**self.xrangefactor)) + self.additionalscalex
        #now we determine y
        for increment in range(0, self.yincrement + 1):
            self.canvas.create_line(self.borderwest + 1, (self.windowy - self.bordersouth)-(increment/self.yincrement)*(self.windowy-self.bordernorth - self.bordersouth),\
                                    self.borderwest + self.graphx, (self.windowy - self.bordersouth)-(increment/self.yincrement)*(self.windowy - self.bordernorth - self.bordersouth), fill = "#bbbbbb", dash = (2,2))
            self.canvas.create_text(self.borderwest - 12, (self.windowy - self.bordersouth)-(increment/self.yincrement)*(self.windowy - self.bordernorth - self.bordersouth),\
                                    text = "{0:4.4}".format((int((min(self.ypoints))*(10**(self.yrangefactor))))/(10**(self.yrangefactor))+((increment)*(10**(-1*self.yrangefactor)))))
        #determining x
        for increment in range(0, self.xincrement + 1):
            self.canvas.create_line(self.bordersouth + (increment/self.xincrement)*(self.windowx - self.bordereast - self.borderwest), (self.windowy - self.bordersouth) - 1,\
                                    self.bordersouth + (increment/self.xincrement)*(self.windowx - self.bordereast - self.borderwest), (self.windowy - self.bordersouth - self.graphy), fill = "#bbbbbb", dash = (2,2))
            self.canvas.create_text(self.borderwest  + (increment/self.xincrement)*(self.windowx - self.bordereast - self.borderwest), (self.windowy - self.bordersouth) + 12,\
                                    text = ((int((min(self.xpoints))*(10**(self.xrangefactor))))/(10**(self.xrangefactor))+((increment)*(10**(-1*self.xrangefactor)))))

        #adding lines
        self.oldypoint = self.yrangemin
        self.oldxpoint = self.xrangemin
        for point in range(0,len(self.xpoints)):
            if self.draw_lines == True:
                self.canvas.create_line((self.xpoints[point] - self.xrangemin)*(self.windowx - self.bordereast - self.borderwest)/(self.xrangemax - self.xrangemin) + self.borderwest,\
                                        (self.windowy - self.bordersouth) - (self.ypoints[point] - self.yrangemin)*(self.windowy - self.bordernorth - self.bordersouth)/(self.yrangemax - self.yrangemin),\
                                        (self.oldxpoint - self.xrangemin)*(self.windowx - self.bordereast - self.borderwest)/(self.xrangemax - self.xrangemin) + self.borderwest,\
                                        (self.windowy - self.bordersouth) - (self.oldypoint - self.yrangemin)*(self.windowy - self.bordernorth - self.bordersouth)/(self.yrangemax - self.yrangemin), fill = self.linecolor)
                self.oldypoint = self.ypoints[point]
                self.oldxpoint = self.xpoints[point]

        #adding points!
        for point in range(0,len(self.xpoints)):
            if self.draw_points == True:
                self.canvas.create_oval((self.xpoints[point] - self.xrangemin)*(self.windowx - self.bordereast - self.borderwest)/(self.xrangemax - self.xrangemin) + self.borderwest + 3,\
                                        (self.windowy - self.bordersouth) - (self.ypoints[point] - self.yrangemin)*(self.windowy - self.bordernorth - self.bordersouth)/(self.yrangemax - self.yrangemin) + 3,\
                                        (self.xpoints[point] - self.xrangemin)*(self.windowx - self.bordereast - self.borderwest)/(self.xrangemax - self.xrangemin) + self.borderwest - 3,\
                                        (self.windowy - self.bordersouth) - (self.ypoints[point] - self.yrangemin)*(self.windowy - self.bordernorth - self.bordersouth)/(self.yrangemax - self.yrangemin) - 3, fill = "white")
        #finalize
        self.canvas.create_line(self.bordernorth, self.borderwest, self.bordernorth, (self.windowy - self.bordersouth))
        self.canvas.create_line(self.borderwest,(self.windowy - self.bordersouth),(self.windowx - self.bordereast), (self.windowy - self.bordersouth))
        self.canvas.pack()
        tk.mainloop()
