"""This is the solution for the MentorMate assignment using python"""
class DoubleMLetter:
    def logo_line(self,current_line): 
        result = "" 
        if current_line < self.m_width / 2: 
            result = (
                     "-" * self.logoSideDashNum
                     + "*" * self.logoStarNum\
                     + "-" * self.logoUpperDashNum
                     + "*" * self.logoStarNum\
                     + "-" * self.logoSideDashNum
                     )
            self.logoUpperDashNum -= 2
            self.logoStarNum += 2
        else: 
            self.logoStarNum -= 2
            result = (
                     "-" * self.logoSideDashNum
                     + "*" * self.m_width  \
                     +"-" * self.logoBottomHalfDashNum
                     + "*" * self.logoStarNum\
                     + "-" * self.logoBottomHalfDashNum
                     + "*" * self.m_width \
                     + "-" * self.logoSideDashNum
                     )
            self.logoBottomHalfDashNum += 2

        self.logoSideDashNum -= 1
        return result * 2  

    def print_logo(self,width): 
        self.m_width = width
        self.logoStarNum = width
        self.logoSideDashNum = width
        self.logoUpperDashNum = width
        self.logoBottomHalfDashNum = 1
        for current_line in range(width + 1):
           print(self.logo_line(current_line))

widthInput = int(input("Write the width of the double M: "))
doubleM = DoubleMLetter() 
doubleM.print_logo(widthInput) 
