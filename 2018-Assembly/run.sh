 if [ ! -d "build" ]
    then
        mkdir build
    fi

nasm -i $(pwd)/inc/ -i $(pwd)/input/ -f elf64 $1.asm -o build/$1.o \
&& ld -s -o build/$1 build/$1.o \
&& ./build/$1