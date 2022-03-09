using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ScrollingBackground : MonoBehaviour {

	private Rigidbody2D bg_rb2d;
	// Use this for initialization
	void Start () {

		bg_rb2d = GetComponent<Rigidbody2D>();
		bg_rb2d.velocity = new Vector2(GameController.instance.scrollSpeed, 0);
	


	}
	
	// Update is called once per frame
	void Update () {
		
		if(GameController.instance.gameOver == true)
		{
			bg_rb2d.velocity = new Vector2(0, 0);
		}


	}
}
