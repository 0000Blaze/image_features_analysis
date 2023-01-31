import matplotlib.pyplot as plt
# from mpl_toolkits import mplot3d
from PIL import Image
import os

saveplotimage=r"./Plot_colorspace"

def plotgraph(px,pilImage, imageName):
    
    ax = plt.axes(projection = '3d')
    x = []
    y = []
    z = []
    c = []

    for row in range(0,pilImage.height):
        for col in range(0, pilImage.width):
            pix =px[col,row]
            newCol = (pix[0] / 255, pix[1] / 255, pix[2] / 255)

            if(not newCol in c):
                x.append(pix[0])
                y.append(pix[1])
                z.append(pix[2])
                c.append(newCol)

    ax.scatter(x,y,z, c = c)
    ax.set_title('Color Spaces' )

    plt.savefig(saveplotimage + "\\" + str(imageName) + ".png")
    print("plotted graph for:"+imageName)


def main():
    imagePath = r"./images"
    if os.path.exists(imagePath):
        imagePaths = [os.path.join(imagePath, f) for f in os.listdir(imagePath)]
        # create empth list
        # now looping through all the image paths 
        for imagePath in imagePaths:
            # loading the image
            pilImage = Image.open(imagePath)
            name = os.path.basename(imagePath)
            fileName=os.path.splitext(name)[0]
            array_2d = pilImage.load()

            plotgraph(array_2d,pilImage, fileName)
    else:
        print("Image file doesnt exist")

main()