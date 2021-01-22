import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('error', function(error) {
  if (error)
    console.log(`Redis client not connected to the server: ${error}`);
});

client.on('ready', function(){
    console.log('Redis client connected to the server');
});

client.set('foo', 'bar', function(err,res){
    redis.print(`Replay: ${res}`);
});


client.get('foo', function(err, replay){
    console.log(`con callback=${replay}`);
});

// We expect a value 'foo': 'bar' to be present
// So instead of writing client.get('foo', cb); you have to write:
getAsync('foo').then(function(res) {
    console.log(`con promisify=${res}`); // => 'bar'
});

(async function myFunc () {
    const res = await getAsync('foo');
    console.log(`con async/await=${res}`); // => 'bar'
})();

// sin inmmediate ejecucion myFunc();

getAsync.then(console.log).catch(console.err);