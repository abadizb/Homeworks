import searcher
import data_load
import indexer
import WEBcrawler
import weather

weather.weather()
visit_url.visit_url()
indexer.indexer()
searcher.searcher()
data_load.traverser()
d = indexer.indexer("raw_data.pickle","shelve")
searcher.search(d)
