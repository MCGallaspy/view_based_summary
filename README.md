What is this?
-------------

A proof-of-concept of view-based summaries, including caching.
 
Use python2.7 and `pip install -r requirements.txt`. Then run the tests.
 
Where do I start?
-----------------
Look at the views. You'll find:
* A SummaryView
* A cached helper function
* A post-save signal handler that invalidates the cache

In reality, we'll probably want to use a different caching function, one which can be invalidated on a per-parameter
basis. For instance, we may wish to invalidate the cache only for the value `user=3`. Our only limit for cache
invalidation is our imagination.

`lru_cache` is in-memory, but other possibilities are disk- and db-backed caching.

One potential issue is with syncing -- if summary logs are very expensive to compute, we may wish to sync their
results between machines, by stashing the result in the db. Using view-based caches doesn't preclude that.