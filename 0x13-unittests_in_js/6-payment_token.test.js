const expect = require('chai').expect;
const getPaymentTokenFromAPI = require('./6-payment_token.js');
    
describe('getPaymentTokenFromAPI function', function() {

it('async testing Promise', function(done) {

    getPaymentTokenFromAPI(true)
      .then((res) => {
        expect(res).to.eql({ data: 'Successful response from the API' })
      });
      done();
  });
});
