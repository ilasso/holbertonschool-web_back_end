const expect = require('chai').expect;
const request = require('request');

describe('express app GET / req', function () {
  it('/ correct status, result', function(done) {

    request('http://localhost:7865',(err, res, body) => {
        if (res) {
            expect(res.statusCode).to.equal(200);
            expect(res.statusMessage).to.equal('OK');
            expect(body).to.equals('Welcome to the payment system');
          };
    });
    done();
  });
});
