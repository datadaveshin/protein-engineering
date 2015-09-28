import colorsys

def return_rgb(res_num, score):
    score = 1 - score          #uncomment to reverse score, thus colors
    rgb_list = list(colorsys.hsv_to_rgb(score * 0.6, 1.0, 1.0))
    print "set_color", "color_" + str(res_num), ",", rgb_list

def select_and_color(res_num):
    print "select res_" + str(res_num), ", resi", res_num 
    print "color", "color_" + str(res_num), ",", "res_" + str(res_num)
    # print "show sphere, name ca and", "res_" + str(res_num)
    
def color_by_score(res_num, score):
    return_rgb(res_num, score)
    select_and_color(res_num)

"""
tests
"""
# return_rgb("test_green", 0) # should return green
# return_rgb("test_yellow", 0.5) # should return yellow
# return_rgb("test_red", 1) # should return red

# print colorsys.hsv_to_rgb(0, 1.0, 1.0)
# print colorsys.hsv_to_rgb(120, 1.0, 1.0)
# print colorsys.hsv_to_rgb(359.0, 1.0, 1.0)

color_by_score(6, 0.0)
color_by_score(7, 0.1)
color_by_score(8, 0.2)
color_by_score(9, 0.3)
color_by_score(10, 0.4)
color_by_score(11, 0.5)
color_by_score(12, 0.6)
color_by_score(13, 0.7)
color_by_score(14, 0.8)
color_by_score(15, 0.9)
color_by_score(16, 1.0)
