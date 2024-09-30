import unittest

from src.markdown.block import *
from tests.helpers import assert_all_cases

class TestBlocks(unittest.TestCase):
    def test_block_type(self):
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

        assert_all_cases(self, test_cases, lambda x: Block(x).type)

if __name__ == "__main__":
    unittest.main()
