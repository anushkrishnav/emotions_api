import { fetch } from 'wix-fetch';

export function updateEmotion() {
  let emotion = 0;
  let user
  let url = "https://emot-api.azurewebsites.net/score";
  return fetch('https://emot-api.azurewebsites.net/score', {
  'method': 'post',
  'headers': {
    'Content-Type': 'application/\json'
  },
  'body': JSON.stringify({ 
    "user": "Tia",
    "link": "https://static.videezy.com/system/resources/previews/000/009/169/original/Young_hispanic_woman_upset_angry_emotional_2.mp4",
})
}
  )
  .then(response => response.json())
  .then(data => {
    emotion = data.score;
    return emotion;
  }
  )

}
