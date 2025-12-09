import networkx as nx
import matplotlib.pyplot as plt

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

def find_min_value(root_node: Node):
    """
    Знаходить найменше значення у Двійковому Дереві Пошуку (BST / AVL).
    
    У BST найменше значення завжди знаходиться у найлівішому вузлі.
    Часова складність: O(h), де h — висота дерева.
    """
    if root_node is None:
        return None 
    
    current_node = root_node
    # Рухаємося по left-вказівнику, доки не досягнемо кінця
    while current_node.left is not None:
        current_node = current_node.left
        
    return current_node.key


# --- Візуалізація ---
def add_edges_to_graph(graph, node, pos, x=0, y=0, layer=1):
    """
    Рекурсивно додає вузли та ребра до об'єкта networkx.
    """
    if node is not None:
        # Додавання поточного вузла
        graph.add_node(node.key, label=node.key)
        
        # Обчислення позиції для поточного вузла
        pos[node.key] = (x, y) 
        
        if node.left:
            # Додаємо ребро до лівого дочірнього елемента
            graph.add_edge(node.key, node.left.key)
            
            # Обчислення нової позиції (ліворуч і на рівень нижче)
            l = x - 1 / 2 ** layer
            pos[node.left.key] = (l, y - 1)
            
            # Рекурсивний виклик для лівого піддерева
            add_edges_to_graph(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
            
        if node.right:
            # Додаємо ребро до правого дочірнього елемента
            graph.add_edge(node.key, node.right.key)
            
            # Обчислення нової позиції (праворуч і на рівень нижче)
            r = x + 1 / 2 ** layer
            pos[node.right.key] = (r, y - 1)
            
            # Рекурсивний виклик для правого піддерева
            add_edges_to_graph(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

def draw_tree(tree_root):
    """
    Візуалізує BST за допомогою networkx та matplotlib.
    """
    if tree_root is None:
        return False

    tree = nx.DiGraph() # Орієнтований граф
    pos = {} # Словник для зберігання позицій вузлів

    # Заповнення графа вузлами та ребрами
    add_edges_to_graph(tree, tree_root, pos)

    # Вилучення міток та кольорів
    labels = {node: node for node in tree.nodes()}
    
    plt.figure(figsize=(10, 7))
    # Малювання вузлів та ребер
    nx.draw(tree, pos=pos, labels=labels, arrows=False, 
            node_size=2000, node_color='lightblue', font_size=12, 
            font_color='black', edge_color='gray')
            
    plt.title("Візуалізація Двійкового Дерева Пошуку (BST)")
    plt.show()
    return True


# --- Тестування ---
if __name__ == "__main__":
    
    print("--- Тест 1: Звичайне дерево ---")
    tree = BST()
    elements = [40, 20, 60, 10, 30, 50, 70]
    for el in elements:
        tree.insert(el)
        
    min_val_1 = find_min_value(tree.root)
    print(f"Найменше значення: {min_val_1}") # 10
    draw_tree(tree.root) 

    print("\n--- Тест 2: Деградоване дерево ---")
    tree_degraded = BST()
    elements_degraded = [10, 20, 30]
    for el in elements_degraded:
        tree_degraded.insert(el)
        
    min_val_2 = find_min_value(tree_degraded.root)
    print(f"Найменше значення: {min_val_2}") # 10
    draw_tree(tree_degraded.root)

    print("\n--- Тест 3: Порожнє дерево ---")
    tree_empty = BST()
    min_val_3 = find_min_value(tree_empty.root)
    
    # Об'єднуємо обробку помилки в один чистий вивід
    if min_val_3 is None:
        print("Результат: Дерево порожнє (Min value: None). Візуалізація пропущена.")
    else:
        print(f"Найменше значення: {min_val_3}")
        draw_tree(tree_empty.root)