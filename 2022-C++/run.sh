if [ ! -d "build" ]
then
    mkdir build
fi

gcc $1.cpp -lstdc++ -o ./build/$1 \
&& ./build/$1