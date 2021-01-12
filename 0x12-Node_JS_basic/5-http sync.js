const http = require('http');
const fs = require('fs');

function countStudents(path, res) {
  let datos;
  try {
    datos = fs.readFileSync(path, 'utf8').split('\n');

  datos = datos.slice(1, datos.length - 1);
  res.write('This is the list of our students\n');
  res.write(`Number of students: ${datos.length}\n`);
  const dict = {};
  for (const row of datos) {
    if (!dict[row.split(',')[3]]) dict[row.split(',')[3]] = [];
    dict[row.split(',')[3]].push(row.split(',')[0]);
  }
  for (const row in dict) {
    if (row) res.write(`Number of students in ${row}: ${dict[row].length}. List: ${dict[row].join(', ')}\n`);
  }
} catch (err) {
    res.write('Cannot load the database');
  }
}

const app = http.createServer(
  (req, res) => {

    switch (req.url) {
        case '/':
            res.write('Hello Holberton School!');
            break;
        case '/students':
            //res.write('<p>This is the list of our students</p>');
            // read file
            countStudents(process.argv[2], res);
            break;
        default:
            break;
    }
    
    res.end();
  },
).listen(1245);

module.exports = app;
