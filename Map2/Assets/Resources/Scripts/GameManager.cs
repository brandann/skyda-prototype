using UnityEngine;
using System.Collections;

public class GameManager : MonoBehaviour {
	
	private char[,] map;
	private int xpos = 1;
	private int ypos = 1;
	
	private int SCREEN_HEIGHT = 9;
	private int SCREEN_WIDTH = 16;
	
	// Use this for initialization
	void Start () {
		MapGenerator m = new MapGenerator();
		map = m.getMap();	
	}
	
	// Update is called once per frame
	void Update () {
		
	}
	
	public void MoveMap(int dx, int dy){
		ypos += dy;
		xpos += dx;
		LoadMapScreen(xpos, ypos);
	}
	
	private void LoadMapScreen(int x, int y){
	
	}
}
