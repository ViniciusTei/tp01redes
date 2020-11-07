#Nome do programa
TARGET = tp01

#compilador
CC = gcc

OBJS = main.o

all: $(OBJS)
	$(CC) obj/*.o -o bin/$(TARGET)

main.o: src/main.c
	$(CC) -c src/main.c -o obj/main.o

run:
	bin/$(TARGET)

clean:
	rm obj/*.o
	rm bin/*