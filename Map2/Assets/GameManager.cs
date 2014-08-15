using UnityEngine;
using System.Collections;

public class GameManager : MonoBehaviour {
	
	private char[,] map;
	
	// Use this for initialization
	void Start () {
		MapGenerator m = new MapGenerator();
		map = m.getMap();	
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
