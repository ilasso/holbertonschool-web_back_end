const expect = require('chai').expect;
const sinon = require('sinon');
const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./5-payment.js');

describe('sendPaymentRequestToApi function', function() {
    let consSpy;
    beforeEach(function() {
        consSpy = sinon.spy(console, 'log')
    });

    it('sendPaymentRequestToAPI(100, 20)', function() {
        sendPaymentRequestToApi(100, 20);
        expect(consSpy.calledOnce).to.be.true;
        expect(consSpy.calledWith('The total is: 120')).to.be.true;
      });
      
    it('sendPaymentRequestToAPI(10, 10)', function() {
    sendPaymentRequestToApi(10, 10);
    expect(consSpy.calledOnce).to.be.true;
    expect(consSpy.calledWith('The total is: 20')).to.be.true;
    });
    

    afterEach(function(){
        consSpy.restore();
    });

});