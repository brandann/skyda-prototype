using UnityEngine;
using System.Collections;

public class MapBuilder : MonoBehaviour {

	public int worldwidth;
	public int worldheight;
	private int startX;
	private int startY;
	
	char[,] map;
	
	GameObject waterObject;
	GameObject grassObject;
	GameObject sandObject;
	GameObject treeObject;
	
	Tokens tok = new Tokens();
	
	// Use this for initialization
	void Start () {
		
	}
	
	public void generateMap(char[,] map){
		waterObject = Resources.Load("Prefabs/watertile") as GameObject;
		grassObject = Resources.Load("Prefabs/grasstile") as GameObject;
		sandObject = Resources.Load("Prefabs/sandtile") as GameObject;
		treeObject = Resources.Load("Prefabs/treetile") as GameObject;
		
		this.map = map;
		
		startX = 0;
		startY = 0;
		worldwidth = map.GetLength(0);
		worldheight = map.GetLength(1);
		worldwidth--;  //im not sure why, remove if this seems buggy
		worldheight--; //im not sure why, remove if this seems buggy
	
		print ("Initilizing World...");
		
		// make ponds
		print ("Digging Ponds...");
		
		// make grass tiles
		print ("Planting Grass...");
		
		// make sand where water and grass meet
		print ("Spreading Sand...");
		
		print ("Growing Trees...");
		
		// make map objects from map[,]
		print("Finalizing World...");
		
		print("World Is Initilized!");
		
		// move camera to the middle of world
		Camera camera = GameObject.Find ("Main Camera").GetComponent<Camera>();
		camera.transform.position = new Vector3(worldwidth/2, worldheight/2, -10);
	}
	
	// match all the tokens with prefabs, create pre fabs and place on map
	void loadTextures(){
		
		// make big grass instaed of lots of little ones
		loadBigGrass();
		
		// load the rest of the textures
		for(int i = 0; i < worldwidth; i++){
			for(int j = 0; j < worldheight; j++){
				if (map[i,j] == tok.getGRASS()){
					//do nothing
					//loadGrass(i,j);
				}
				else if (map[i,j] == tok.getWATER()){
					loadWater(i + startX , j + startY);
				}
				else if (map[i,j] == tok.getSAND()){
					loadSand(i + startX , j + startY);
				}
				else if (map[i,j] == tok.getTREE()){
					loadTree(i + startX , j + startY);
				}
			}
		}
	}
	
	// make 1 grass object and scale it to the 
	void loadBigGrass(){
		GameObject e = Instantiate(grassObject) as GameObject;
		GrassTile spawnedParticle = e.GetComponent<GrassTile>();
		if(spawnedParticle != null) {
			e.transform.position = new Vector3(worldwidth/2,worldheight/2 - 1.5f,0);
			e.transform.localScale = new Vector3(worldwidth,worldheight,1);
		}
		else {
			print ("error creating big grass");
		}
	}
	
	// instantiate grass object
	void loadGrass(int x, int y){
		GameObject e = Instantiate(grassObject) as GameObject;
		GrassTile spawnedParticle = e.GetComponent<GrassTile>();
		if(spawnedParticle != null) {
			e.transform.position = new Vector3(x,y,0);
		}
		else {
			print ("error creating grass");
		}
	}
	
	// instantiate water object
	void loadWater(int x, int y){
		GameObject e = Instantiate(waterObject) as GameObject;
		WaterTile spawnedParticle = e.GetComponent<WaterTile>();
		if(spawnedParticle != null) {
			e.transform.position = new Vector3(x,y,0);
		}
		else {
			print ("error creating water");
		}
	}
	
	// instantiate sand object
	void loadSand(int x, int y){
		GameObject e = Instantiate(sandObject) as GameObject;
		SandTile spawnedParticle = e.GetComponent<SandTile>();
		if(spawnedParticle != null) {
			e.transform.position = new Vector3(x,y,0);
		}
		else {
			print ("error creating sand");
		}
	}
	
	// instantiate tree object
	void loadTree(int x, int y){
		GameObject e = Instantiate(treeObject) as GameObject;
		TreeTile spawnedParticle = e.GetComponent<TreeTile>();
		if(spawnedParticle != null) {
			e.transform.position = new Vector3(x,y,0);
		}
		else {
			print ("error creating tree");
		}
	}
	
}
