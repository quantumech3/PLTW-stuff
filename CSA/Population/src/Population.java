/**
 * Written and developed by Scott Burgert on 3/15/19
 *
 * Description:
 * 		Class that predicts the size of a population of organisms
 */

public class Population
{
	// Population growth stored as a percent (75) rather then a decimal (0.75) because the requirements say
	// "The class should store [the organisms] average population increase as a percentage"
	private double avgGrowthRate = 0;

	// Number of days that population will increase for
	private int growthSpan = 0;

	// As specified by requirements: "The class should store the starting number of organisms"
	// This stores the starting number of organisms
	private int initPopulation = 0;

	/**
	 * Class contains methods that predicts the size of a population of organisms
	 * @param avgGrowthRate
	 * @param growthSpan
	 * @param initPopulation
	 */
	public Population(int initPopulation, double avgGrowthRate, int growthSpan)
	{
		this.avgGrowthRate = avgGrowthRate;
		this.growthSpan = growthSpan;
		this.initPopulation = initPopulation;
	}

	/**
	 * Get initial population
	 */
	public int getInitPopulation()
	{
		return initPopulation;
	}

	/**
	 * Set initial population
	 * @param initPopulation
	 */
	public void setInitPopulation(int initPopulation)
	{
		this.initPopulation = initPopulation;
	}

	/**
	 * Get average growth rate of population
	 * @return
	 */
	public double getAvgGrowthRate()
	{
		return this.avgGrowthRate;
	}

	/**
	 * Set average growth rate of population
	 *
	 * @param avgGrowthRate
	 * @return
	 */
	public void setAvgGrowthRate(double avgGrowthRate)
	{
		this.avgGrowthRate = avgGrowthRate;
	}

	/**
	 * Get the period the population will grow for in days
	 * @return
	 */
	public int getGrowthSpan()
	{
		return this.growthSpan;
	}

	/**
	 * Set the period the population will grow for in days
	 * @param growthSpan
	 */
	public void setGrowthSpan(int growthSpan)
	{
		this.growthSpan = growthSpan;
	}

	/**
	 * Simulate and display population growth as specified by requirements requirements:
	 * 'The class should have a method that uses a loop to display the size of the population for each day'
	 *
	 * This method uses a loop to display the size of the population for each day
	 */
	public void simGrowth()
	{
		double avgPopulation = this.initPopulation;

		for (int i = 1; i <= growthSpan; i++)
		{
			System.out.println("Average population on day #" + i + ' ' + avgPopulation);
			avgPopulation += avgPopulation * (avgGrowthRate / 100.0);
		}
	}
}
