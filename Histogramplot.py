import numpy as np
import os
import matplotlib.pyplot as plt

saveplot = r"./Plot_ColorsHistogram"
npypath = r"./ColorHistogram/"



def loadNpyFiles(npypath):
    npyFile = [os.path.join(npypath, f) for f in os.listdir(npypath)]


    for npyFilePath in npyFile:

        name = os.path.basename(npyFilePath)
        main(npyFilePath,name)


def main(npyFilePath,name):
    data = np.load(npyFilePath)
    x=[]
    y=[]
    z=[]
    for i in range( len(data)):
        r,g,b= data[i]
        x.append(r)
        y.append(g)
        z.append(b)
    plt.title("Color Histogram")
    plt.plot(x), plt.plot(y),plt.plot(z)
    plt.savefig(saveplot + "\\" + str(name) + ".png")
    
    print("plotted graph for:"+name)   

loadNpyFiles(npypath)


