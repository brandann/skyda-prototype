using UnityEngine;
using System.Collections;

public class Camera : MonoBehaviour {

	string[] map;
	// Use this for initialization
	void Start () {
		map = System.IO.File.ReadAllLines(@".\map.txt");
		foreach (string s in map){
			print(s);
		}
	}
	
	// Update is called once per frame
	void Update () {
	
	}
}
