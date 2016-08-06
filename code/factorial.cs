using System;
 
class Program
{
    static int Factorial(int number)
    {
        int accumulator = 1;
        for (int factor = 1; factor <= number; factor++)
        {
            accumulator *= factor;
        }
        return accumulator;
    }
 
    static void Main()
    {
        Console.WriteLine(Factorial(10));
    }
}
