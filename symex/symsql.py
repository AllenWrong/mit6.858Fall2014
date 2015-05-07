## This module wraps SQLalchemy's methods to be friendly to
## symbolic / concolic execution.

import fuzzy
import sqlalchemy.orm

oldget = sqlalchemy.orm.query.Query.get
def newget(query, primary_key):
  ## Exercise 5: your code here.
  ##
  ## Find the object with the primary key "primary_key" in SQLalchemy
  ## query object "query", and do so in a symbolic-friendly way.
  ##
  ## Hint: given a SQLalchemy row object r, you can find the name of
  ## its primary key using r.__table__.primary_key.columns.keys()[0]
  print "QUERY:",query
  allRecords = query.all()
  print "RECORDS:",allRecords
  for record in allRecords:
    primary_key_name = record.__table__.primary_key.columns.keys()[0]
    if primary_key == getattr(record, primary_key_name):
      return record
  return None

sqlalchemy.orm.query.Query.get = newget
