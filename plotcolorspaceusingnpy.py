import numpy as np
import os
import matplotlib.pyplot as plt

saveplot = r"./Plot_ColorspaceusingNPYFile"
npypath = r"./ColorSpace"

def loadNpyFiles(npypath):
    npyFile = [os.path.join(npypath, f) for f in os.listdir(npypath)]


    for npyFilePath in npyFile:
        
        name = os.path.basename(npyFilePath)
        main(npyFilePath,name)
        
        


def main(npyFilePath,name):
    data = np.load(npyFilePath)

    ax = plt.axes(projection = '3d')

    x=[]
    y=[]
    z=[]
    c=[]


    for i in range( len(data)):
        r,g,b= data[i]
        x.append(r)
        y.append(g)
        z.append(b)
        newCol = (r / 255, g / 255, b / 255)
        c.append(newCol)


    ax.scatter(x,y,z, c = c)
    ax.set_title('Color Spaces' )
    plt.savefig(saveplot + "\\" + str(name) + ".png")
    print("plotted graph for:"+name)   

loadNpyFiles(npypath)

