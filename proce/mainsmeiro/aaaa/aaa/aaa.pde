PImage img;
PImage floor;
PImage wall;
PImage chara;
PImage[] player= new PImage[5];
PImage blood;
PImage bar;
PImage over;
PImage block;
PImage bridge;
PImage[] magic = new PImage[16];
PImage result;
PImage hyoshi;
PImage[] bomb = new PImage[4];

Opscreen op;
Controler cnt;
Displayer disp;
Maingame mg;
Maingame mc;
Maingame mk;
Gameend ge;


//prog 0,1 opning 3 menyu gamen 100 tutorial 200 main game 300 ending 1000 gameover 2000 result 2432 kirikae

void setup(){
  translate(0,0);
  size(400,400);
  frameRate(30);
  background(0);
  rectMode(CENTER);
  img = loadImage("bg.png");
  floor = loadImage("iron_block.png");
  wall = loadImage("packed_ice.png");
  chara = loadImage("nncy.png");
  for (int i=0; i<player.length; i++) {
    player[i] = loadImage("chr"+i+".png");
  }
  for (int i=0; i<magic.length; i++) {
    magic[i] = loadImage("bridge"+i+".png");
  }
  for (int i=0; i<bomb.length; i++) {
    bomb[i] = loadImage("bomb"+i+".png");
  }
  bar = loadImage("select.png");
  over = loadImage("gameover.png");
  blood = loadImage("bloodend.png");
  block = loadImage("block_select.png");
  bridge = loadImage("bridge.png");
  result = loadImage("nny.png");
  hyoshi = loadImage("nanashi.png");
  mc = new Maingame();
  mk = new Maingame();
  ge = new Gameend();
}

int progress=0;
int fps=5;
int x=0;
int chprog=0;
int chrani=0;
char rank= 70;
int score=5000;
int flagc=0;
int timeplus=10;
float tflag;
float ms;
float result_time;




