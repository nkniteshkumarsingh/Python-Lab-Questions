class Service:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def get_service(self):
        return f"{self.host}:{self.port}"

    def get_data(self):
        return ""


class Web(Service):
    def __init__(self, protocol="http", host="0.0.0.0", port=80):
        super().__init__(host, port)
        self.protocol = protocol

    def get_service(self):
        return f"{self.protocol}://{self.host}:{self.port}"

    def get_data(self):
        return "<HTML> ... </HTML>"


class Mail(Service):
    def __init__(self, method="IMAP", host="0.0.0.0", port=143):
        super().__init__(host, port)
        self.method = method

    def get_data(self):
        return """
            To: programming@example.com
            From: object@example.com
            Content Type: plain/text
            \n
            Hello, World!
        """


if __name__ == "__main__":
    s = Service("0.0.0.0", 8888)
    print(f"Service: {s.get_service()}\n")

    http = Web()
    print(f"Web Service: {http.get_service()}")
    print(f"Data: {http.get_data()}\n")

    mail = Mail(method="POP3")
    print(f"Mail Service: {mail.get_service()}")
    print(f"Data: {mail.get_data()}\n")
