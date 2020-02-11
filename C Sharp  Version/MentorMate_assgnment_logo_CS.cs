using System;
public class Program
{

    public static void Main(string[] args)
    {
        //This is the solution for the MentorMate assignment using C#
        int mWidth = int.Parse(Console.ReadLine()); //get the width of the m character from the console
        DoubleMLetter mm = new DoubleMLetter();
        mm.Draw(mWidth);
    }
}
class DoubleMLetter
{
    private int cWidth;
    private int cLogoStarNumber;
    private int cLogoSideDashNumber;
    private int cLogoUpperDashNumber;
    private int cLogoLowerDashNumber;

    public DoubleMLetter() { }

    private String DrawLogoLine(int index) //returns the symbols for one line, for one M
    {
        string result = ""; //variable to hold the created line
        if (index <= this.cWidth / 2) //for the upper half of the logo this pattern is used
        {
            result =
                new String('-', this.cLogoSideDashNumber)
                + new String('*', this.cLogoStarNumber)
                + new String('-', this.cLogoUpperDashNumber)
                + new String('*', this.cLogoStarNumber)
                + new String('-', this.cLogoSideDashNumber);

            this.cLogoUpperDashNumber -= 2;
            this.cLogoStarNumber += 2;
        }
        else //for the lower half of the logo this pattern is used
        {
            this.cLogoStarNumber -= 2;
            result = 
                new String('-', this.cLogoSideDashNumber) 
                + new String('*', this.cWidth)
                + new String('-', this.cLogoLowerDashNumber) 
                + new String('*', this.cLogoStarNumber)
                + new String('-', this.cLogoLowerDashNumber)
                + new String('*', this.cWidth)
                + new String('-', this.cLogoSideDashNumber);
            this.cLogoLowerDashNumber += 2;
        }
        this.cLogoSideDashNumber -= 1;
        return result + result;//returns a string which contains the result 2 times, so that we have the needed parts for 2 "M" letters

    }
    public void Draw(int width) //prints the MM logo by given width for the M character
    {
        this.cWidth = width;
        this.cLogoStarNumber = width;
        this.cLogoSideDashNumber = width;
        this.cLogoUpperDashNumber = width;
        this.cLogoLowerDashNumber = 1;
        for (int i = 0; i <= width; i++)
        {
            Console.WriteLine(DrawLogoLine(i));
        }
    }
}
