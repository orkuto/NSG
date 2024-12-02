int n = 15;
int y = 20;//迷路の大きさ
float len;
int[][] c = new int[n][y];

void setup(){
  size(700, 1000);
 
  len = width/float(n); //1マスの長さ
  
  //盤面の初期設定（c = 0:道, 1:壁）
  for(int i = 0; i < n; i ++){
  for(int j = 0; j < y; j ++){
    c[i][j] = 0; //一面壁にしておく
  }
  }
}

void draw(){
  background(255);
  
  //盤面の描画
  for(int i = 0; i < n; i ++){
  for(int j = 0; j < y; j ++){
    if(c[i][j] == 1){ fill(255); }
    else if(c[i][j] == 0){ fill(0); }
    stroke(230);
    rect(i*len, j*len, len, len);
  }
  }
  
  //"穴を掘る"処理
  int col, row;
  col = floor(random(2, n-2)); //ランダムに
  row = floor(random(2, y-2)); //1ヶ所を選ぶ
  if(col % 2 == 1 && row % 2 == 1 && c[col][row] == 0){ //選んだ座標が奇数で壁のとき
    makeRoute(col, row); //道を作る
  }
  print("\nint[][] map = {\n");
  for(int x=0;x<19;x++){
    print("{");
    for(int yd=0;yd<15;yd++){
      print(c[yd][x]+",");
    }
    print("},\n");
  }
  print("};");
}

//道を作る関数
void makeRoute(int col, int row){      
  //ランダムに進む方向を決める
  IntList array = new IntList();
  array.append(1);
  array.append(2);
  array.append(3);
  array.append(4);
  array.shuffle();
  
  for(int i = 0; i < 4; i ++){
    int p = array.get(i);
  
    int a = 0;
    int b = 0;
    if(p == 1){ a = 1; b = 0; } //右に
    else if(p == 2){ a = -1; b = 0; } //左に
    else if(p == 3){ a = 0; b = 1; } //下に
    else if(p == 4){ a = 0; b = -1; } //上に
  
    if(col+2*a < 0 || n-1 < col+2*a || row+2*b < 0 || y-1 < row+2*b){ //進んだ先が画面外のとき
      continue; //for文を抜ける
    }
    
    if(c[col+2*a][row+2*b] == 1){ //進んだ先が道のとき
      continue; //for文を抜ける
    }
    
    //道を掘る
    c[col][row] = 1;
    c[col+a][row+b] = 1;
    c[col+2*a][row+2*b] = 1;
    
    //掘り進んだ先を次の始点として道を作っていく
    makeRoute(col+2*a, row+2*b);
  }
}
