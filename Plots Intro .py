#Name:Chelsie Banton
#
#Project Name: Plots
#
#Date: Oct 6,2024
#
#
#
#
#
#

import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

class Plots:
    def __init__(self,plots):
        self.x = 0
        self.y = 0

    def plot1 (self):
        plt.plot([1, 2, 3, 4])
        plt.ylabel('some numbers')
        plt.show()
    
    def plot2 (self):
        plt.plot([1, 2, 3, 4], [1, 4, 9, 16], '-ro')
        #x axis will range from 0-6 & ) to 20
        plt.axis([0, 6, 0, 20])
        #x axis range from 0-6 and y from 0-20
        plt.xlabel('numbers-1')
        plt.ylabel('numbers-2')
        plt.show()

    def plot3 (self):
        #make an array of x values
        x =[1, 2, 3, 4, 5]
        y =[1, 4, 9, 16, 25]
        plt.plot(x,y)
        #give the plot a title
        plt.title('Plot of y vs. x')
        #label the axis
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        #set limits for the axis
        plt.xlim(0.0, 7.0)
        plt.ylim(0.0, 30.0)
        #show the plot on graph/screen
        plt.show

    def plot4 (self):
        # Make x, y arrays for each graph
        x1 = [1, 2, 3, 4, 5]
        y1 = [1, 4, 9, 16, 25]
        x2 = [1, 2, 4, 6, 8]
        y2 = [2, 4, 8, 12, 16]
        # use pylab to plot x and y
        plt.plot(x1, y1, 'b*')# blue star
        plt.plot(x2, y2, 'go')# green circle
        # give plot a title
        plt.title('Plot of y vs. x')
        # make axis labels
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        # set axis limits
        plt.xlim(0.0, 9.0)
        plt.ylim(0.0, 30.)
        # show the plot on the screen
        plt.show()

    def plot5 (self):
        #make an array of random numbers with a gaussian distribution with
        # mean = 8.0
        # rms = 4.0
        # number of points = 500
        data = np.random.normal(8.0, 4.0, 500)
        # make a histogram of the data array
        plt.hist(data)
        # make plot labels
        plt.xlabel('data')
        plt.show()

    def plot6 (self):
        x = [1, 2, 3, 4, 5]
        y = [1, 4, 9, 16, 25]
        fig1 = plt.figure(1)
        plt.subplot(211)
        plt.plot(x,y)
        # subplot(211) means that you will have a figure with 2 rows, 1 column, and you’re going to draw in the top plot
        plt.subplot(212)
        plt.show()

    def plot7 (self):
        def update_title(axes):
            axes.set_title(datetime.now())

        fig, ax = plt.subplots()
        timer = fig.canvas.new_timer(interval=100)
        timer.add_callback(update_title, ax)
        timer.start()

        def OnClick(event):
            print("Click", event)

        def OnRelease(event):
            print("Release", event)

        cid_click = fig.canvas.mpl_connect('button_press_event', OnClick)
        cid_release = fig.canvas.mpl_connect('button_release_event', OnRelease)
        plt.gca().text(0.5, 0.5, "Click on the canvas to test mouse events.",
                       ha="center", va="center")
        plt.show()

    def plot8 (self):
        figsrc = plt.figure()
        figzoom = plt.figure()
        axsrc = figsrc.add_subplot(111, xlim=(0, 1), ylim=(0, 1), autoscale_on=False)
        axzoom = figzoom.add_subplot(111, xlim=(0.45, 0.55), ylim=(0.4, 0.6), autoscale_on=False)
        axsrc.set_title('Click to zoom')
        axzoom.set_title('Zoom Window')

        x, y, s, c = np.random.rand(4, 200)
        s *= 200
        axsrc.scatter(x, y, s, c)
        axzoom.scatter(x, y, s, c)

        def onpress(event):
            if event.button != 1:  # Left mouse button
                return

            x, y = event.xdata, event.ydata
            axzoom.set_xlim(x - 0.1, x + 0.1)
            axzoom.set_ylim(y - 0.1, y + 0.1)
            figzoom.canvas.draw()

        figsrc.canvas.mpl_connect('button_press_event', onpress)
        plt.show()

    def plot9 (self):
    #had assistance from Jason and he used this code to get the program to run on mac.
        image_path = os.path.expanduser("~/Downloads/USA.png")
        im = plt.imread(image_path)
        plt.imshow(im)
        plt.show()


my_plots = Plots(plt)

my_plots.plot1()
my_plots.plot2()
my_plots.plot3()
my_plots.plot4()
my_plots.plot5()
my_plots.plot6()
my_plots.plot7()
my_plots.plot8()
my_plots.plot9()

