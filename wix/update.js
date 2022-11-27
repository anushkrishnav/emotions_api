import { updateEmotion } from 'backend/emotions.js'

let data = updateEmotion();
let user = data.user;
let score = data.anger;

$w('#table1').updateRow(0, {
  "Name": user,
  "Score": score
});