Couchbase vs. MySQL
===================

This project presents multiple experiments for comparing performance of
Couchbase and MySQL under different kinds of workloads.

Data Set
--------
The experiments all work with genealogical data because of its hierarchical nature.
This opened the doors for interesting data retrieval workloads involving lots of `JOIN`s for `SQL` and multiple `GET`s for Couchbase.
The data is randomly generated.

Code Organization
-----------------
The code is organized as follows.
The `db/` directory contains database specific code related to connecting and querying the Couchbase and MySQL databases.
The `util/` directory contains code for stats gathering as well as random person generation.
Finally, the root directory contains the experiments (`exp_*.py`) and helper script for running them in parallel.

Experimental Setup
------------------
All of the experiments extend `Experiment` found in `experiment.py`.
The base class takes care of all command line parsing and DB setup so the derived classes can focus on the experiment.
It also contains lots of helper functions to perform operations such as inserting and retrieving a number of people.

An experiment is run by supplying the database to run the experiment on as well as a range of valid `personid`'s.
A range is necessary so multiple tests can be run in parallel without any conflicts.
The `runmulti.py` script automatically supplies the correct arguments to the experiment scripts based on the supplied number of people already inserted in the database.
