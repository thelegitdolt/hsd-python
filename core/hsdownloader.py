card_source = 'https://static.firestoneapp.com/cards/enUS/512/id_here.png'
card_source_bg = 'https://static.firestoneapp.com/cards/bgs/enUS/512/id_here.png'


def site_from_id(id, battlegrounds=False):
    return (card_source_bg if battlegrounds else card_source).replace('id_here', id)

output_path = 'outputs/cards'
read_json_path = 'inputs/hearthstone.json'
