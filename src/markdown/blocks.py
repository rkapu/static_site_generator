def markdown_to_blocks(markdown):
    return list(
        filter(
            None,
            map(
                lambda x: x.strip(),
                markdown.split("\n\n")
            )
        )
    )
