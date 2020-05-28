from recipe_parser.helper import find_order, text_to_number, improve_fractions
import json
import re

def parse_instructions(texts, blocks):

    """
    if google api detects several blocks of text those will be returned individually.
    if only one block of text is detected find_order() will be applied
    to the text.
    """

    if len(blocks.pages[0].blocks) < 2:

        recipe = texts[0].description

        recipe = improve_fractions(recipe)

        recipe = re.sub('[^A-Za-z0-9 ,;.:/-?!""]+', '', recipe)

        recipe = text_to_number(recipe, texts)

        instructions_dict = find_order(recipe)

        return json.dumps(instructions_dict)


    else:

        all_blocks = ""

        for a in range(len(blocks.pages[0].blocks)):

            all_blocks = all_blocks + "new block"

            for b in range(len(blocks.pages[0].blocks[a].paragraphs)):

                for c in range(len(blocks.pages[0].blocks[a].paragraphs[b].words)):

                    all_blocks = all_blocks + " "
                    for d in range(len(blocks.pages[0].blocks[a].paragraphs[b].words[c].symbols)):

                        all_blocks = all_blocks + blocks.pages[0].blocks[a].paragraphs[b].words[c].symbols[d].text

        blocks_splitted = all_blocks.split("new block")[1:]

        instructions_dict =  {"instructions": blocks_splitted}

        return json.dumps(instructions_dict)