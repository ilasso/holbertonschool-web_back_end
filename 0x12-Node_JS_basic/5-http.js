const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(
  (req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    switch (req.url) {
      case '/':
        res.write('Hello Holberton School!');
        res.end();
        break;
      case '/students':
        // read file
        countStudents(process.argv[2])
          .then(
            (dict) => {
              res.write('This is the list of our students\n');
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
        break;
      default:
        res.end();
        break;
    }
  },
).listen(1245);

module.exports = app;
