import pandas as pd
import numpy as np
import cv2
import os


def getImagesPath():
    file_names = os.listdir(r"./images")
    file_names = pd.Series(file_names)
    images_relative_path = "./images/" + file_names
    return images_relative_path

def getColorSpace(image, img_path):
    # reshape image 
    flat_img = image.reshape(-1, image.shape[-1])
    # Obtain A color only once
    unique_colors = np.unique(flat_img, axis = 0)

    f_name = img_path.split('/')[-1][:-4]
    f_path = r"./ColorSpace/"+f_name+".npy"
    # Store
    np.save(f_path, unique_colors)
    return f_path

def getColorHist(image, img_path):
    red = cv2.calcHist([image], [0], None, [256], [0, 256]).reshape(256)
    green = cv2.calcHist([image], [1], None, [256], [0, 256]).reshape(256)
    blue = cv2.calcHist([image], [2], None, [256], [0, 256]).reshape(256)
    hist_arr = np.array([red, green, blue]).T
    f_name = img_path.split('/')[-1][:-4]
    f_path = r"./ColorHistogram/"+f_name+".npy"
    np.save(f_path, hist_arr)
    return f_path


if __name__ == "__main__":

    df = pd.DataFrame()
    
    paths = getImagesPath()
    df["relative_path"] = paths

    # Read all images and store as array of numpy arrays
    print("Reading All Images...\n")
    images = [cv2.imread(path) for path in paths]
    images = [cv2.cvtColor(image, cv2.COLOR_BGR2RGB) for image in images]
    images = np.array(images, dtype = object)



    # Get dimensions of all images
    print("Reading Dimensions of Images...\n")
    dimensions = np.array(list(map(lambda x: x.shape, images)))

    # Update Dataframe
    df[["Height", "Width", "Channel"]] = dimensions

    # Add orentaiton column

    df["Orientation"] = np.where(df["Height"] > df["Width"], "Potrait", "landscape")

    # Obtaining Color Space
    # All colors in image are stored in the form of n X 3 array of pixel colors
    print("Obtaining Image colour space...\n")
    if not os.path.exists(r"./ColorSpace"):
        os.mkdir(r"./ColorSpace")
    ColorSpace = np.vectorize(getColorSpace)
    space_fpaths = ColorSpace(images, df["relative_path"])
    df["colorSpace_fpath"] = space_fpaths

    # Obtaining data for image color histogram
    print("Obtaining Data for color Histogram...\n")
    if not os.path.exists(r"./ColorHistogram"):
        os.mkdir(r"./ColorHistogram")
    ColorHistogram = np.vectorize(getColorHist)
    hist_fpaths = ColorHistogram(images, df["relative_path"])
    df["colorHistogram_fpath"] = hist_fpaths

    df.to_csv("dataframe.csv", index=False)
    print(df.head())