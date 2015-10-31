# CuckooMap
Python implementation of a [Cuckoo HashMap](https://en.wikipedia.org/wiki/Cuckoo_hashing)

Some notes:

* Sometimes, using cuckoo hashing, the set() function will turn into an infinite loop (as explained by the Wikipedia article).
  In order to resolve this, I chose to define a function that will detect if there are more than 2000 knockouts.
  Once this limit has reached, I will reject the setter. Rejection does not affect placements of other elements.
* This is a fix-sized implementation of the hashmap. I chose to initialize it with 2x the number of buckets
  for reduced hash-collisions.
* The load factor returns (float) current_size / max_size

