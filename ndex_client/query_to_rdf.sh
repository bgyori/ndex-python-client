# Example: query_to_rdf.sh "ARAF BRAF RAF1" RAF_neighborhood
#     produces RAF_neighborhood.bel and RAF_neighborhood.rdf
# Requires bel.rb

# Change line below to set path to bel.rb
belrbdir="../bel.rb"

if [ ! -f "$belrbdir/bin/bel2rdf" ]
then 
    echo "Could not find $belrbdir/bin/bel2rdf. Set belrbdir in $0 to correct path."
    exit 1
fi

if [ "$#" -ne 2 ]
then
    echo "Usage: $0 \"protein1 protein2 ...\" outfile" >&2
    exit 1
fi

proteins=$1
file=$2
belfile="$file.bel"
rdffile="$file.rdf"

# Run NDEx query and print BEL script
python query_to_bel.py "$proteins" $belfile

# Attach some properties to the BEL script related to the query
properties="#Properties section\nSET DOCUMENT Name = \"NDEx query result in BEL script\"\nSET DOCUMENT Description = \"Query with ndex-python-client, one step neighborhood of $proteins\""
bel_statements=$(cat $belfile)
echo -en "$properties\n$bel_statements" > $belfile

# Use bel2rdf to convert to RDF file
$belrbdir/bin/bel2rdf -b $belfile > $rdffile
# Replace invalid hyphens in RDF file
sed '/_:\([^ ]\+\)/{s/-//g;}' < $rdffile > "$file.tmp"
mv "$file.tmp" $rdffile
