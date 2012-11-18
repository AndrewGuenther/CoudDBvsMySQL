#!/usr/bin/env python

from couchbase.client import Couchbase
from couchbase.rest_client import RestConnection

client = Couchbase("ip-10-168-7-254.us-west-1.compute.internal:8091", "genealogy", "")

bucket = client["genealogy"]

bucket.set("key1", 0, 0, '{"value1": 5}')
print bucket.get("key1")
