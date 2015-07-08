# Example: python query_to_bel.py "ARAF BRAF RAF1" RAF_neighborhood.bel

import ndexClient as nc
import ndexUtil as util
import sys

def query_to_belscript(proteins,outfile=None):
    myNdex = nc.Ndex("http://ndexbio.org")
    #myNet = myNdex.getNeighborhood('1ada3330-45cc-11e4-a9e5-000c29873918', proteins)
    #myNet = myNdex.getNeighborhood('7e57f74d-a39b-11e4-bda0-000c29202374', proteins)
    myNet = myNdex.getNeighborhood('9ea3c170-01ad-11e5-ac0f-000c29cb28fb', proteins)
    
    myWrapper = util.NetworkWrapper(myNet,removeNamespace=['MGI','RGD','PFM','NCM','PFR','NCR'])
    bel_script = myWrapper.writeBELScript(outfile)
    return bel_script

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: python query_to_bel.py "protein1 protein2 ..." outfile'
        sys.exit()
    
    proteins = sys.argv[1]
    outfile = sys.argv[2]
    query_to_belscript(proteins,outfile)
    
