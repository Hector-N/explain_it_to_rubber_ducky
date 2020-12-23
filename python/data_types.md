# Q: Draw a diagram that represents built-in data types in Python

## A:
The idea of categorizing data may be expressed with following diagrams

                                     DATA TYPE
                            /                            \
                COMPOUND                                           SCALAR
                /                    \                             * int, float
        MUTABLE                          IMMUTABLE
        (may contain)                    (may contain)
        /       |       \                   /       \
    ANY     HASHES      HASH: ANY      HASHES          ANY
    * list  * set       * dict         * frozen set    * str, tuple, range


                                        DATA TYPE
                            /               |                   \
                SEQUENTIAL              NOT SEQUENTIAL                MAPPING
        (list, str, tuple, range)   (set, frozenset, int, float)      (dict)
