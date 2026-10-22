"""
Модуль тестирования функций генерации бинарного дерева из модуля gen_bin_tree.
"""

import unittest
from gen_bin_tree import (
    gen_bin_tree,
    gen_bin_tree_dataclass,
    gen_bin_tree_defaultdict,
    gen_bin_tree_namedtuple,
    gen_bin_tree_userdict,
)


class TestGenBinTree(unittest.TestCase):
    """Набор модульных тестов для проверки генерации бинарного дерева."""

    def test_default_parameters(self) -> None:
        """Проверяет построение дерева с параметрами по умолчанию (Вариант 1)."""
        tree = gen_bin_tree(height=3)
        self.assertEqual(tree["value"], 1)
        self.assertEqual(tree["left"]["value"], 2)
        self.assertEqual(tree["right"]["value"], 4)
        self.assertEqual(tree["left"]["left"]["value"], 4)
        self.assertEqual(tree["left"]["right"]["value"], 5)
        self.assertEqual(tree["right"]["left"]["value"], 8)
        self.assertEqual(tree["right"]["right"]["value"], 7)
        self.assertIsNone(tree["left"]["left"]["left"])

    def test_custom_parameters(self) -> None:
        """Проверяет передачу пользовательских параметров (на примере Варианта 3)."""
        tree = gen_bin_tree(
            root=3,
            height=2,
            left_leaf=lambda x: x + 2,
            right_leaf=lambda x: x * 3,
        )
        self.assertEqual(tree["value"], 3)
        self.assertEqual(tree["left"]["value"], 5)
        self.assertEqual(tree["right"]["value"], 9)
        self.assertIsNone(tree["left"]["left"])

    def test_edge_cases_height(self) -> None:
        """Проверяет граничные случаи высоты (0, отрицательная, 1)."""
        self.assertEqual(gen_bin_tree(height=0), {})
        self.assertEqual(gen_bin_tree(height=-3), {})

        single = gen_bin_tree(height=1, root=42)
        self.assertEqual(single, {"value": 42, "left": None, "right": None})

    def test_alternative_containers(self) -> None:
        """Проверяет корректность работы альтернативных контейнеров."""
        # 1. namedtuple
        nt_tree = gen_bin_tree_namedtuple(root=1, height=2)
        self.assertIsNotNone(nt_tree)
        self.assertEqual(nt_tree.value, 1)
        self.assertEqual(nt_tree.left.value, 2)
        self.assertEqual(nt_tree.right.value, 4)
        self.assertIsNone(gen_bin_tree_namedtuple(height=0))

        # 2. defaultdict
        dd_tree = gen_bin_tree_defaultdict(root=1, height=2)
        self.assertEqual(dd_tree["left"]["value"], 2)
        self.assertIsNone(dd_tree["left"]["left"])  # Свойство defaultdict

        # 3. UserDict
        ud_tree = gen_bin_tree_userdict(root=1, height=2)
        self.assertIsNotNone(ud_tree)
        self.assertEqual(ud_tree["right"]["value"], 4)
        self.assertIsNone(gen_bin_tree_userdict(height=0))

        # 4. dataclass
        dc_tree = gen_bin_tree_dataclass(root=1, height=2)
        self.assertIsNotNone(dc_tree)
        self.assertEqual(dc_tree.left.value, 2)
        self.assertIsNone(gen_bin_tree_dataclass(height=0))


if __name__ == "__main__":
    unittest.main()