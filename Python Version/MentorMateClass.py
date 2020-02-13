#used for rounding 
import math
class DoubleMLetter:
    #setting variables and iterating the lines. 
    def print_logo(self,width): 
        self.m_width = width
        self.logoStarNum = width
        self.logoSideDashNum = width
        self.logoUpperDashNum = width
        self.logoBottomHalfDashNum = 1
        for current_line in range(width + 1):
           print(self.logo_line(current_line))
    #for this specific example there is one more way to do it with placeholders
    def logo_line(self,current_line): 
        current_half_of_line = "" 
        #drawing upper half of M
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
        #drawing bottom half of M
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
    #this alternative usess less variables but instead it does more calculations 
    def alternative_print_logo(self, width):    
        
        half = math.floor((width + 1) / 2)
        current_half_of_line = ""
        
        for current_line in range(width + 1):
            current_half_of_line = "-" * (width - current_line)
            #drawing upper half of M
            if current_line < half: 
                current_half_of_line += (
                     "*" * (width + current_line * 2)
                     + "-" * (width - current_line * 2)
                     + "*" * (width + current_line * 2)
                     )
            #drawing bottom half of M
            else: 
                current_half_of_line += (
                     "*" * width
                     +"-" * math.floor((1 + 2 * (current_line-half)))
                     + "*" *  ((width*2 - (2 if width%2==0 else 1)) - (2 * (current_line - half)))
                     + "-" *   math.floor((1 + 2 * (current_line-half)))
                     + "*" * width
                     )
                     
            current_half_of_line += "-" * (width - current_line)
            print( current_half_of_line * 2 )
            #preparing for the next repetition
            current_half_of_line = "" 
            
        