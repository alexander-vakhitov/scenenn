all: PlaybackSync.o
	g++ -O3 -o playback PlaybackSync.o -lboost_system -lboost_filesystem -lOpenNI -lopencv_imgcodecs -lopencv_core

PlaybackSync.o: PlaybackSync.cpp
	g++ -g -c PlaybackSync.cpp -o PlaybackSync.o -I/usr/include/ni/
