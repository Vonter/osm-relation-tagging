# osm-relation-tagging
Python scripts to aid in tagging wikidata tags on OpenStreetMap

**Avoid using such automation scripts if you are not sure about what you are doing or without [careful planning and consultation with the local community](https://wiki.openstreetmap.org/wiki/Osmapi)**

### relationmodify.py
Given a list of relation IDs in `tmplist`, searches for Wikipedia articles sharing the same name as the corresponding relation.
Finds the corresponding Wikidata QID.
Saves the modified relation having a Wikidata and Wikipedia tag.