// start 2 goal 3 bomb 4 bridge state 5 research state 6
int[][] map = {
{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
{0,1,1,1,1,1,0,1,1,1,1,1,0,2,0},
{0,1,0,0,0,1,0,1,0,0,0,1,0,1,0},
{0,1,0,1,4,1,0,1,1,1,0,1,1,4,0},
{0,1,0,0,0,0,0,1,0,1,0,0,0,0,0},
{0,1,1,1,0,1,4,1,0,1,0,4,1,1,0},
{0,0,0,1,0,1,0,0,0,1,0,1,0,1,0},
{0,1,0,1,0,1,1,1,0,4,1,1,0,1,0},
{0,1,0,1,0,0,0,0,0,0,0,0,0,1,0},
{0,1,0,1,4,1,1,1,1,4,1,1,1,1,0},
{0,1,0,0,0,0,0,0,0,0,0,0,0,1,0},
{0,1,1,1,1,1,0,1,1,1,1,4,1,1,0},
{0,0,0,0,0,1,0,1,0,0,0,0,0,0,0},
{0,1,1,4,1,4,0,1,1,1,1,1,1,1,0},
{0,1,0,0,0,0,0,0,0,0,0,0,0,1,0},
{0,1,1,1,1,1,1,1,1,1,0,1,1,1,0},
{0,1,0,0,0,1,0,0,0,1,0,1,0,0,0},
{0,3,1,1,0,1,1,4,0,1,0,1,4,1,0},
{0,0,0,1,0,0,0,1,0,1,1,1,0,4,0},
{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
};

void draw(){
  ms = millis();
  if(progress == 0){
    op = new Opscreen();
    op.fpscount();
    op.backg();
    progress = op.fpscount();
  }
  if(progress == 1){
    cnt = new Controler();
    op.sctitle();
    if(cnt.keyjudge(0,'a')==1){
      progress= 2432;
      disp = new Displayer();
      chprog=3;
      disp.clearall();
    }
  }
  if(progress==2432){
    op.scchange(chprog,10);
  }
  if(progress == 3){
    op.menyoo();
    
    if(cnt.musclk(0,300,75,125,0)==1){
      println("clicke1");
      progress=2432;
      chprog=100;
      disp.clearall();
    }
    if(cnt.musclk(0,250,175,225,0)==1){
      println("clicke2");
      progress=2432;
      chprog=200;
      mg = new Maingame();
      tflag=ms;
      disp.clearall();
    }
    if(cnt.musclk(0,200,275,325,0)==1){
      println("clicke3");
      progress=2432;
      chprog=300;
      disp.clearall();
    }
  }
  if(progress==100){
    fill(255,255,255);
    rect(200,200,400,400);
    fill(random(255),random(255),random(255));
    textSize(random(20,40));
    text("comming soon!! maybe",mouseX,mouseY);
  }
  if(progress==200){
    if(score<0){
      score=0;
    }
    mg.mapwrite();
    if(mg.state==0){
      result_time = ms-tflag;
      mg.chr_clr();
    }
    if(mg.state==1){
       mg.grid_search();
       mg.grid_write(0);
    }
    if(mg.state==2){
      mg.grid_search();
      mg.grid_write(1);
    }
    mg.mode_ui_walk();
    mg.mode_ui_bridge();
    mg.mode_ui_research();
    mg.select_bar();
    flagc=flagc+1;
    if(mk.time_flagger(timeplus)==1){
      score = score -1;
      if(flagc>600){
        timeplus=1;
      }
    }
  }
  if(progress==300){
    mk.credit();
  }
  if(progress==1000){
    if(mg.bomb_ani(200,200,300)==1){
      progress=1001;
    }
  }
  if(progress==1001){
    ge.badend();
  }
  if(progress==2000){//result
    ge.result();
  }
}

class Controler{//mouse no atari hantei
  int musclk(int srangex,int brangex,int srangey,int brangey,int mode){
    if(mode==0){
      if(mouseX>srangex&&mouseX<brangex&&mouseY>srangey&&mouseY<brangey&&mousePressed==true){
        return 1;
      }
      else{
        return 0;
      }
    }
    if(mode==1){
      if(mouseX>srangex&&mouseX<brangex&&mouseY>srangey&&mouseY<brangey){
        return 1;
      }
      else{
        return 0;
      }
    }
    else{
      return 0;
    }
  }
  int keyjudge(int onff,char code){
    if(keyPressed==true){
      if(onff==1){
        if(key==code){
          return 1;
        }
        else{
          return 0;
        }
      }
      if(onff==0){
        return 1;
      }
    }
    else{
      return 0;
    }
    return 0;
  }
}

class Displayer{
  public int rcolr=255;
  public int gcolr=255;
  public int bcolr=255;
  void clearall(){//haikei wo shironi suru
    fill(rcolr,gcolr,bcolr);
    rect(200,200,400,400);
  }
}
      


class Opscreen{
  private int mov=0;
  private int col;
  int fpscount(){
    frameRate(fps);
    fps = fps+1;
    if(fps>=60){
      return 1;
    }
    return 0;
  }
    
  void backg(){//randam na sankaku wo hyozi
      stroke(random(255),random(255),random(255));
      strokeWeight(random(100));
      fill(random(255),random(255),random(255),random(255));
      triangle(random(400),random(400),random(400),random(400),random(400),random(400));
      strokeWeight(1);
      stroke(0);
  }
  void sctitle(){//taitoru dasu
    rect(mov,65,5,50);
    if (mov<400){
      mov = mov+4;
      println(mov/4+"%");
    }
    else if(mov==400){
      textSize(40);
      if(mk.time_flagger(5)==1){
        fill(random(0,100));
      }
      text("mainsmeiro",90,80);
      textSize(25);
      image(hyoshi,0,70,400,400);
      text(" --click any key to start game--",0,300);
      
    }
  }
  void scchange(int prog,int speed){//gamen no kirikae 
    fill(col,col,col);
    rect(200,200,400,400);
    col = col+speed;
    if(col>=256){
      progress = prog;
      col=0;
    }
  }
  
  void menyoo(){
    fill(0,0,0);
    textSize(30);
    text("serect mode",100,50);
    rect(100,100,random(400),50);
    rect(100,200,random(300),45);
    rect(100,300,random(200),40);
    fill(255,255,255);
    if(random(1)<=0.9){
      text("serect mode",101,51);
    }
    textSize(20);
    text("TUTORIAL",20,110);
    text("MAIN GAME",20,210);
    text("CREDIT",20,310);
    fill(0,0,0);
    text("TUTORIAL",18,110);
    text("MAIN GAME",18,210);
    text("CREDIT",18,310);
    image(chara,160,-20,322,487);
  }
}

class Maingame{
  int xzahyo=10;
  int yzahyo=10;
  int red=255,blue=255,green=255;
  int flagger=0;
  int plmin=1;
  int[] mouse_zahyo = new int[2];
  PFont font = createFont("HG創英角ﾎﾟｯﾌﾟ体",35);
  PFont font2 = createFont("HG創英角ﾎﾟｯﾌﾟ体",20);
  PFont jpane = createFont("ＭＳ Ｐ明朝",20);
  int mg_effect=0;
  int move=0;
  int bb=0;
  int bbc=0;
  
  public int state = 0; //0 = walk 1= bridge 2 = research 3
  
  
  void grid_search(){
    int x=0;
    int y=0;
    while(x<400){
      if(mouseX<x){
        println(x/20);
        if(x/20>14){
          x=300;
        }
        mouse_zahyo[0]=x/20;
        x=400;
      }
      x=x+20;
    }
    while(y<=400){
      if(mouseY<y){
        println(y/20);
        if(y/20>19){
          y=400;
        }
        mouse_zahyo[1]=y/20;
        y=420;
      }
      y=y+20;
    }
  }
  void grid_write(int mode){
    if(mode==1){
      if(map[mouse_zahyo[1]-1][mouse_zahyo[0]-1]==0){
        imageMode(CORNER);
        block.resize(20,20);
        image(block,(mouse_zahyo[0]-1)*20,(mouse_zahyo[1]-1)*20);
        research();
      }
    }
    if(mode==0){
      if(map[mouse_zahyo[1]-1][mouse_zahyo[0]-1]==1||map[mouse_zahyo[1]-1][mouse_zahyo[0]-1]==4){
        imageMode(CORNER);
        block.resize(20,20);
        image(block,(mouse_zahyo[0]-1)*20,(mouse_zahyo[1]-1)*20);
        bridge();
      }
    }
  }
  void bridge(){//hashi wo kakeru
    if(mouseButton==LEFT){
      if(map[mouse_zahyo[1]-1][mouse_zahyo[0]-1]==4){
        score=score+500;
      }
      else{
        score = score-250;
      }
      map[mouse_zahyo[1]-1][mouse_zahyo[0]-1]=5;
    }
  }
  void research(){//kabe wo chosa
    if(mouseButton==RIGHT){
      map[mouse_zahyo[1]-1][mouse_zahyo[0]-1]=6;
      score = score-50;
    }
  }
  
  void select_bar(){//nani wo sentaku shiteruka
    if(state==0){
      imageMode(CENTER);
      bar.resize(50,50);
      image(bar,350,120);
    }
    else if(state==1){
      imageMode(CENTER);
      bar.resize(50,50);
      image(bar,350,200);
    }
    else{
      imageMode(CENTER);
      bar.resize(50,50);
      image(bar,350,280);
    }
  }
  int time_flagger(int cnt){//nan fps ni itido kakunin suruka
    if(flagger==cnt){
      flagger=0;
      return 1;
    }
    flagger= flagger+1;
    return 0;
  }
  void colupper(int lr,int lg,int lb,int speed){//scchange no ashu
    if(red>=lr){
      red = red - lr/speed;
      println(red);
    }
    if(blue>=lb){
      blue = blue - lb/speed;
    }
    if(green>=lg){
      green = green - lg/speed;
    }
    fill(red,green,blue);
  }
  void mode_ui_walk(){
    fill(220,255,255);
    if(cnt.musclk(330,370,100,140,0)==1){
      state=0;
    }
    else if(cnt.musclk(330,370,100,140,1)==1){
      colupper(160,120,255,30);
    }
    else if(cnt.musclk(330,370,100,140,1)==0&&cnt.musclk(330,370,180,220,1)==0&&cnt.musclk(330,370,260,300,1)==0){
      red=255;
      blue=255;
      green=255;
    }
    rect(350,120,40,40,10);
    fill(0,0,0);
    textFont(font);
    text("W",340,135);
  }
  void mode_ui_bridge(){
    fill(220,255,255);
    if(cnt.musclk(330,370,180,220,0)==1){
      state=1;
    }
    else if(cnt.musclk(330,370,180,220,1)==1){
      colupper(160,120,255,30);
    }
    else if(cnt.musclk(330,370,100,140,1)==0&&cnt.musclk(330,370,180,220,1)==0&&cnt.musclk(330,370,260,300,1)==0){
      red=255;
      blue=255;
      green=255;
    }
    rect(350,200,40,40,10);
    fill(0,0,0);
    textFont(font);
    text("B",340,215);
  }
  void mode_ui_research(){
    fill(220,255,255);
    if(cnt.musclk(330,370,260,300,0)==1){
      state=2;
    }
    else if(cnt.musclk(330,370,260,300,1)==1){
      colupper(160,120,255,30);
    }
    else if(cnt.musclk(330,370,100,140,1)==0&&cnt.musclk(330,370,180,220,1)==0&&cnt.musclk(330,370,260,300,1)==0){
      red=255;
      blue=255;
      green=255;
    }
    rect(350,280,40,40,10);
    fill(0,0,0);
    textFont(font);
    text("R",340,295);
  }
  void gameover(){
    progress=1000;
    imageMode(CORNER);
      
    //image(over,0,0,400,400);
  }
  void chr_clr(){
    if(xzahyo+1<15&&keyPressed==false&&map[yzahyo][xzahyo+1]!=0&&map[yzahyo][xzahyo+1]!=6){
      if(key==('d')){
        if(map[yzahyo][xzahyo+1]==4){
          gameover();
        }
        if(map[yzahyo][xzahyo+1]==3){
          progress=2432;
          chprog=2000;
        }
        else{
          map[yzahyo][xzahyo]=1;
          map[yzahyo][xzahyo+1]=2;
        }
        key = 'h';
      }
    }
    if(xzahyo-1>=0&&keyPressed==false&&map[yzahyo][xzahyo-1]!=0&&map[yzahyo][xzahyo-1]!=6){
      if(key==('a')){
        if(map[yzahyo][xzahyo-1]==4){
          gameover();
        }
        if(map[yzahyo][xzahyo-1]==3){
          progress=2432;
          chprog=2000;
        }
        else{
          map[yzahyo][xzahyo]=1;
          map[yzahyo][xzahyo-1]=2;
        }
        key= 'h';
      }
    }
    if(yzahyo+1<20&&keyPressed==false&&map[yzahyo+1][xzahyo]!=0&&map[yzahyo+1][xzahyo]!=6){
      if(key==('s')){
        if(map[yzahyo+1][xzahyo]==4){
          gameover();
        }
        if(map[yzahyo+1][xzahyo]==3){
          progress=2432;
          chprog=2000;
        }
        else{
          map[yzahyo][xzahyo]=1;
          map[yzahyo+1][xzahyo]=2;
        }
        key = 'h';
      }
    }
    if(yzahyo-1>=0&&keyPressed==false&&map[yzahyo-1][xzahyo]!=0&&map[yzahyo-1][xzahyo]!=6){
      if(key==('w')){
        if(map[yzahyo-1][xzahyo]==4){
          gameover();
        }
        if(map[yzahyo-1][xzahyo]==3){
          progress=2432;
          chprog=2000;
        }
        else{
          map[yzahyo][xzahyo]=1;
          map[yzahyo-1][xzahyo]=2;
        }
        key= 'h';
      }
    }
  }
  void credit(){
    textFont(jpane);
    fill(10,10,10);
    rect(200,200,400,400);
    fill(0,200,0);
    translate(0,move);
    text("マインスメイロ　スタッフロール\n\n\n私の夢はスタッフロールを自分で埋めること\n\n\n企画　自分\n\n\nキャラクターデザイン/原画　自分\n\n\n原案・脚本　ストーリーあるけど時間なかった \n\n\n脚本協力　自分だけ\n\n\n",10,400);
    text("グラフィック　自分\n\n\nシステムプランナー/進行管理　自分\n\n\nシステムグラフィック/ムービー　自分\n\n\n表紙キャラクターデザイナー　同じ席の人\n\n\nメニューキャラクターデザイナー　同じ席の人\n\n\nリザルトキャラクターデザイナー　同じ席の人\n\n\n爆発デザイナー　同じ席の人\n\n\n",10,900);
    text("構成協力　自分\n\n\nデバッグ・テストプレイ　自分\n\n\nプロデューサー　自分\n\n\nディレクター　自分\n\n\nプログラム　自分\n\n\nサポート　自分？\n\n\n制作進行　自分\n\n\n",10,1450);
    text("ディレクター　本人\n\n\nプロデューサー　本人\n\n\nスペシャルサンクス　キナリエル　アイボリー",10,2000);
    
    move=move-2;
  }
  int bomb_ani(int x,int y,int size){
    image(bomb[bb],x,y,size,size);
    if(bbc==5){
      bb=bb+1;
      bbc=0;
      if(bb==4){
        bb=0;
        mapwrite();
        imageMode(CENTER);
        return 1;
      }
    }
    bbc=bbc+1;
    return 0;
  }
  
  void mapwrite(){
    int range;
    int plu;
    int goal;
    imageMode(CORNER);
    image(img,0,0,400,400);
    textFont(font2);
    text("SCORE\n"+score,310,25);
    text("______",310,60);
    for(int x=0;x<15;x=x+1){
      for(int y=0;y<20;y=y+1){
        range = 1000;
        plu = 0;
        goal = 0;
        if(map[y][x]==4){
          image(floor,0+x*20,0+y*20,20,20);
        }
        if(map[y][x]!=0){
          image(wall,0+x*20,0+y*20,20,20);
        }
        if(map[y][x]==0){
          image(floor,0+x*20,0+y*20,20,20);
        }
        if(map[y][x]==6){
          image(wall,0+x*20,0+y*20,20,20);
          for(int xx=0;xx<15;xx++){
            for(int yy=0;yy<20;yy++){
              if(map[yy][xx]==3){
                if((xx-x)*(xx-x)>=(yy-y)*(yy-y)){
                  if(x-xx>=0){
                    goal = x - xx;
                  }
                  else{
                    goal = xx - x;
                  }
                }
                else{
                  if(y-yy>=0){
                    goal = y - yy;
                  }
                  else{
                    goal = yy - y;
                  }
                }
              }
              if(map[yy][xx]==4){
                if((xx-x)*(xx-x)>=(yy-y)*(yy-y)){
                  if(x-xx>=0){
                    plu = x - xx;
                  }
                  else{
                    plu = xx - x;
                  }
                }
                else{
                  if(y-yy>=0){
                    plu = y - yy;
                  }
                  else{
                    plu = yy - y;
                  }
                }
                if(range>plu){
                  range=plu;
                }
              }
            }
          }
          textSize(10);
          text(range,0+x*20,10+y*20);
          println(range);
          text(goal,0+x*20,20+y*20);
        }
        if(map[y][x]==5){
          image(magic[mg_effect],0+x*20,0+y*20,20,20);
          if(mc.time_flagger(5)==1){
            mg_effect=mg_effect+1;
          }
          if(mg_effect==16){
            map[y][x]=1;
            mg_effect=0;
            
          }
        }
        if(map[y][x]==2){
          image(wall,0+x*20,0+y*20,20,20);
          if(chrani==4){
            plmin=-1;
          }
          if(chrani==0){
            plmin=1;
          }
          image(player[chrani],0+x*20,0+y*20,20,20);
          if(mg.time_flagger(5)==1){
            chrani=chrani+1*plmin;
          }
          yzahyo=y;
          xzahyo=x;
        }
      }
    }
  }
}

class Gameend{
  int count=0;
  void badend(){
    if(mg.time_flagger(5)==1){
      image(blood,200,count,400,100);
      count=count+15;
      if(count >= 600){
        fill(100,0,0);
        textSize(90);
        text("GAME OVER",0,200);
      }
    }
  }
  void result(){
    imageMode(CORNER);
    image(result,0,0,566,400);
    PFont font = createFont("HG創英角ﾎﾟｯﾌﾟ体",35);
    textFont(font);
    fill(255,255,0);
    count = 70 - score/400;
    if(count<65){
      count = 83;
    }
    rank = (char)count;
    text(rank,30,60);
    fill(0);
    text("______",10,65);
    text("Score\n"+score,10,110);
    text("________",10,165);
    text("Time",10,210);
    text(result_time/1000+"s",10,260);
    text("_________",10,265);
  }
}


      
