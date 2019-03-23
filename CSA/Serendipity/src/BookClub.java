import java.util.Scanner;

/**
 * Written and developed by Scott Burgert on 3/23/19
 *
 * Description:
 * 		Asks the user to enter the number of book that he or she has purchased this month
 * 		and then displays the number of points awarded
 */

public class BookClub
{
	/**
	 *  Calculates how many points get awarded based off of bookAmt such that
	 *	This method was made instead of just switching in main() for modularity.
	 *	Serendipity book club definitely would need to calculate points for more then just display
	 *
	 *  bookAmt | pts recieved
	 *  ----------------------
	 *  0		| 0
	 *  1		| 5
	 *  2		| 15
	 *  3		| 30
	 *  4+		| 60
	 */
	public static int ptsFromBookAmt(int bookAmt)
	{
		switch (bookAmt)
		{
			case(0):
				return 0;
			case(1):
				return 5;
			case(2):
				return 15;
			case(3):
				return 30;
			default:
				return 60;
		}
	}

	public static void main(String[] args)
	{
		// Initialize input device
		Scanner input = new Scanner(System.in);

		// Get amount of books bought by user
		System.out.println("Please enter the amount of books you bought: ");
		int bookAmt = input.nextInt();

		// Display amount of points awarded
		System.out.println("Number of points you get: " + ptsFromBookAmt(bookAmt));
	}
}
