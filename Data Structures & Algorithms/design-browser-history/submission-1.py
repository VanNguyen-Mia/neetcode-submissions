class BrowserHistory:

# Initializes the object with the homepage of the browser.
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = 0
        self.n = 1

# Visits url from the current page. It clears up all the forward history.
    def visit(self, url: str) -> None:
        self.cur += 1
        if self.cur == len(self.history):
            self.history.append(url)
            self.n += 1
        else:
            self.history[self.cur] = url
            self.n = self.cur + 1

# Move steps back in history. 
# If you can only return x steps in the history and steps > x, 
# you will return only x steps. 
# Return the current url after moving back in history at most steps.
    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]

# Move steps forward in history. 
# If you can only forward x steps in the history and steps > x, 
# you will forward only x steps. 
# Return the current url after forwarding in history at most steps.
  
    def forward(self, steps: int) -> str:
        self.cur = min(self.n - 1, self.cur + steps)
        return self.history[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)