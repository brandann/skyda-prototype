using UnityEngine;
using System.Collections;

public class Camera : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		float H = Input.GetAxis ("Horizontal");
		float V = Input.GetAxis ("Vertical");
		this.transform.Translate(new Vector3(H*.05f,V*.05f,0));
	}
}
