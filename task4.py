from typing import List

class Comment:
    """
    Представляє окремий коментар в ієрархічній системі.
    """
    DELETED_MESSAGE = "Цей коментар було видалено."

    def __init__(self, text: str, author: str):
        self.text = text
        self.author = author
        self.replies: List['Comment'] = []
        self.is_deleted = False

    def add_reply(self, reply: 'Comment'):
        """Додає нову відповідь до списку відповідей цього коментаря."""
        self.replies.append(reply)

    def remove_reply(self):
        """
        Видаляє коментар: змінює текст на стандартне повідомлення 
        та встановлює прапорець is_deleted в True.
        """
        self.is_deleted = True
        self.text = self.DELETED_MESSAGE
        # Примітка: Ми не видаляємо відповіді replies фізично, 
        # щоб зберегти ієрархічну структуру для відповідей на видалений коментар.

    def display(self, level=0):
        """
        Рекурсивно виводить коментар та всі його відповіді, 
        використовуючи відступи для відображення ієрархічної структури.
        """
        indent = "    " * level
        
        if self.is_deleted:
            # Якщо коментар видалено, виводимо лише стандартне повідомлення
            print(f"{indent}{self.DELETED_MESSAGE}")
        else:
            # Виводимо автора та текст коментаря
            print(f"{indent}{self.author}: {self.text}")
        
        # Рекурсивний виклик для всіх відповідей
        for reply in self.replies:
            # Збільшуємо рівень відступу для дочірніх елементів
            reply.display(level + 1)
            
# --- Тестування ---
if __name__ == "__main__":
    # 1. Створення кореневого коментаря та двох відповідей
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    # 2. Відповідь на відповідь (третій рівень)
    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    # 3. Видалення проміжного коментаря
    reply1.remove_reply()

    print("--- Ієрархічна Система Коментарів ---")
    root_comment.display()