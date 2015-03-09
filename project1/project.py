#/usr/bin/python3
###############################################################################
# CPSC 335 Project 1
# Spring 2015
#
# Authors: Daniel Jordan
###############################################################################

# constant parameters
CANVAS_WIDTH = 700
CANVAS_HEIGHT = 700
CANVAS_MARGIN = 20
BOX_OUTLINE_COLOR = 'olive'
BOX_FILL_COLOR = 'mint cream'
HULL_OUTLINE_COLOR = 'gold'
HULL_FILL_COLOR = 'linen'
INTERIOR_POINT_COLOR = 'gray'
POINT_RADIUS = 2
OUTLINE_WIDTH = 2

import math, random, time, tkinter, sys

# Class representing one 2D point.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# input: a list of Point objects
# output: a 4-tuple (x_min, y_min, x_max, y_max)
def bounding_box(points):
    xMin = CANVAS_MARGIN
    xMax = 0 
    yMin = CANVAS_MARGIN 
    yMax = 0

    for p in points:
        if(p.x >= xMax):
            xMax = p.x
        elif(p.x <= xMin):
            xMin = p.x
        if(p.y >= yMax):
            yMax = p.y
        elif(p.y <= yMin):
            yMin = p.y

    return (xMin, yMin, xMax, yMax)

# input: a list of Point objects
# output: a list of the Point objects on the convex hull boundary
def convex_hull(points):
    H = []
    for p in points: 
        for q in points: 
            if p != q: 
                a = q.y-p.y #delta y
                b = p.x-q.x # delta x
                c = (p.x*q.y)-(p.y*q.x) # x,y cross product
                k = [] #points above the line            
                for t in points:
                    if t != p and t != q:
                        if (a*t.x)+(b*t.y)-c > 0:
                            k.append(t)
                if len(k) == 0 or len(k) == len(points)-2: 
                    if p not in H: 
                        H.append(p) 
                    if q not in H: 
                        H.append(q) 
    return H 
###############################################################################
# The following code is reponsible for generating instances of random
# points and visualizing them. You can leave it unchanged.
###############################################################################

# input: an integer n >= 0
# output: n Point objects with all coordinates in the range [0, 1]
def random_points(n):
    return [Point(random.random(), random.random())
            for i in range(n)]

# translate coordinates in [0, 1] to canvas coordinates
def canvas_x(x):
    return CANVAS_MARGIN + x * (CANVAS_WIDTH - 2*CANVAS_MARGIN)
def canvas_y(y):
    return CANVAS_MARGIN + y * (CANVAS_HEIGHT - 2*CANVAS_MARGIN)

# extract the x-coordinates (or y-coordinates respectively) from a
# list of Point objects
def xs(points):
    return [p.x for p in points]
def ys(points):
    return [p.y for p in points]

# input: a non-empty list of numbers
# output: the mean average of the list
def mean(numbers):
    return sum(numbers) / len(numbers)

# input: list of Point objects
# output: list of the same objects, in clockwise order
def clockwise(points):
    if len(points) <= 2:
        return points
    else:
        center_x = mean(xs(points))
        center_y = mean(ys(points))
        return sorted(points,
                      key=lambda p: math.atan2(p.y - center_y,
                                               p.x - center_x),
                      reverse=True)

# Run one trial of one or both of the algorithms.
#
# 1. Generates an instance of n random points.
# 2. If do_box is True, run the bounding_box algorithm and display its output.
# 3. Likewise if do_hull is True, run the convex_hull algorithm and display
#    its output.
# 4. The run-times of the two algorithms are measured and printed to standard
#    output.
def trial(do_box, do_hull, n):
    print('generating n=' + str(n) + ' points...')
    points = random_points(n)

    if do_box:
        print('bounding box...')
        start = time.perf_counter()
        (x_min, y_min, x_max, y_max) = bounding_box(points)
        end = time.perf_counter()
        print('elapsed time = ' + str(end - start) + ' seconds')

    if do_hull:
        print('convex hull...')
        start = time.perf_counter()
        hull = convex_hull(points)
        end = time.perf_counter()
        print('elapsed time = ' + str(end - start) + ' seconds')

    w = tkinter.Canvas(tkinter.Tk(),
                       width=CANVAS_WIDTH, 
                       height=CANVAS_HEIGHT)
    w.pack()

    if do_box:
        w.create_polygon([canvas_x(x_min), canvas_y(y_min),
                          canvas_x(x_min), canvas_y(y_max),
                          canvas_x(x_max), canvas_y(y_max),
                          canvas_x(x_max), canvas_y(y_min)],
                         outline=BOX_OUTLINE_COLOR,
                         fill=BOX_FILL_COLOR,
                         width=OUTLINE_WIDTH)

    if do_hull:
        vertices = []
        for p in clockwise(hull):
            vertices.append(canvas_x(p.x))
            vertices.append(canvas_y(p.y))

        w.create_polygon(vertices,
                         outline=HULL_OUTLINE_COLOR,
                         fill=HULL_FILL_COLOR,
                         width=OUTLINE_WIDTH)

    for p in points:
        w.create_oval(canvas_x(p.x) - POINT_RADIUS,
                      canvas_y(p.y) - POINT_RADIUS,
                      canvas_x(p.x) + POINT_RADIUS,
                      canvas_y(p.y) + POINT_RADIUS,
                      fill=INTERIOR_POINT_COLOR)

    tkinter.mainloop()

###############################################################################
# This main() function runs multiple trials of the algorithms to
# gather empirical performance evidence. You should rewrite it to
# gather the evidence you need.
###############################################################################
def main():
    trial(True, True, 500)

if __name__ == '__main__':
    main()
