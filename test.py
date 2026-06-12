from lightrail_locations import LIGHTRAIL_STATIONS
# from api import get_places_from_stops
from pprint import pprint
from session import genereate_search_results, get_search_results

genereate_search_results()
pprint(get_search_results())
