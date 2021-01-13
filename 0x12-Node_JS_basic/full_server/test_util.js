const readDatabase = require('./utils');

readDatabase('database.csv')
  .then((res) => {
    console.log(res);
    console.log('Done!');
  })
  .catch((error) => {
    console.log(error);
  });
