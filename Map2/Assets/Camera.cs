using UnityEngine;
using System.Collections;

public class Camera : MonoBehaviour {

	char[,] map;
	// Use this for initialization
	void Start () {
		Mapper m = new Mapper();
		map = m.getMap();	
	}
	
	// Update is called once per frame
	void Update () {
		float H = Input.GetAxis ("Horizontal");
		float V = Input.GetAxis ("Vertical");
		/*
		if(H != 0){
			H = .25f * Mathf.Sign(H);
		}
		if(V != 0){
			V = .25f * Mathf.Sign(V);
		}
		*/
		this.transform.Translate(new Vector3(H*.05f,V*.05f,0));
	}
}
