from decors import speedtest

@speedtest(interations=10)
def search(url):
    import requests

    s = requests.get(url)
    return s.text





web = search('https://edition.cnn.com/')
print(web)



