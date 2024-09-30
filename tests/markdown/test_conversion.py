import unittest
import textwrap

from src.markdown.block import *
from src.markdown.conversion import *
from tests.helpers import *

class TestConversion(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = textwrap.dedent("""\
        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.



        * This is the first list item in a list block
        * This is a list item
        * This is another list item


        """)
        expected_result = [
            Block("# This is a heading"),
            Block("This is a paragraph of text. It has some **bold** and *italic* words inside of it."),
            Block("* This is the first list item in a list block\n* This is a list item\n* This is another list item")
        ]

        self.assertListEqual(expected_result, markdown_to_blocks(markdown))

    def test_markdown_to_html(self):
        markdown = textwrap.dedent("""\
        # This is a heading 1

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        ## This is heading 2

        * This is the first list item in a list block
        * This is a list item
        * This is another list item

        1. first item
        2. second *item*
        3. third **item**

        ```
        def some_func():
            print("Hello world")
        ```

        > This is a quote

        This is the end

        ###### Heading 6

        ####### Heading 7

        """)
        expected_title = "This is a heading 1"
        expected_html = "<div><h1>This is a heading 1</h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><h2>This is heading 2</h2><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul><ol><li>first item</li><li>second <i>item</i></li><li>third <b>item</b></li></ol><pre><code>\ndef some_func():\n    print(\"Hello world\")\n</code></pre><blockquote>This is a quote</blockquote><p>This is the end</p><h6>Heading 6</h6><p>####### Heading 7</p></div>"

        self.assertEqual((expected_title, expected_html), markdown_to_html(markdown))


    def test_missing_title(self):
        markdown = textwrap.dedent("""\
        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        ## This is heading 2

        * This is the first list item in a list block
        * This is a list item
        * This is another list item

        ####### Heading 7

        """)

        with self.assertRaises(ValueError) as e:
            markdown_to_html(markdown)
        self.assertEqual("No title found in the list of markdown blocks", str(e.exception))

if __name__ == "__main__":
    unittest.main()
