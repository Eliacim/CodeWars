"""
4 kyu Pyramid Slide Down

https://www.codewars.com/kata/551f23362ff852e2ab000037

Lyrics...
Pyramids are amazing! Both in architectural and mathematical sense. If you have
a computer, you can mess with pyramids even if you are not in Egypt at the
time. For example, let's consider the following problem. Imagine that you have
a pyramid built of numbers, like this one here:


 /3/
 \7\ 4 
 2 \4\ 6 
8 5 \9\ 3

Here comes the task... Let's say that the 'slide down' is the maximum sum of
consecutive numbers from the top to the bottom of the pyramid. As you can see,
the longest 'slide down' is 3 + 7 + 4 + 9 = 23

Your task is to write a function longestSlideDown (in ruby/crystal/julia:
longest_slide_down) that takes a pyramid representation as argument and returns
its' largest 'slide down'. For example,

longestSlideDown([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) => 23

"""


def longest_slide_down(pyramid):
    for r in range(len(pyramid) - 1):
        row = len(pyramid) - 2 - r
        for col in range(len(pyramid[row])):
            pyramid[row][col] = max(
                pyramid[row][col] + pyramid[row + 1][col],
                pyramid[row][col] + pyramid[row + 1][col + 1]
            )
    return pyramid[0][0]


assert longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) == 23

assert longest_slide_down([
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]) == 1074
