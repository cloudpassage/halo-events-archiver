import cloudpassage
from utility import Utility


class GetEvents(object):
    def __init__(self, key, secret, api_hostname, batch_size, target_date):
        self.ua = Utility.build_ua("")
        self.session = cloudpassage.HaloSession(key, secret,
                                                api_host=api_hostname,
                                                integration_string=self.ua)
        self.target_date = target_date
        self.batch_size = batch_size
        self.streamer = cloudpassage.TimeSeries(self.session, self.target_date,
                                                "/v1/events", "events")
        print("Event retrieval initialized for date %s") % self.target_date

    def __iter__(self):
        batch = []
        for event in self.streamer:
            if event["created_at"].startswith(self.target_date):
                if len(batch) >= self.batch_size:
                    yield list(batch)
                    batch = []
                else:
                    batch.append(event)
            else:
                yield list(batch)
                print("No more events for target day!")
                raise StopIteration
