using UnityEngine;
using System.Collections;

public class MapBuilder : MonoBehaviour {

	public int worldwidth;
	public int worldheight;
	
	string[,] map;
	
	GameObject waterObject;
	GameObject grassObject;
	GameObject sandObject;
	GameObject treeObject;
	
	private const string GRASS = "grass";
	private const string WATER = "water";
	private const string SAND = "sand";
	private const string TREE = "tree";
	
	private int startX = 0;
	private int startY = 0;
	
	
	// Use this for initialization
	void Start () {
		worldwidth--;
		worldheight--;
	}
	
	public void generateMap(int x, int y){
		waterObject = Resources.Load("Prefabs/watertile") as GameObject;
		grassObject = Resources.Load("Prefabs/grasstile") as GameObject;
		sandObject = Resources.Load("Prefabs/sandtile") as GameObject;
		treeObject = Resources.Load("Prefabs/treetile") as GameObject;
		map = new string[worldwidth , worldheight];
		
		startX = x;
		startY = y;
	
		print ("Initilizing World...");
		
		// make ponds
		print ("Digging Ponds...");
		initilizePond();
		
		// print out the string[,] for debugging
		for(int i = 0; i < worldwidth; i++){
			for(int j = 0; j < worldheight; j++){
				print(map[i,j]);
			}
		}
		
		// make 1 sheet of grass
		// make grass tiles
		print ("Planting Grass...");
		buildGrass();
		
		// make sand where water and grass meet
		print ("Spreading Sand...");
		buildSand();
		
		print ("Growing Trees...");
		buildTrees();
		
		// make map objects from map[,]
		print("Finalizing World...");
		loadTextures();
		
		print("World Is Initilized!");
		
		// move camera to the middle of world
		Camera camera = GameObject.Find ("Main Camera").GetComponent<Camera>();
		camera.transform.position = new Vector3(worldwidth/2, worldheight/2, -10);
	}
	
	void buildTrees(){
		int numoftrees = (int) Random.Range(1, (int) ((worldwidth*worldheight)*.1f) );
		for(int i = 0; i < numoftrees; i++){
			int locX = Random.Range(0,worldwidth-1);
			int locY = Random.Range(0,worldheight-1);
			if(map[locX,locY] == GRASS){
				map[locX,locY] = TREE;
			}
			else {
				i--;
			}
		}
	}
	
	void buildSand(){
		for(int i = 0; i < worldwidth; i++){
			for(int j = 0; j < worldheight; j++){
				 if (map[i,j] == WATER){
					for (int k = i-1; k < i+2; k++){
						if(k > 0 && k < worldwidth){
							for (int l = j-1; l < j+2; l++){
								if(l > 0 && l < worldheight){
									if(map[k,l] == GRASS){
										loadSand(k,l);
									}
								}
							}
						}
					}
				}
			}
		}
	}
	
	// match all the tokens with prefabs, create pre fabs and place on map
	void loadTextures(){
		
		// make big grass instaed of lots of little ones
		loadBigGrass();
		
		// load the rest of the textures
		for(int i = 0; i < worldwidth; i++){
			for(int j = 0; j < worldheight; j++){
				if (map[i,j] == GRASS){
					//do nothing
					//loadGrass(i,j);
				}
				else if (map[i,j] == WATER){
					loadWater(i + startX , j + startY);
				}
				else if (map[i,j] == SAND){
					loadSand(i + startX , j + startY);
				}
				else if (map[i,j] == TREE){
					loadTree(i + startX , j + startY);
				}
			}
		}
	}
	
	// put grass tiles in any blank positions
	private void buildGrass(){
		for(int i = 0; i < worldwidth; i++){
			for(int j = 0; j < worldheight; j++){
				if(map[i,j] == null)
					map[i,j] = GRASS;
			}
		}
	}
	
	// randomly select the number of ponds to buld
	// randomly select the position of the ponds
	private void initilizePond(){
		//int numofponds = (int) Random.Range(1,Mathf.Sqrt(worldwidth*worldheight));
		int numofponds = (int) Random.Range(1,(worldwidth*worldheight)/100);
		print ("Number of ponds: " + numofponds);
		for(int i = 0; i < numofponds; i++){
			buildPond(Random.Range(0,worldwidth-1),Random.Range(0,worldheight-1));
		}
	}
	
	// recurasvly build ponds outward
	private void buildPond(int x, int y){
		
		if(y >= worldheight || y < 0){
			return;
		}
		
		if(x >= worldwidth || x <= 0){
			return;
		}
		
		map[x,y] = WATER;
		
		int continuepond = Random.Range(0,50);
		if(continuepond == 0){
			return;
		}
		
		int u = Random.Range(1,5);
		int r = Random.Range(1,5);
		int d = Random.Range(1,5);
		int l = Random.Range(1,5);
		
		
		if(u == 1){
			buildPond(x,y+1);
		}
		if(r == 2){
			buildPond(x+1,y);
		}
		if(d == 3){
			buildPond(x,y-1);
		}
		if(l == 4){
			buildPond(x-1,y);
		}
	}
	
	// make 1 grass object and scale it to the 
	void loadBigGrass(){
		GameObject e = Instantiate(grassObject) as GameObject;
		grasstilescript spawnedParticle = e.GetComponent<grasstilescript>();
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
		grasstilescript spawnedParticle = e.GetComponent<grasstilescript>();
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
		watertilescript spawnedParticle = e.GetComponent<watertilescript>();
		if(spawnedParticle != null) {
			e.transform.position = new Vector3(x,y,0);
		}
		else {
			print ("error creating water");
		}
	}
	
	void loadSand(int x, int y){
		GameObject e = Instantiate(sandObject) as GameObject;
		sandtilescript spawnedParticle = e.GetComponent<sandtilescript>();
		if(spawnedParticle != null) {
			e.transform.position = new Vector3(x,y,0);
		}
		else {
			print ("error creating sand");
		}
	}
	
	void loadTree(int x, int y){
		GameObject e = Instantiate(treeObject) as GameObject;
		treetilescript spawnedParticle = e.GetComponent<treetilescript>();
		if(spawnedParticle != null) {
			e.transform.position = new Vector3(x,y,0);
		}
		else {
			print ("error creating tree");
		}
	}
	
}
