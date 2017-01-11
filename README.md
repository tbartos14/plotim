PLOTIM
======

This work-in-progress module currently includes tools for objects for creating graphs using the Tkinter canvas.
I plan to add classes for bar graphs, box-and-whisker plots, pie charts, and all sorts of other stuff.
This is my first project, and such the code may be poorly written/hard to read. Please excuse all violations
of PEP 8.

Here are the current classes available in plotim:

`linear_plot()` - Linear plotting tool

Here are the current functions available in plotim:

`vertical_text()` - Text reformatter for y-axis titles, automatic in linearplot()

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Below is a list of methods and attributes callable:

`linear_plot()` Methods:


`__init__()` : comes with the following parameters

**REQUIRED:**

**NOT REQUIRED:**
`windowx`: window size x, default 600  
`windowy`: window size y, default 400  
`bordernorth`: border, default 50  
`bordersouth`: border, default 50  
`bordereast`: border, default 30  
`borderwest`: border, default 50  
`title: title`, default "Linear Plot"  
`sortpoints`: whether x-points sorted to be ascending, default True  
`draw_lines`: whether lines are drawn connecting each point, default True  
`draw_points`: whether 3-pixel-radius circles are drawn on each point, default False  
`ytitle`: y-axis title, default "y"  
`xtitle`: x-axis title, default "x"  
`line_color`: color of inter-point lines, default "#0000bb"  
`image`: file location for images placed center on points, default None  


`set_data()`: comes with the following parameters

**REQUIRED:**
x: array of x points
y: array of y points

**NOT REQUIRED:**

`plot_data()`: comes with the following parameters

**REQUIRED:**

**NOT REQUIRED:**


`linear_plot()` Attributes:
`windowx`  
`windowy`  
`bordernorth`  
`bordersouth`  
`bordereast`  
`borderwest`  
`xpoints`  
`ypoints`  
`sortpoints` - whether points are sorted  
`originalyaxistitle` - title before reformatting with `vertical_text()`  
`yaxistitle`  
`xaxistitle`  
`yaxis` - 2-item array, min/max of ypoints  
`xaxis` - 2-item array, min/max of xpoints  
`draw_lines` - whether lines are drawn  
`draw_points` - whether points are drawn  
`graphx` - width of graph (pixels)  
`graphy` - height of graph (pixels)  
`linecolor` - color of lines drawn  
`image` - file location of image drawn on points  
`line_of_best_fit` - whether a line of best fit is drawn  
`yrange` - range of ypoints  
`xrange` - range of xpoints  
`yrangefactor` - power of 10 which the y increment is multiplied by  
`xrangefactor` - power of 10 which the x increment is multiplied by  
`yrangemin` - y axis range min  
`xrangemin` - x axis range min  
`yrangemax` - y axis range max  
`xrangemax` - x axis range max  
`additionalscaley` - number of additional increments added to y axis  
`additionalscalex` - number of additional increments added to x axis  
`yincrement` - size of y axis increment  
`xincrement` - size of x axis increment  
`bestfitslope` - slope of best fit line  
`bestfitintercept` - intercept of best fit line  
`bestfitequation` - equation printed on graph  


`vertical_text()`: comes with the following parameters

`text`: text to be made vertical

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

I will be bringing more functionality to plotim as I learn more about Python.
If you encounter any errors, do not be afraid to report them on GitHub.
