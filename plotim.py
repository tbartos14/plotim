# # P L O T I M # #

#version 0.5, 1/9/2017


import tkinter as tk

def vertical_text(text):
    newtext = ""
    for character in text:
        newtext += character + "\n"
    return newtext

class linear_plot(object):
    def __init__(self, windowx = 600, windowy = 400, bordernorth = 50, bordersouth = 50, bordereast = 30, borderwest = 50, title = "Linear Plot",\
                 sortpoints = True, draw_lines = True, draw_points = False, ytitle = "y", xtitle = "x", line_color = "#0000bb", image = None,\
                 line_of_best_fit = False):
        self.windowx = windowx
        self.windowy = windowy
        self.bordernorth = bordernorth
        self.bordersouth = bordersouth
        self.bordereast = bordereast
        self.borderwest = borderwest
        self.xpoints = []
        self.ypoints = []
        self.sortpoints = sortpoints
        self.originalyaxistitle = ytitle
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
        self.image = image
        self.line_of_best_fit = line_of_best_fit
    def set_data(self, x, y):
        if self.sortpoints == True:
            temppointsx = []
            temppointsy = []
            for count in range(0, len(x)):
                temppointsx.append(x[count])
                temppointsy.append(y[count])
            while len(temppointsx) > 0:
                xvalue = min(temppointsx)
                yindex = temppointsx.index(xvalue)
                yvalue = temppointsy[yindex]
                temppointsx.pop(yindex)
                temppointsy.pop(yindex)
                self.xpoints.append(xvalue)
                self.ypoints.append(yvalue)
        elif self.sortpoints == False:
            for value in x:
                self.xpoints.append(value)
            for value in y:
                self.ypoints.append(value)
        print(self.xpoints,self.ypoints)
    def plot_data(self):
        self.master = tk.Tk()
        self.canvas = tk.Canvas(self.master, width = self.windowx, height = self.windowy)
        self.canvas.create_text(self.borderwest + self.graphx/2,self.bordernorth/2, text = self.title)
        self.canvas.create_text(self.borderwest/3, self.bordernorth + self.graphy/2, text = self.yaxistitle)
        self.canvas.create_text(self.borderwest + self.graphx/2, self.windowy - self.bordersouth/3, text = self.xaxistitle)
        self.master.title(self.title)
        self.canvas.create_rectangle(self.bordernorth, self.borderwest, (self.windowx - self.bordereast), (self.windowy - self.bordersouth), fill="white", outline="white")
        
        # finding limits for axis
        self.yaxis.append(min(self.ypoints))
        self.yaxis.append(max(self.ypoints))
        self.xaxis.append(min(self.xpoints))
        self.xaxis.append(max(self.xpoints))
        self.yrange = abs(self.yaxis[1] - self.yaxis[0])
        self.xrange = abs(self.xaxis[1] - self.xaxis[0])
        self.yrangefactor = 0
        self.xrangefactor = 0
        # choosing what kind of scale to use
        # y range factorization
        while self.yrange*(10**self.yrangefactor) > 10 or self.yrange*(10**self.yrangefactor) < 1:
            if self.yrange*(10**self.yrangefactor) < 1:
                self.yrangefactor = self.yrangefactor + 1
            elif self.yrange*(10**self.yrangefactor) > 10:
                self.yrangefactor = self.yrangefactor - 1
                
        # x range factorization
        while self.xrange*(10**self.xrangefactor) > 10 or self.xrange*(10**self.xrangefactor) < 1:
            if self.xrange*(10**self.xrangefactor) < 1:
                self.xrangefactor = self.xrangefactor + 1
            elif self.xrange*(10**self.xrangefactor) > 10:
                self.xrangefactor = self.xrangefactor - 1
                
        # determining how many lines need to be placed
        # minimums/maximums for ease of reading
        self.yrangemin = ((int((min(self.ypoints))*(10**(self.yrangefactor))))/(10**(self.yrangefactor)))
        self.xrangemin = ((int((min(self.xpoints))*(10**(self.xrangefactor))))/(10**(self.xrangefactor)))
        self.yrangemax = ((int((min(self.ypoints))*(10**(self.yrangefactor))))/(10**(self.yrangefactor))+((int(self.yrange*(10**self.yrangefactor)) + 1)*(10**(-1*self.yrangefactor))))
        self.xrangemax = ((int((min(self.xpoints))*(10**(self.xrangefactor))))/(10**(self.xrangefactor))+((int(self.xrange*(10**self.xrangefactor)) + 1)*(10**(-1*self.xrangefactor))))

        #determining increments
        #finding if scales are appropriate
        self.additionalscaley = 0
        self.additionalscalex = 0
        
        # seeing if data needs more space (y)
        while True:
            if max(self.ypoints) > self.yrangemax:
                self.additionalscaley = self.additionalscaley + 1
                self.yrangemax = ((int((min(self.ypoints))*(10**(self.yrangefactor))))/(10**(self.yrangefactor))+((int(self.yrange*(10**self.yrangefactor)) + 1 + self.additionalscaley)*(10**(-1*self.yrangefactor))))
            else:
                break
            
        # (x)
        while True:
            if max(self.xpoints) > self.xrangemax:
                self.additionalscalex = self.additionalscalex + 1
                self.xrangemax = ((int((min(self.xpoints))*(10**(self.xrangefactor))))/(10**(self.xrangefactor))+((int(self.xrange*(10**self.xrangefactor)) + 1 + self.additionalscalex)*(10**(-1*self.xrangefactor))))
            else:
                break
        self.yincrement = int(self.yrange*(10**self.yrangefactor)) + self.additionalscaley + 1
        self.xincrement = int(self.xrange*(10**self.xrangefactor)) + self.additionalscalex + 1
        
        # now we determine y
        for increment in range(0, self.yincrement + 1):
            self.canvas.create_line(self.borderwest + 1, (self.windowy - self.bordersouth)-(increment/self.yincrement)*(self.windowy-self.bordernorth - self.bordersouth),\
                                    self.borderwest + self.graphx, (self.windowy - self.bordersouth)-(increment/self.yincrement)*(self.windowy - self.bordernorth - self.bordersouth), fill = "#bbbbbb", dash = (2,2))
            self.canvas.create_text(self.borderwest - 12, (self.windowy - self.bordersouth)-(increment/self.yincrement)*(self.windowy - self.bordernorth - self.bordersouth),\
                                    text = "{0:4.4}".format((int((min(self.ypoints))*(10**(self.yrangefactor))))/(10**(self.yrangefactor))+((increment)*(10**(-1*self.yrangefactor)))))
            
        # determining x
        for increment in range(0, self.xincrement + 1):
            self.canvas.create_line(self.bordersouth + (increment/self.xincrement)*(self.windowx - self.bordereast - self.borderwest), (self.windowy - self.bordersouth) - 1,\
                                    self.bordersouth + (increment/self.xincrement)*(self.windowx - self.bordereast - self.borderwest), (self.windowy - self.bordersouth - self.graphy), fill = "#bbbbbb", dash = (2,2))
            self.canvas.create_text(self.borderwest  + (increment/self.xincrement)*(self.windowx - self.bordereast - self.borderwest), (self.windowy - self.bordersouth) + 12,\
                                    text = ((int((min(self.xpoints))*(10**(self.xrangefactor))))/(10**(self.xrangefactor))+((increment)*(10**(-1*self.xrangefactor)))))
            
        # line of best fit
        n = len(self.xpoints)
        sumx = sum(self.xpoints)
        sumy = sum(self.ypoints[:len(self.xpoints)])
        sumxytemp = []
        for point in range(0,len(self.xpoints)):
            sumxytemp.append(self.xpoints[point]*self.ypoints[point])
        sumxy = sum(sumxytemp)
        sumxsquaredtemp = []
        for point in range(0,len(self.xpoints)):
            sumxsquaredtemp.append((self.xpoints[point])**2)
        sumxsquared = sum(sumxsquaredtemp)
        self.bestfitslope = (n*sumxy-(sumx*sumy))/(n*(sumxsquared) - (sumx**2))
        self.bestfitintercept = ((sumxsquared)*(sumy)-(sumx)*(sumxy))/(n*(sumxsquared) - (sumx**2))
        if self.line_of_best_fit == True:
            bestfitstart = [min(self.xpoints), self.bestfitslope*min(self.xpoints) + self.bestfitintercept]
            bestfitend =  [max(self.xpoints), self.bestfitslope*max(self.xpoints) + self.bestfitintercept]
            self.canvas.create_line((bestfitstart[0] - self.xrangemin)*(self.windowx - self.bordereast - self.borderwest)/(self.xrangemax - self.xrangemin) + self.borderwest,\
                                    (self.windowy - self.bordersouth) - (bestfitstart[1] - self.yrangemin)*(self.windowy - self.bordernorth - self.bordersouth)/(self.yrangemax - self.yrangemin),\
                                    (bestfitend[0] - self.xrangemin)*(self.windowx - self.bordereast - self.borderwest)/(self.xrangemax - self.xrangemin) + self.borderwest,\
                                    (self.windowy - self.bordersouth) - (bestfitend[1] - self.yrangemin)*(self.windowy - self.bordernorth - self.bordersouth)/(self.yrangemax - self.yrangemin), fill = "#000000")
            
        #line of best fit equation
        self.bestfitslope = "{0:4.4}".format(self.bestfitslope)
        self.bestfitintercept = "{0:4.4}".format(self.bestfitintercept)
        self.bestfitequation = "Line of Best Fit Equation:\n" + str(self.originalyaxistitle) + " = " + str(self.bestfitslope) + " * " + str(self.xaxistitle) + " + " + str(self.bestfitintercept)
        if self.line_of_best_fit == True:
            if self.ypoints[len(self.xpoints)-1] < (self.yrangemax - self.yrangemin):
                self.canvas.create_text((self.windowx - self.bordereast - self.graphx/5), (self.bordernorth + self.graphy/5), text = self.bestfitequation)
            else:
                self.canvas.create_text((self.windowx - self.bordereast - self.graphx/5), (self.bordernorth + 4*self.graphy/5), text = self.bestfitequation)
            
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
                
        #use an image?
        pointimages = []
        for point in range(0,len(self.xpoints)):
            if self.image != None:
                pointimages.append(tk.PhotoImage(file = self.image))
                self.canvas.create_image((self.xpoints[point] - self.xrangemin)*(self.windowx - self.bordereast - self.borderwest)/(self.xrangemax - self.xrangemin) + self.borderwest,\
                        (self.windowy - self.bordersouth) - (self.ypoints[point] - self.yrangemin)*(self.windowy - self.bordernorth - self.bordersouth)/(self.yrangemax - self.yrangemin), image = pointimages[point])

        #finalize
        self.canvas.create_line(self.bordernorth, self.borderwest, self.bordernorth, (self.windowy - self.bordersouth))
        self.canvas.create_line(self.borderwest,(self.windowy - self.bordersouth),(self.windowx - self.bordereast), (self.windowy - self.bordersouth))
        self.canvas.pack()
        tk.mainloop()
