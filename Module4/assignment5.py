import pandas as pd
import glob
from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
from sklearn import manifold
# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
# .. your code here .. 
samples = []
colors = []
#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
# .. your code here .. 
path= 'C:/Users/IBM_ADMIN/Desktop/DATmaster/Module4/Datasets/ALOI/32'
filenames = glob.glob(path + '/*.png')
for file in filenames:
    img = misc.imread(file)
    X = img.reshape(-1)
    samples.append(X)
    colors.append('b')
#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
# .. your code here .. 
newpath= 'C:/Users/IBM_ADMIN/Desktop/DATmaster/Module4/Datasets/ALOI/32i'
filename = glob.glob(newpath + '/*.png')
for file in filename:
    img = misc.imread(file)
    X = img.reshape(-1)
    samples.append(X)
    colors.append('r')

#
# TODO: Convert the list to a dataframe
#
# .. your code here .. 
df = pd.DataFrame(samples)


#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
# .. your code here .. 
iso = manifold.Isomap(n_components = 3, n_neighbors = 6)
iso.fit(df)
T = iso.transform(df)


#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here .. 
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(T[:,0],T[:,1], marker='o',alpha=0.7, c = colors)



#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_title('isomap')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter(T[:,0], T[:,1], T[:,2], marker='o', alpha=0.7, c = colors)


plt.show()

