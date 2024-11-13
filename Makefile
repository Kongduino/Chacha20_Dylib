.POSIX:
TARGET = chacha20_poly1305
CC = gcc
CFLAGS = -Ofast -g -c

# The list of object files.
OBJS =  chacha-portable.o helper.o portable8439.o

# the list of files to clean
TOCLEAN = chacha20_poly1305.dylib $(OBJS)

RM ?= rm -f

all: $(TARGET)
clean:
	$(RM) $(TOCLEAN)

chacha20_poly1305: $(OBJS)
	$(CC) $(CFLAGS) *.c
	$(CC) -dynamiclib *.o -o $(TARGET).dylib
	rm *.o

install:
	cp $(TARGET).dylib /usr/local/lib/