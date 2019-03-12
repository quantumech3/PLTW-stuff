package MediaLib;

/**
 * Written by Scott Burgert on 3/11/2019
 * <p>
 * Description:
 * 		I am too lazy to copy and paste the same stuff over and over again for Song, Book and Movie classes xd
 */

public class BaseMedia
{
	int rating = 0;
	String title = "";

	public BaseMedia(int rating, String title)
	{
		this.rating = rating;
		this.title = title;
	}

	public int getRating()
	{
		return rating;
	}

	public void setRating(int rating)
	{
		this.rating = rating;
	}

	public String getTitle()
	{
		return title;
	}

	public void setTitle(String title)
	{
		this.title = title;
	}
}
