class Node:
    """Вузол для Двійкового Дерева Пошуку (BST) або AVL-дерева."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    """Проста реалізація Двійкового Дерева Пошуку (BST)."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Вставляє новий ключ у дерево."""
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        """Рекурсивна допоміжна функція для вставки."""
        if node is None:
            return Node(key)
        
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        
        return node

def find_sum_values(root_node: Node) -> int:
    """
    Знаходить суму всіх значень у двійковому дереві пошуку (BST/AVL) 
    за допомогою рекурсивного обходу.
    
    Часова складність: O(n), де n — кількість вузлів, оскільки відвідується кожен вузол.
    """
    # Базовий випадок: якщо вузол порожній, повертаємо 0
    if root_node is None:
        return 0
    
    # Рекурсивний випадок: сума = поточне значення + сума лівого піддерева + сума правого піддерева
    return root_node.key + find_sum_values(root_node.left) + find_sum_values(root_node.right)


# --- Тестування ---
if __name__ == "__main__":
    
    print("--- Тест 1: Звичайне дерево ---")
    tree = BST()
    elements = [40, 20, 60, 10, 30, 50, 70]
    for el in elements:
        tree.insert(el)
    
    sum_val_1 = find_sum_values(tree.root)
    print(f"Сума всіх значень: {sum_val_1}") # 280


    print("\n--- Тест 2: Деградоване дерево ---")
    tree_degraded = BST()
    elements_degraded = [10, 20, 30]
    for el in elements_degraded:
        tree_degraded.insert(el)
        
    sum_val_2 = find_sum_values(tree_degraded.root)
    print(f"Сума всіх значень: {sum_val_2}") # 60


    print("\n--- Тест 3: Порожнє дерево ---")
    tree_empty = BST()
    
    sum_val_3 = find_sum_values(tree_empty.root)
    print(f"Сума всіх значень: {sum_val_3}")