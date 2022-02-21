import libs.wrapper as myWrap

HOST = '0.0.0.0'
PORT = 5060
MY_CODES = {
        480 : "Temporarily Unavailable",
        486 : "Ta neotravuj teraz"
}

if __name__ == "__main__":
    server = myWrap.Wrapper(HOST,PORT,MY_CODES)
    server.start()
