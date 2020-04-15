import nexmo
from pprint import pprint

client = nexmo.Client(
  application_id='1b137924-cc7b-41fa-b446-0fc79eac57bf',
  private_key='PATH_TO_PRIVATE_KEY',
)

ncco = [
  {
    'action': 'talk',
    'voiceName': 'Laila',
    'text': 'تبا لك نحن الانونويموس ولقد اتينا لكي نخبرك بما سيحدث عن قريب ستتلقى درسا جيدا قد ينسيك هذا المجال 
ام اكس تي'
  }
]

response = client.create_call({
  'to': [{
    'type': 'phone',
    'number': '963955239678'
  }],
  'from': {
    'type': 'phone',
    'number': '17622131531'
  },
  'ncco': ncco
})

pprint(response)