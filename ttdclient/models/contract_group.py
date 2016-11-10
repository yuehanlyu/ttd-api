import json

from ttdclient.models.base import Base


class ContractGroup(Base):

    obj_name = "contractgroup"

    def find_by_advertiser(self, partnerId, advertiserId):
        payload = { "AdvertiserId": advertiserId,
                    "PageStartIndex": 0,
                    "PageSize": None }
        method = "POST"
        url = '{0}/{1}'.format(self.get_url(), 'query/advertiser/available')
        
        response = self._execute(method, url, json.dumps(payload))
        return self._get_response_objects(response)

    def get_avails(self, contractId, startDate, endDate):
        payload = { "ContractGroupId": contractId,
                    "ReportStartDateUtc": startDate,
                    "ReportEndDateUtc": endDate,
                    "PageStartIndex": 0,
                    "PageSize": None }

        method = "POST"
        url = '{0}/{1}'.format(self.get_url(), 'report/impressions/available')
        
        response = self._execute(method, url, json.dumps(payload))
        return self._get_response_object(response)
        
