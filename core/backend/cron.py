from django_cron import CronJobBase, Schedule
import random
import requests
from .signals import send_sms


class MyCronJob(CronJobBase):
    # RUN_EVERY_MINS = 1  # every 1 minute
    RETRY_AFTER_FAILURE_MINS = 1  # how often to retry if the job failed
    RUN_AT_TIMES = ['6:30', '12:00', '19:00']

    schedule = Schedule(run_at_times=RUN_AT_TIMES, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)  # noqa
    code = 'backend.cron.MyCronJob'    # a unique code

    def do(self):
        # QUOTES OF THE DAY
        quote_id = random.randint(1, 1643)
        QUOTES_URL = 'https://type.fit/api/quotes'
        response = requests.get(QUOTES_URL)
        quotes = response.json()
        recipients = ['0558366133', '0599310774', '0558370022', '0557013564',
                      '0545757673', '0278904936', '0504704634', '0541718985',
                      '0553249665', '0552145563', '0276490600', '0543358113',
                      '0543821458', '0596265255', '0245907066', '0554009071']
        title = "devprincek - Daily Motivation"
        message = quotes[quote_id]['text']
        author = quotes[quote_id]['author']
        content = title + "\n\n" + message + "\n\n" + "---" + author
        send_sms('devprincek', content, recipients)
        # print(quotes[quote_id]['text'])
        # print(quotes[quote_id]['author'])

        # WORDS OF THE DAY
        # WORDS_URL = "https://wordsapiv1.p.rapidapi.com/words/"
        # querystring = {"random": "true"}
        # headers = {
        #     "X-RapidAPI-Key": "95c04fee08mshaa3cdb94c1e4c6ap18948cjsnc2fe7e8e95c8",
        #     "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
        # }
        # response = requests.get(WORDS_URL, headers=headers, params=querystring)
        # print(response.text)
