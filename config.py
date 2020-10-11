class Parameter:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def to_dict(self):
        return {self.key: self.value}


class Config:
    TOKEN = "1318733250:AAEJXft0OfQ-cVsoucGgyeKeBdRQunRQEGY"
    CHAT_ID = "1325598558"
    HOURS = 8

    # API endoint
    ENDPOINT = "https://api.anwb.nl/occasion-hexon-search"

    # URL query parameters
    BRAND = Parameter("vehicle.brand.keyword", "renault")
    MODEL = Parameter("vehicle.model.keyword", "clio")
    COORDINATES = Parameter("company.coordinates", "2171xv-100km")
    PRICE = Parameter("vehicle.askingPrice", "0-9500")
    FROM = Parameter("from", "2014")
    MILEAGE = Parameter("vehicle.mileageInKm", "0-90000")
    BODYSHAPE = Parameter("vehicle.bodyShape.keyword", "HATCHBACK")
    DOORS = Parameter("vehicle.numberOfDoors", "4-5")
    LIMIT = Parameter("limit", "100")
    VIEW = Parameter("viewwrapper", "grid")

    # headers
    CONNECTION = Parameter("Connection", "keep-alive")
    ACCEPT = Parameter("Accept", "application/json")
    DNT = Parameter("DNT", "1")
    CLIENT_ID = Parameter("x-anwb-client-id", "innzlrw2VjJNTsfWGaTK0C887VOO5mIJ")
    USER_AGENT = Parameter("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36")
    ORIGIN = Parameter("Origin", "https://www.anwb.nl")
    FETCH_SITE = Parameter("Sec-Fetch-Site", "same-site")
    FETCH_MODE = Parameter("Sec-Fetch-Mode", "cors")
    FETCH_DEST = Parameter("Sec-Fetch-Dest", "empty")
    REF = Parameter("Referer", "https://www.anwb.nl/")
    ACCEPT_LANGUAGE = Parameter("Accept-Language", "en-US,en;q=0.9,hr-HR;q=0.8,hr;q=0.7,nl;q=0.6,la;q=0.5")
    COOKIE = Parameter("Cookie", "optimizelyEndUserId=oeu1602049939765r0.9981325892211941; _cs_mk=0.49465314211777023_1603; _gid=GA1.2.1331447756.1602161480; SSO=TkT0b8SnLF3AddQ; AccessToken=w9c64b5635bxzndk; login-expires=1602170756513; login-name=R.%20Luijk; _ga_9ZJ9JFZNEG=GS1.1.1602169460.5.1.1602169488.0; _ga=GA1.2.1172286515.1602049940")

    def get_url_params(self):
        return {
            **self.BRAND.to_dict(),
            **self.MODEL.to_dict(),
            **self.COORDINATES.to_dict(),
            **self.PRICE.to_dict(),
            **self.FROM.to_dict(),
            **self.MILEAGE.to_dict(),
            **self.BODYSHAPE.to_dict(),
            **self.DOORS.to_dict(),
            **self.LIMIT.to_dict(),
            **self.VIEW.to_dict()
        }

    def get_headers(self):
        return {
            **self.CONNECTION.to_dict(),
            **self.ACCEPT.to_dict(),
            **self.DNT.to_dict(),
            **self.CLIENT_ID.to_dict(),
            **self.USER_AGENT.to_dict(),
            **self.ORIGIN.to_dict(),
            **self.FETCH_SITE.to_dict(),
            **self.FETCH_MODE.to_dict(),
            **self.FETCH_DEST.to_dict(),
            **self.REF.to_dict(),
            **self.ACCEPT_LANGUAGE.to_dict(),
            **self.COOKIE.to_dict()
        }
