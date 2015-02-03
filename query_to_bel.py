# Example: python query_to_bel.py "ARAF BRAF RAF1" RAF_neighborhood.bel

import ndexClient as nc
import ndexUtil as util
import sys

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'Usage: python query_to_bel.py "protein1 protein2 ..." outfile'
        sys.exit()
    
    proteins = sys.argv[1]
    outfile = sys.argv[2]
    myNdex = nc.Ndex("http://test.ndexbio.org")
    myNet = myNdex.getNeighborhood('1ada3330-45cc-11e4-a9e5-000c29873918', proteins)
    myWrapper = util.NetworkWrapper(myNet,removeNamespace=['MGI','RGD','PFM','NCM','PFR','NCR'])
    myWrapper.writeBELScript(outfile)
