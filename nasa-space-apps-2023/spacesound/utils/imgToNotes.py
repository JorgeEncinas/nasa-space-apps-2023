import numpy as np
import math
from PIL import Image

centroidsToColors = {
    (128,128,128):"gray",
    (192,192,192):"silver",
    (0,0,128):"navy",
    (0,0,0):"black",
    (0,0,255):"blue",
    (0,255,0):"lime",
    (255,255,255):"white",
    (128,0,128):"purple",
    (255,0,255):"fuchsia",
    (128,0,0):"maroon",
    (255,255,0):"yellow",
    (255,0,0):"red" 
}
#print(centroidsToColors)
numbersToNotes = {
    "white":50,#"B", #12
    "silver":51,#"A#",
    "gray":52,#"A",
    "black":53,#"G#",
    "maroon":54,#"G",
    "red":55,#"F#",
    "fuchsia":56,#"F",
    "purple":57,#"E",
    "navy":58,#"D#",
    "blue":59,#"D",
    "lime":60,#"C#",
    "yellow":61#"C" #1
}
centroids = {
    "gray": (128,128,128),
    "silver": (192,192,192),
    "navy":(0,0,128),
    "black":(0,0,0),
    "blue":(0,0,255),
    "lime":(0,255,0),
    "white":(255,255,255),
    "purple":(128,0,128),
    "fuchsia":(255,0,255),
    "maroon":(128,0,0),
    "yellow":(255,255,0),
    "red":(255,0,0)
}

centroids_arr = [
    (128,128,128),
    (192,192,192),
    (0,0,128),
    (0,0,0),
    (0,0,255),
    (0,255,0),
    (255,255,255),
    (128,0,128),
    (255,0,255),
    (128,0,0),
    (255,255,0),
    (255,0,0)
]

def get_distancesq(rgbValue, centroid):
    #print(f"rgbValue: {rgbValue}, centroid: {centroid}")
    dist_array = np.array([math.pow(a-b,2) for a,b in zip(rgbValue, centroid)])
    return np.sum(dist_array)

def get_note(x):
    #print(x)
    color_distances = np.array([(get_distancesq(x, centroid),centroidsToColors[centroid]) for centroid in centroids_arr])
    max_index = np.argmax(color_distances[:,0])
    #return numbersToNotes[color_distances[max_index, 1]]
    return color_distances[max_index, 1]

def sort_data(mapped_arr):
    unique_values, counts = np.unique(mapped_arr, return_counts=True)
    colors_and_counts = [(x, y) for x, y in zip(unique_values, counts)]
    sorted_data = np.array(sorted(colors_and_counts, key=lambda x: x[1], reverse=True))

def sonify_vector(vector):
    mapped_vector = np.array([get_note(rgbtuple) for rgbtuple in vector])
    return sort_data(mapped_vector)

def sonify_image(img_name):
    img = Image.open(img_name)
    img2 = img.convert('RGB')
    data = list(img2.getdata())
    mapped_arr = np.array([get_note(rgbtuple) for rgbtuple in data[0:img.width]])
    return sort_data(mapped_arr)

#last = np.array(np.unique(mapped_arr, return_counts=True))
#unique_values, counts = np.unique(mapped_arr, return_counts=True)
#colors_and_counts = [(x, y) for x, y in zip(unique_values, counts)]
#sorted_data = np.array(sorted(colors_and_counts, key=lambda x: x[1], reverse=True))