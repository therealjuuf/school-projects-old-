using UnityEngine;
using System.Collections;
using UnityEngine.UI;
using UnityEngine.SceneManagement;


public class GameController : MonoBehaviour
{
	public static GameController instance;         //A reference to our game control script so we can access it statically.
	public Text SkorYazi;                      //A reference to the UI text component that displays the player's score.
	public GameObject OyunBittiYazi;             //A reference to the object that displays the text which appears when the player dies.
	public Text HealthYazi;



	public int birdohealth = 100;
	private int score = 0;                      //The player's score.
	public bool gameOver = false;               //Is the game over?
	public float scrollSpeed = -1.5f;


	void Awake()
	{
		//If we don't currently have a game control...
		if (instance == null)
			//...set this one to be it...
			instance = this;
		//...otherwise...
		else if (instance != this)
			//...destroy this one because it is a duplicate.
			Destroy(gameObject);
	}

	void Update()
	{
		//If the game is over and the player has pressed some input...
		if (gameOver && Input.GetKeyDown("space"))
		{
			//...reload the current scene.
			SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
		}
	}

	public void BirdScored()
	{
		//The bird can't score if the game is over.
		if (gameOver)
			return;
		//If the game is not over, increase the score...
		score++;
		//...and adjust the score text.
		SkorYazi.text = "Skor: " + score.ToString();
	}


	public void BirdDamageTaken()
	{
		//The bird can't score if the game is over.
		if (gameOver)
			return;
		//If the game is not over, increase the score...
		birdohealth -= 25;
		//...and adjust the score text.
		HealthYazi.text = "Can: " + birdohealth.ToString();
	}



	public void BirdDied()
	{
		//Activate the game over text.
		OyunBittiYazi.SetActive(true);
		//Set the game to be over.
		gameOver = true;
	}
}