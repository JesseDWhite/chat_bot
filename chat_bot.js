const spawner = require('child_process').spawn;

const prompt = process.argv.slice(2).join(', ');

const python_process = spawner('python', ['./chat_bot.py', prompt]);

python_process.stdout.on('data', (data) => {
  console.log(data.toString());
});