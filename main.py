import subprocess
import json

EndP = {
    "posts": "https://jsonplaceholder.typicode.com/posts",
}

def test(nazwa, url):
    try:
        wynik = subprocess.run(
            ['curl', '-s', '-w', '%{http_code}', url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        odp = wynik.stdout.decode('utf-8')
        http_code = odp[-3:]
        json_body = odp[:-3]

        try:
            data = json.loads(json_body)
        except json.JSONDecodeError:
            data = None

        if http_code == "200":
            if data:
                if all(key in data[0] for key in ["id", "userId", "title"]):
                    print(f"Test {nazwa}: PASSED")
                else:
                    print(f"Test {nazwa}: FAILED - Missing keys in JSON response")
            else:
                print(f"Test {nazwa}: FAILED - Response is not valid JSON")
        else:
            print(f"Test {nazwa}: FAILED - HTTP Status {http_code}")
    except Exception as e:
        print(f"Test {nazwa}: FAILED - Error occurred: {e}")


for nazwa, endpoint in EndP.items():
    test(nazwa, endpoint)
