 if [ ! -d "build" ]
    then
        mkdir build
    fi

nasm -i $(pwd)/src/ -i $(pwd)/input/ -f elf64 src/$1.asm -o build/$1.o \
&& ld -s -o build/$1 build/$1.o \
&& ./build/$1