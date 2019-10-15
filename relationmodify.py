from osmapi import OsmApi
import wptools
import time
import json
import csv
import codecs
import wikipedia
import configparser
import threading
import time
import os

def main():

	global myOSMAPI 
        config = configparser.ConfigParser()
        config.read('config.ini')
        myOSMAPI = OsmApi(username=config.get('OSM','OPENSTREETMAP_USERNAME'), password=config.get('OSM','OPENSTREETMAP_PASSWORD'))
        myOSMAPI.ChangesetCreate({u"comment": u"district wikidata and wikipedia tags"})

        i = 0

	#reads list of relations that need to be modified
	txt = open("tmplist", 'r')

	for place in txt.readlines():

            try:

                i+=1
		
		#get relation details		

		relJSON = myOSMAPI.RelationGet(place)
		name = relJSON["tag"]["name"]
	        print name
                
		#get wikipedia article name

		qid = open("qidandname", 'r')
                sch = wikipedia.search(name + '_district',  results=1)
                article = sch[0]
                print article

		#get wikidata qid

                n = wptools.page(sch[0].encode('ascii','ignore'), silent = True)
                qid = n.get_wikidata().wikibase
                print qid

		#make changes in osm

                newrelJSON = relJSON
                #newrelJSON["tag"]["wikidata"] = qid
                newrelJSON["tag"]["wikipedia"] = "en:" + article

                if(i >= 10):
                    myOSMAPI.ChangesetClose()
                    break

            except:
                print place + " failed"

if __name__ == "__main__":
	main()
