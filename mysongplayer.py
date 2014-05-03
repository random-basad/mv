import pygame,time,sys,thread,os;
from mutagen.mp3 import MP3;

pygame.init()

list=sys.argv[1:];
#["song.mp3","song5.mp3","song.mp3","song5.mp3"];
songnum=0;repeat=0;

def playsong(num):
	pygame.mixer.music.load(list[num])
	pygame.mixer.music.play()

def length():
        audio = MP3(list[songnum]);
        return audio.info.length
#	return os.path.getsize(list[songnum])*155.0/3748867;

song=pygame.mixer.music;

a = pygame.mixer.Sound(list[0])
print("length",a.get_length())

def selffun(name,deli):
	global songnum,repeat;
	while(1):
		if(songnum==-1):
			break;
		if(not(song.get_busy())):
			if(not(repeat)):
				songnum=(songnum+1)%len(list);
			playsong(songnum);
			time.sleep(2);


def user(name,deli):
	global songnum,list,repeat;
	while(1):
		input=raw_input("song Apps of mohit$ ");
		if(input==""):
			continue;
		if(input=="exit"):
			songnum=-1;
			exit();
		work=input.split();
		if(work[0]=="push"):
			pygame.mixer.music.queue("song5.mp3");
		elif(work[0]=="next"):
			songnum=(songnum+1)%len(list);
			playsong(songnum);
		elif(work[0]=="prv"):
			songnum=(songnum-1)%len(list);
			playsong(songnum);
		elif(work[0]=="play"):
			song.unpause();
		elif(work[0]=="pause"):
			song.pause();
		elif(work[0]=="stop"):
			playsong(songnum);
			song.pause();
		elif(work[0]=="re"):
			playsong(songnum);
		elif(work[0]=="inc"):
			song.set_volume(song.get_volume()+0.1);
		elif(work[0]=="red"):
			if(song.get_volume()<0.1):
				song.set_volume(0);
			else:
				song.set_volume(song.get_volume()-0.1);
		elif(work[0]=="vol"):
			if(len(work)==1):
				print "you didn't specifiy";
				continue;
			song.set_volume(float(work[1])/100.0);
		elif(work[0]=="loop"):
			repeat=not(repeat);
		elif(work[0]=="help"):
			print "help";
		elif(work[0]=="see"):
			print song.get_volume(),song.get_pos(),song.get_busy(),songnum,length();
			print "seeing";
		else:
			print work[0],": command not found";


try:
        thread.start_new_thread( user, ("mohit",1) )
        thread.start_new_thread( selffun , ("sain",1) )
except:
        print "Error: unable to start thread"


while 1:
	if(songnum==-1):
		break;
        time.sleep(1);
        pass


#time.sleep(900);
