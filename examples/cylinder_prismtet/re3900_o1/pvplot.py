from paraview.simple import *

dirc = "/home/yifanb/cylinder_prismtet/re3900_o1/"
files = [dirc+"cylinder_"+str(i)+".vtu" for i in range(0,10,2)]

reader = OpenDataFile (files)

view = CreateRenderView ()
#view = CreateView (" MultiSlice ")
#view. ZSliceValues = [1.5]

SaveScreenshot ("sample.png", view=view)
