from datetime import datetime


class BenchmarkMiddleware(object):
    def process_request(self, request):
        request._request_time = datetime.now()

    def process_template_response(self, request, response):
        response_time = datetime.now() - request._request_time
        response.context_data['response_time'] = response_time
        return response
