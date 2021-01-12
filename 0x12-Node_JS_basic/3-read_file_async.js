/* Using the database database.csv (provided in project description),
create a function countStudents in the file 2-read_file.js

Create a function named countStudents. It should accept a path in argument
The script should attempt to read the database file synchronously
If the database is not available, it should throw an error with the text Cannot load the database
If the database is available, it should log the following message to the console Number of students:
NUMBER_OF_STUDENTS
It should log the number of students in each field, and the list with the following format:
Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES
CSV file can contain empty lines (at the end) - and they are not a valid student! */

const fs = require('fs');

function countStudents(path) {
  return new Promise((res, rej) => {
    fs.readFile(path, 'utf8', (err, data) => {
      let datos;
      if (err) return rej(Error('Cannot load the database'));
      datos = data.split('\n');
      datos = datos.slice(1, datos.length - 1);
      console.log(`Number of students: ${datos.length}`);
      const dict = {};
      for (const row of datos) {
        if (!dict[row.split(',')[3]]) dict[row.split(',')[3]] = [];
        dict[row.split(',')[3]].push(row.split(',')[0]);
      }
      for (const row in dict) {
        if (row) console.log(`Number of students in ${row}: ${dict[row].length}. List: ${dict[row].join(', ')}`);
      }
      return res();
    });
  });
}

module.exports = countStudents;
