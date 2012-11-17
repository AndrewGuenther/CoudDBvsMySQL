#!/usr/bin/env python

from couchbase.couchbaseclient import CouchbaseClient
from couchbase.rest_client import RestConnection

client = CouchbaseClient("http://ec2-50-18-23-176.us-west-1.compute.amazonaws.com:8091/pools/default", "default", "");
client.set("key1", 0, 0, "value1")
client.get("key1")
