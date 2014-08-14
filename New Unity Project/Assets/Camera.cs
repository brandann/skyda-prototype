using UnityEngine;
using System.Collections;

public class Camera : MonoBehaviour {

	string[] map;
	// Use this for initialization
	void Start () {
		//map = System.IO.File.ReadAllLines(@".\map.txt");
		//foreach (string s in map){
		//	print(s);
		//}
		loadInitialMap();
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
	
	void loadInitialMap(){
		GameObject mapObject = Resources.Load("Prefabs/MapGenerator") as GameObject;
		GameObject e = Instantiate(mapObject) as GameObject;
		MapBuilder spawnedParticle = e.GetComponent<MapBuilder>();
		if(spawnedParticle != null) {
			spawnedParticle.generateMap(0,0);
		}
		else {
			print ("error creating map");
		}
	}
}
