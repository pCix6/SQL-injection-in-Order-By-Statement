# SQL-injection-in-Order-Statement

In this repository you can find a script used in a CTF challenge to read a flag through a SQL injection via a parameter in the URL.  The script is made in python and implements threads and binary search, improving significantly its performance if done without threads and using linear search.

# Important Notes

This script is based on the fact that we have a page where we can order items with the `order` parameter which is vulnerable to SQLi and has been determined to be part of an ORDER BY clause. In addition it is also assumed that the flag we read is in a table named `flag` and a column named `flag` as well.

Anyway, it remains as a reference so that it can be adapted to each case assuming that something of interest has been found. 

# Usage
Syntax:

`./getFlag.py <IP> <index_firstChar> <index_lastChar>`

Example:

`./getFlag.py 10.10.10.10 1 10 `

This example will retrieve the first 10 chars of the flag.
However, if you do not know the length of the flag, you can adjust the values as needed.
