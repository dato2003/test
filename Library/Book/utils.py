import json
import redis


dc = redis.StrictRedis(port=6379,bd=0)


class redis:
    def set (cache_kay,input_data):
        dumped_data = json.dumps(input_data)
        dc.set(cache_kay,dumped_data,15)
        return True


    def get(cache_kay):
        cache_data = dc.get(cache_kay)
        if not cache_data:
            return  False
        cache_data_json = json.loads(cache_data)
        return cache_data_json