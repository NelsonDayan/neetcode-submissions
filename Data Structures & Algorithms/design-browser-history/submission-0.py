class HistoryNode:
    def __init__(self, val = "", next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        temp_node = HistoryNode(val=homepage)
        self.cur_page = temp_node

    def visit(self, url: str) -> None:
        new_node = HistoryNode(val=url,prev=self.cur_page)
        self.cur_page.next = new_node
        self.cur_page = new_node

    def back(self, steps: int) -> str:
        temp_node = self.cur_page
        for i in range(0,steps):
            if temp_node.prev:
                temp_node = temp_node.prev
            else:
                break
        self.cur_page = temp_node
        return temp_node.val

    def forward(self, steps: int) -> str:
        temp_node = self.cur_page
        for i in range(0,steps):
            if temp_node.next:
                temp_node = temp_node.next
            else:
                break
        self.cur_page = temp_node
        return temp_node.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)