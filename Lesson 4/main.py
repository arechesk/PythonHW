from website_alive.check_response import response


if __name__=='__main__':
    url = input("URL:")
    if response(url):
        print(f"site {url} is available")
    else:
        print(f"site {url} not available")