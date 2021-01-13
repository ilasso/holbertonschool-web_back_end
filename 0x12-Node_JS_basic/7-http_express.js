const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
  res.end();
});

app.get('/students', (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.write('This is the list of our students\n');
  countStudents(process.argv[2])
    .then(
      (dict) => {
        let numofstudents = 0;
        for (const row in dict) {
          if (row) numofstudents += dict[row].length;
        }
        res.write(`Number of students: ${numofstudents}\n`);
        for (const row in dict) {
          if (row) res.write(`Number of students in ${row}: ${dict[row].length}. List: ${dict[row].join(', ')}\n`);
        }
        res.end();
      },
    )
    .catch((error) => {
      res.end(error.message);
    });
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});

module.exports = app;
