# there is width+1 vertical lines and height+1 horizontal lines.
#every rectangle uses 2 vertical 2 horizontal
# choose(width+1,2)=width(width+1)/2
# length(length+1)/2 rectangles is width*length(width+1)*(length+1)/4
width=0
total=0
while total<2000000:
    width+=1
    total=width**2*(width+1)*(width+1)/4
print(width)
#hence max width and length is 54 so use 100 for safety
closest,area=10000000,0
for width in range(0,100):
    for length in range(0,width):
        current=width*length*(width+1)*(length+1)/4
        if current>2000000:
            current-=2000000
        else:
            current=2000000-current
        if current<closest:
            closest,area=current,length*width
print(area)
