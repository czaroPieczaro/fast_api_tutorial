import time
import requests

def main():
    request_count = 10
    url = 'https://httpbin.org/get'
    session = requests.Session()
    for i in range(request_count):
        print(f'Makin request {i+1}')
        resp = requests.get(url)
        if resp.status_code == 200:
            pass


start = time.time()
main()
end = time.time()
print(f'It took {end - start} secs')
