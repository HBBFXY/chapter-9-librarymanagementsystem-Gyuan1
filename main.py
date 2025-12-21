class Book:
    """书籍类，包含书名、作者、ISBN等属性，以及可借状态"""
    def __init__(self, title, author, isbn):
        self.title = title  # 书名
        self.author = author  # 作者
        self.isbn = isbn  # ISBN编号
        self.is_borrowed = False  # 书籍是否被借出，默认未借出

    def __str__(self):
        status = "已借出" if self.is_borrowed else "可借阅"
        return f"《{self.title}》- {self.author} | ISBN: {self.isbn} | 状态: {status}"


class User:
    """用户类，包含姓名、借书卡号，以及借阅书籍列表"""
    def __init__(self, name, card_id):
        self.name = name  # 姓名
        self.card_id = card_id  # 借书卡号
        self.borrowed_books = []  # 已借书籍列表

    def borrow_book(self, book):
        """借书功能：检查书籍是否可借，可借则加入借阅列表并更新书籍状态"""
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} 成功借阅《{book.title}》")
        else:
            print(f"抱歉，《{book.title}》已被借出，无法借阅")

    def return_book(self, book):
        """还书功能：检查是否为已借书籍，是则移除并更新书籍状态"""
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} 成功归还《{book.title}》")
        else:
            print(f"{self.name} 未借阅《{book.title}》，无法归还")

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        borrowed_str = ", ".join(borrowed_titles) if borrowed_titles else "无"
        return f"用户：{self.name} | 借书卡号：{self.card_id} | 已借书籍：{borrowed_str}"


# 测试示例
if __name__ == "__main__":
    # 创建书籍实例
    book1 = Book("Python编程：从入门到实践", "埃里克·马瑟斯", "9787115428028")
    book2 = Book("数据结构与算法分析", "马克·艾伦·维斯", "9787115546920")

    # 创建用户实例
    user1 = User("张三", "C001")
    user2 = User("李四", "C002")

    # 测试借书、还书功能
    print("=== 初始书籍状态 ===")
    print(book1)
    print(book2)

    print("\n=== 张三借阅书籍 ===")
    user1.borrow_book(book1)
    print(book1)

    print("\n=== 李四尝试借阅同一本书 ===")
    user2.borrow_book(book1)

    print("\n=== 张三归还书籍 ===")
    user1.return_book(book1)
    print(book1)

    print("\n=== 用户信息展示 ===")
    print(user1)
    print(user2)
# 在这里编写代码
