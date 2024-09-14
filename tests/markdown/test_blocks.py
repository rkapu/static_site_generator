import unittest
import textwrap

from src.markdown.blocks import *

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = textwrap.dedent("""\
        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.



        * This is the first list item in a list block
        * This is a list item
        * This is another list item


        """)
        expected_result = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]

        self.assertEqual(expected_result, markdown_to_blocks(markdown))

if __name__ == "__main__":
    unittest.main()
