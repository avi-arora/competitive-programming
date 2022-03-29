import random
class Codec:

    urlEncode = {}
    chars = "abcdefghijklmnopqrstuvwxyz"
    
    def __getEncoding(self, str):
        return ''.join([random.choices(self.chars) for _ in range(6)])

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        encoding = ""
        while True:
            encoding = self.__getEncoding(longUrl)
            if encoding not in self.urlEncode:
                self.urlEncode[encoding] = longUrl
                break
        return "http://tinyurl.com/ " + encoding
        


        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urlEncode[shortUrl.split('/')[-1]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))