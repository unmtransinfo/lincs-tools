#!/bin/bash
#
set -e
#
DBNAME="lincs"
DBSCHEMA="public"
#
#
tables=`psql -q -d $DBNAME -tAc "SELECT table_name FROM information_schema.tables WHERE table_schema='$DBSCHEMA'"`
#
for t in $tables ; do
	echo $t
	psql -P pager=off -q -d $DBNAME -c "SELECT column_name,data_type FROM information_schema.columns WHERE table_schema='$DBSCHEMA' AND table_name = '$t'"
	psql -q -d $DBNAME -c "SELECT count(*) AS \"${t}_count\" FROM $DBSCHEMA.$t"
done
#
