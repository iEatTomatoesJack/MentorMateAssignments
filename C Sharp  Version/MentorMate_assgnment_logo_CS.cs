using System;
  class Program
    {

        static void Main(string[] args)
        {
            //This is the solution for the MentorMate assignment using C#
            int mWidth = int.Parse(Console.ReadLine()); //get the width of the m character from the console
            MentorMate mm = new MentorMate();
            mm.PrintLogo(mWidth);
        }
    }
    class MentorMate
    {
        private int mWidth;
        private int logoStarNumber;
        private int logoSideDashNumber;
        private int logoUpperDashNumber;
        private int logoLowerDashNumber;

        public MentorMate() { }

        private String CreateLogoLine(int index) //returns the symbols for one line, for one M
        {
            string result = ""; //variable to hold the created line
            if (index <= this.mWidth / 2) //for the upper half of the logo this pattern is used
             {
                result = new String('-', this.logoSideDashNumber) + new String('*', this.logoStarNumber)
                    + new String('-', this.logoUpperDashNumber) + new String('*', this.logoStarNumber)
                    + new String('-', this.logoSideDashNumber);

                this.logoUpperDashNumber -= 2;
                this.logoStarNumber += 2;
            }
            else //for the lower half of the logo this pattern is used
            {
                this.logoStarNumber -= 2;
                result = new String('-', this.logoSideDashNumber) + new String('*', this.mWidth)
                    + new String('-', this.logoLowerDashNumber) + new String('*', this.logoStarNumber)
                    + new String('-', this.logoLowerDashNumber) + new String('*', this.mWidth)
                    + new String('-', this.logoSideDashNumber);
                this.logoLowerDashNumber += 2;
            }
            this.logoSideDashNumber -= 1;
            return result + result;//returns a string which contains the result 2 times, so that we have the needed parts for 2 "M" letters

        }
        public void PrintLogo(int width) //prints the MM logo by given width for the M character
        {
            this.mWidth = width;
            this.logoStarNumber = width;
            this.logoSideDashNumber = width;
            this.logoUpperDashNumber = width;
            this.logoLowerDashNumber = 1;
            for (int i = 0; i <= width; i++)
            {
                Console.WriteLine(CreateLogoLine(i));
            }
        }
    }
