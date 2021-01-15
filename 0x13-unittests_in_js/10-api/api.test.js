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

describe('GET /cart/:id', () => {
  it('correct status, result', function(done) {
    request('http://localhost:7865/cart/12',(err, res, body)=> {
      if (res) {
        expect(res.statusCode).to.equal(200);
        expect(res.statusMessage).to.equal('OK');
        expect(res.body).to.equal('Payment methods for cart 12');
        done();
      };
      });
      
  })
  it('correct status if id isNaN', function(done) {
    request('http://localhost:7865/cart/twelve', (err, res, body) => {
      if (res) {
        expect(res.statusCode).to.equal(404);
        done();
      };
      });

  });
});


describe('GET /available_payments', function(done) {
  it('request /available_payments', (done) => {
    request('http://localhost:7865/available_payments', (error, response, body) => {
      if (response) {
        expect(response.statusCode).to.equal(200);
        expect(JSON.parse(body)).to.eql({ payment_methods: { credit_cards: true, paypal: false } });
        done();
      }
    });
  });
});

describe('POST /login', () => {
  it('request /login success', (done) => {
    request.post({ uri: 'http://localhost:7865/login', method: 'POST', json: { userName: "Betty" } }, (error, response, body) => {
      if (response) {
        expect(response.statusCode).to.equal(200);
        expect(body).equals("Welcome Betty")
        done();
      }
    });
  });
});



