import requests
from datetime import datetime, timedelta
from telegram.ext import Updater
from config import Config

conf = Config()


def call_api():
    # import json
    # return json.load(open("response.json"))
    params = conf.get_url_params()
    headers = conf.get_headers()
    r = requests.get(conf.ENDPOINT, params=params, headers=headers)
    return r.json()


def get_latest(results):
    ts = datetime.now() - timedelta(hours=conf.HOURS)
    filtered = [
        doc for doc in results
        if datetime.fromtimestamp(doc.get("meta").get("createdAt") / 1000.0) > ts
    ]
    return sorted(filtered, key=lambda k: k.get("meta").get("createdAt"), reverse=True)


def get_cover_image(doc):
    media = [
        img for img in doc.get("vehicle").get("media")
        if "https" in img.get("value")
    ]
    if len(media) > 0:
        return media[0].get("value").replace("\n", "")
    else:
        return None


def format_mileage(x):
    x = str(x)
    return "{},{}".format(x[:-3],  x[-3:])


def format_price(x):
    x = str(x)
    return "€{},{}".format(x[:-3], x[-3:])


def format_location(x):
    return x.lower().capitalize()


def callback_timer(context):
    response = call_api()
    results = get_latest(response.get("results"))
    if results is not None and len(results) > 0:
        context.bot.send_message(chat_id=conf.CHAT_ID, text="Nieuwe waggies! Zie hier de {} nieuwste:".format(len(results)), parse_mode="MARKDOWN", disable_web_page_preview=True)
        for doc in results:
            city = format_location(doc.get("company").get("city"))
            province = format_location(doc.get("company").get("province"))
            price = format_price(doc.get("vehicle").get("askingPrice"))
            registration = doc.get("vehicle").get("dateFirstRegistration")
            mileage = format_mileage(doc.get("vehicle").get("mileageInKm"))
            timestamp_posted = (datetime.fromtimestamp(doc.get("meta").get("createdAt") / 1000.0)).strftime("%d %b %Y, %H:%M")
            id = doc.get("id")
            lat = doc.get("company").get("coordinates").get("lat")
            lon = doc.get("company").get("coordinates").get("lon")
            location = "https://maps.google.com/?q={},{}".format(lat, lon)
            url = "https://www.anwb.nl/auto/kopen/detail/merk=renault/model=clio/overzicht/{}".format(id)
            img_url = get_cover_image(doc)

            msg = "Km: {}\nPrijs: {}\nGeregistreerd: {}\nPlaats: {} ({})\nGeplaatst op: {}\nLocatie dealer: [Google Maps]({})\nMeer info: [ANWB]({})".format(
                mileage, price, registration, city, province, timestamp_posted, location, url
            )
            if img_url is not None:
                context.bot.send_photo(chat_id=conf.CHAT_ID, photo=img_url)

            context.bot.send_message(chat_id=conf.CHAT_ID, text=msg, parse_mode="MARKDOWN", disable_web_page_preview=True)
    else:
        context.bot.send_message(chat_id=conf.CHAT_ID, text="Geen nieuwe waggies :(", disable_web_page_preview=True)


def main():
    # create updater
    updater = Updater(conf.TOKEN)
    job_queue = updater.job_queue

    # force a first call
    job_queue.run_once(callback_timer, when=0)

    # create job and start program
    job_queue.run_repeating(callback_timer, interval=timedelta(hours=conf.HOURS))
    updater.start_polling()


if __name__ == "__main__":
    main()
