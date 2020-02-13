"""This is the solution for the MentorMate assignment using python"""
import math
class DoubleMLetter:
    def logo_line(self,current_line): 
        current_half_of_line = "" 
        if current_line < self.m_width / 2: 
            current_half_of_line = (
                     "-" * self.logoSideDashNum
                     + "*" * self.logoStarNum
                     + "-" * self.logoUpperDashNum
                     + "*" * self.logoStarNum
                     + "-" * self.logoSideDashNum
                     )
            self.logoUpperDashNum -= 2
            self.logoStarNum += 2
        else: 
            self.logoStarNum -= 2
            current_half_of_line = (
                     "-" * self.logoSideDashNum
                     + "*" * self.m_width
                     +"-" * self.logoBottomHalfDashNum
                     + "*" * self.logoStarNum
                     + "-" * self.logoBottomHalfDashNum
                     + "*" * self.m_width
                     + "-" * self.logoSideDashNum
                     )
            self.logoBottomHalfDashNum += 2

        self.logoSideDashNum -= 1
        return current_half_of_line * 2  

    def print_logo(self,width): 
        self.m_width = width
        self.logoStarNum = width
        self.logoSideDashNum = width
        self.logoUpperDashNum = width
        self.logoBottomHalfDashNum = 1
        for current_line in range(width + 1):
           print(self.logo_line(current_line))
        

    def alternative_print_logo(self, width):
        half = math.floor((width + 1) / 2)
        current_half_of_line = ""
        for current_line in range(width + 1):
            current_half_of_line = "-" * (width - current_line)
            if current_line < half:
                current_half_of_line += (
                     "*" * (width + current_line * 2)
                     + "-" * (width - current_line * 2)
                     + "*" * (width + current_line * 2)
                     )
            else: current_half_of_line += (
                     "*" * width
                     +"-" * math.floor((1 + 2 * (current_line-half)))
                     + "*" *  (width*2 - 2 if width%2==0 else 1)
                     + "-" *   math.floor((1 + 2 * (current_line-half)))
                     + "*" * width
                     )
            current_half_of_line += "-" * (width - current_line)
            print( current_half_of_line * 2 )
            current_half_of_line = ""
        return 0
        



#widthInput = int(input("Write the width of the double M: "))
doubleM = DoubleMLetter() 
doubleM.print_logo(3)
doubleM.alternative_print_logo(3) 
