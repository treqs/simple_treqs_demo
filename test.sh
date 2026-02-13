#!/bin/bash

SIZE=${SIZE:-10000000}
CHUNK=${CHUNK:-100}
CMD=${CMD:-"roar run"}

echo "SIZE = " $SIZE
echo "CHUNK = " $CHUNK
echo "CMD = " $CMD

# 1
$CMD python src/produce.py --seed 100 --n $SIZE --chunk $CHUNK data/1.bin
$CMD python src/produce.py --seed 101 --n $SIZE --chunk $CHUNK data/2.bin
$CMD python src/produce.py --seed 102 --n $SIZE --chunk $CHUNK data/3.bin
$CMD python src/produce.py --seed 103 --n $SIZE --chunk $CHUNK data/4.bin

# 2
$CMD python src/binary_op.py --add --chunk $CHUNK data/1.bin data/2.bin data/5.bin
$CMD python src/binary_op.py --add --chunk $CHUNK data/3.bin data/4.bin data/6.bin

# 3
$CMD python src/binary_op.py --mul --chunk $CHUNK data/5.bin data/6.bin data/7.bin
