/**
 * Written and developed by Scott Burgert on 3/15/19
 *
 * Description:
 * 		Tester program for 'Population' class.
 * 		Asks user for population starting size, average daily increase and number of days they will multiply then
 * 	    ... uses the Population class to display the daily population on those days.
 *
 * 	    Requirements said "The program should display the daily population" so I took that to mean that the daily population
 * 	    should be displayed for all the days in the growth span specified by user.
 */

import java.util.Scanner;

public class Tester
{
	public static void main(String[] args)
	{
		// Init input device
		Scanner input = new Scanner(System.in);

		// Values gotten from user input
		int initPopulation = 0;
		double avgGrowthRate = 0;
		int growthSpan = 0;

		// "Do not accept a number less then 2 for the starting population...
		// a negative number for the average daily population increase
		// or a number less then 1 for the number of days they will multiply" as specified by requirements
		//
		// Loop until user inputs valid values
		do
		{
			System.out.println("Please enter starting size of population: ");
			initPopulation = input.nextInt();
		} while (initPopulation < 2);
		do
		{
			System.out.println("Please enter average daily population increase (as a percentage): ");
			avgGrowthRate = input.nextDouble();
		} while (avgGrowthRate < 0);
		do
		{
			System.out.println("Please enter number of days population will multiply");
			growthSpan = input.nextInt();
		} while (growthSpan < 1);

		// Instantiate 'Population' object with user defined values
		Population population = new Population(initPopulation, avgGrowthRate, growthSpan);

		// "Display the daily population" as specified by requirements
		// Will choose to interpret that as "Display the daily population [for each in range of growthSpan]"
		population.simGrowth();
	}
}
