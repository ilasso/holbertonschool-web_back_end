const expect = require('chai').expect;
const sinon = require('sinon');

const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./4-payment.js');

describe('sendPaymentRequestToApi function', () => {
  const consSpy = sinon.spy(console, 'log');

  it('validate the usage of the Utils function', () => {
    const utilStub = sinon.stub(Utils, 'calculateNumber');
    utilStub.withArgs('SUM', 100, 20).returns(10);

    sendPaymentRequestToApi(100, 20);
    expect(consSpy.calledOnce).to.be.true;
    expect(consSpy.calledWith('The total is: 10')).to.be.true;
    utilStub.restore();
    consSpy.restore();
  });
});
