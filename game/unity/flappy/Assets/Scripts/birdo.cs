using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class birdo : MonoBehaviour {

	public float ucma = 150f;
	public bool isDead = false;

	





	private Rigidbody2D birdrb;

	// Use this for initialization
	void Start () {
		birdrb = GetComponent<Rigidbody2D>();
	}
	
	// Update is called once per frame
	void Update () {
		
		if(isDead == false)
		{
			if (Input.GetKey("space"))
			{

				birdrb.velocity = Vector2.zero;
				birdrb.AddForce(new Vector2(0, ucma));

			}
			GameController.instance.BirdScored();
		}

	}


	void OnCollisionEnter2D(Collision2D other)
	{



		GameController.instance.BirdDamageTaken();



		if (GameController.instance.birdohealth <= 0)
		{

			// Zero out the bird's velocity
			birdrb.velocity = Vector2.zero;
			// If the bird collides with something set it to dead...
			isDead = true;
			//...tell the Animator about it...
			GameController.instance.BirdDied();
		}


	}

}
