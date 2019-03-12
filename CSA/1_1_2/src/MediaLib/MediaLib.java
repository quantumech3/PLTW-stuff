package MediaLib;

/**
 * Written by Scott Burgert on 3/11/2019
 *
 * Description:
 *
 */

public class MediaLib
{
	public static void main(String[] args)
	{
		// Maybe they should say "Welcome to MY Media Library" instead
		System.out.println("Welcome to your Media Library");

		// Initialize mumble rappers
		Song song1 = new Song(0, "All mumble rap");

		System.out.println(song1.getTitle());
	}
}
