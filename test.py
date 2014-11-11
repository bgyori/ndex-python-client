# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 22:34:42 2014

@author: dexter pratt
"""
import ndex_client as nc
import ndex_util as util

# Establish an object to communicate with the NDEx Test Server 
# Anonymous connection, can perform only Read operations
myNdex = nc.Ndex("http://test.ndexbio.org")
# myNet = myNdex.getNetworkByEdges("63177354-433b-11e4-9369-90b11c72aefa", 0 , 25)
# 1ada3330-45cc-11e4-a9e5-000c29873918
#myNet = myNdex.get_neighborhood('1ada3330-45cc-11e4-a9e5-000c29873918', 'BRAF RAF1 KRAS NRAS HRAS MAPK1 MAPK2 MAP2K1 MAP2K2')
# BEL Large Corpus on NDEx TEST server
myNet = myNdex.get_neighborhood('1ada3330-45cc-11e4-a9e5-000c29873918', 'BRAF RAF1 KRAS NRAS HRAS MAPK1 MAPK2 MAP2K1 MAP2K2')

# The utility wrapper is a work in progress to provide useful manipulations of networks
myWrapper = util.NetworkWrapper(myNet)
myWrapper.write_summary("RAS-RAF-MEK-MAPK.txt")