// Example program
#include <iostream>
#include <string>
using namespace std;

class DoubleMLetter
{
    private:
        int cWidth;
        int cLogoStarNumber;
        int cLogoSideDashNumber;
        int cLogoUpperDashNumber;
        int cLogoLowerDashNumber = 1;
        string drawLine(int index)
        {
             string oneLetterLineToBePrinted = "";
            if (index <= this->cWidth / 2)
            {
                oneLetterLineToBePrinted = 
                string(this->cLogoSideDashNumber, '-') 
                + string(this->cLogoStarNumber, '*') 
                + string(this->cLogoUpperDashNumber, '-') 
                + string(this->cLogoStarNumber, '*') 
                + string(this->cLogoSideDashNumber, '-');
                
                this->cLogoUpperDashNumber -= 2;
                this->cLogoStarNumber += 2;
            }
            else
            {   
                this->cLogoStarNumber -= 2;
                oneLetterLineToBePrinted = 
                string(this->cLogoSideDashNumber, '-') 
                + string(this->cWidth, '*') 
                + string(this->cLogoLowerDashNumber, '-') 
                + string(this->cLogoStarNumber, '*') 
                + string(this->cLogoLowerDashNumber, '-')
                + string(this->cWidth, '*')
                + string(this->cLogoSideDashNumber, '-');
                 this->cLogoLowerDashNumber += 2;
            }
            this->cLogoSideDashNumber -= 1;
            return oneLetterLineToBePrinted + oneLetterLineToBePrinted;
        };
    public:
        DoubleMLetter(){}
        DoubleMLetter(int fWidth)
        {
            this->cWidth =  fWidth;
            this->cLogoStarNumber = fWidth;
            this->cLogoSideDashNumber = fWidth;
            this->cLogoUpperDashNumber = fWidth;
        }
        ~DoubleMLetter(){};
        void draw();
};



void DoubleMLetter::draw()
{
   for (int i = 0; i <= this->cWidth; i++)
            {
                cout << this->drawLine(i) <<endl;
            }
    
}

int main()
{
  int widthOfM;
  cin >> widthOfM;
  DoubleMLetter * doubleM = new DoubleMLetter(widthOfM);
  doubleM->draw();
}
