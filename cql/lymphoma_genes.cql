MATCH (c:Cell {id:"U937"})-[r1]-(s:Signature)-[r2]-(d:Drug)
MATCH (c:Cell {id:"U937"})-[r1]-(s:Signature)-[r3]-(g:Gene)
RETURN (c)--(s), (s)--(d), (s)--(g)
	;
