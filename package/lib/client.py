try:
    import requests
    requests.packages.urllib3.disable_warnings()
except ImportError as e:
    print "requests not found. Please install by `pip install requests`"
    exit(1)

sslVerify = True

def disableSSL():
    """TODO: Docstring for disableSSL.
    :returns: None

    """
    global sslVerify
    sslVerify = False

def get_google():
    """TODO: Docstring for get_goole.
    :returns: status code, response

    """
    global sslVerify
    r = requests.get('https://www.google.com', verify = sslVerify)
    return r

def patch_google():
    """TODO: Docstring for patch_goole.
    :returns: status code, response

    """
    global sslVerify
    r = get_google()
    if r.status == 200:
        #status, content = patch data to google
        pass
    return r
