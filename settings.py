import config

SEARCH_KEY = config.SEARCH_KEY
SEARCH_ID = config.SEARCH_ID
COUNTRY = "IN"

SEARCH_URL = "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&num=10&gl=" + COUNTRY
RESULT_COUNT = 20