"""This is the solution for the MentorMate assignment using python"""
class MentorMate:
    def logo_line(self,i):  # returns the symbols for one line, for one M
        result = "" # variable to hold the created line
        if i < self.m_width / 2:  # for the upper half of the logo this pattern is used
            result = "-" * self.logo_side_dash_num + "*" * self.logo_star_num\
                     + "-" * self.logo_upper_dash_num + "*" * self.logo_star_num\
                     + "-" * self.logo_side_dash_num
            self.logo_upper_dash_num -= 2
            self.logo_star_num += 2
        else: # for the lower half of the logo this pattern is used
            self.logo_star_num -= 2
            result = "-" * self.logo_side_dash_num + "*" * self.m_width  \
                     +"-" * self.logo_lower_dash_num + "*" * self.logo_star_num\
                     + "-" * self.logo_lower_dash_num + "*" * self.m_width \
                     + "-" * self.logo_side_dash_num
            self.logo_lower_dash_num += 2

        self.logo_side_dash_num -= 1
        return result * 2  # returns a string which contains the result 2 times, so that we have the needed parts for 2 "M" letters

    def print_logo(self,width): # prints the MM logo by given width for the M  character
        self.m_width = width
        self.logo_star_num = width
        self.logo_side_dash_num = width
        self.logo_upper_dash_num = width
        self.logo_lower_dash_num = 1
        for i in range(width + 1):
           print(self.logo_line(i))

m_width = int(input()) # get the m_widthber from the console
mm = MentorMate() # create a MentorMate class
mm.print_logo(m_width) # print the MentorMate logo
