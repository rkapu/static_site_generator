import unittest
import textwrap

from src.markdown.blocks import *
from tests.helpers import assert_all_cases

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

    def test_block_to_block_type(self):
        test_cases = [
            # Heading
            ["# Heading", BlockType.HEADING],
            ["## Heading", BlockType.HEADING],
            ["### Heading", BlockType.HEADING],
            ["#### Heading", BlockType.HEADING],
            ["##### Heading", BlockType.HEADING],
            ["###### Heading", BlockType.HEADING],
            ["#heading", BlockType.PARAGRAPH],
            ["####### Heading", BlockType.PARAGRAPH],
            ["heading", BlockType.PARAGRAPH],
            ["heading#", BlockType.PARAGRAPH],

            # Code
            ["```ruby\n return 'something'\n```", BlockType.CODE],
            ["```a code sample```", BlockType.PARAGRAPH],
            ["`code`", BlockType.PARAGRAPH],
            ["``code``", BlockType.PARAGRAPH],
            ["```code", BlockType.PARAGRAPH],
            ["code```", BlockType.PARAGRAPH],
            ["```", BlockType.PARAGRAPH],
            ["``````", BlockType.PARAGRAPH],

            # Quote
            [">quote", BlockType.QUOTE],
            ["> quote", BlockType.QUOTE],
            [">         quote", BlockType.QUOTE],
            [">> quote", BlockType.QUOTE],
            [">\n>quote", BlockType.QUOTE],
            [">\nquote", BlockType.PARAGRAPH],
            ["quote", BlockType.PARAGRAPH],

            # Unordered list
            ["* item", BlockType.UNORDERED_LIST],
            ["- item", BlockType.UNORDERED_LIST],
            ["* \n* item\n* item", BlockType.UNORDERED_LIST],
            ["- \n- item\n- item", BlockType.UNORDERED_LIST],
            ["*item", BlockType.PARAGRAPH],
            ["-item", BlockType.PARAGRAPH],
            ["*item*", BlockType.PARAGRAPH],
            ["* item\n- item", BlockType.PARAGRAPH],

            # Ordered list
            ["1. item", BlockType.ORDERED_LIST],
            ["1. item\n2. item\n3. item", BlockType.ORDERED_LIST],
            ["1item", BlockType.PARAGRAPH],
            ["1 item", BlockType.PARAGRAPH],
            ["2. item", BlockType.PARAGRAPH],
            ["1. item\n3. item\n4. item", BlockType.PARAGRAPH],

            # Paragraph
            ["*This* is just a paragraph\n#paragraph", BlockType.PARAGRAPH]
        ]

        assert_all_cases(self, test_cases, block_to_block_type)

if __name__ == "__main__":
    unittest.main()
