class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = words
        self.ends = [word[-1] for word in words]
        self.stream = ''

    def query(self, letter: str) -> bool:
        self.stream += letter
        if letter in self.ends:
            for word in self.words:
                if self.stream.endswith(word):
                    return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)