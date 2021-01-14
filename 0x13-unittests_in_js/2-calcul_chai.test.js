const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai.js');
  
  
describe('calculateNumber type == SUM', () => {
  it('checks the output', () => {
    const answer = calculateNumber('SUM', 1.1, 2.5);
    expect(answer).to.equal(4);
    expect(calculateNumber('SUM', 0.0, 0)).to.equal(0);
  });
  it('negative numbers', () => {
    expect(calculateNumber('SUM', -1, 1), 'negative').to.equal(0);
    expect(calculateNumber('SUM', -1.5, 0)).to.equal(-1);
  });
  it('checks arguments', () => {
    expect(isNaN(calculateNumber('SUM', 2.2))).to.equal(true);
    expect(isNaN(calculateNumber(2.2, 2.2))).to.equal(true);
    expect(isNaN(calculateNumber(2.2))).to.equal(true);
    expect(isNaN(calculateNumber())).to.equal(true);
  });
});

describe('calculateNumber type == SUBSTRACT', () => {
  it('checks the output', () => {
    expect(calculateNumber('SUBSTRACT', 3.1, 2.5), 0).to.equal;
    expect(calculateNumber('SUBSTRACT', 0.0, 5), -5).to.equal;
  });
  it('negative numbers', () => {
    expect(calculateNumber('SUBSTRACT', -1, 1), -2).to.equal;
    expect(calculateNumber('SUBSTRACT', -1.5, 0), -1).to.equal;
  });
  it('checks arguments', () => {
    expect(isNaN(calculateNumber('SUBSTRACT', 2.2)), true).to.equal;
    expect(isNaN(calculateNumber(2.2, 2.2)), true).to.equal;
    expect(isNaN(calculateNumber(2.2)), true).to.equal;
    expect(isNaN(calculateNumber()), true).to.equal;
  });
});
describe('calculateNumber type == DIVIDE', () => {
  it('check the output', () => {
    expect(calculateNumber('DIVIDE', 2, 2.5), 0.6666666666666666).to.equal;
    expect(calculateNumber('DIVIDE', 0.0, 2), 0).to.equal;
  });
  it('check negative numbers', () => {
    expect(calculateNumber('DIVIDE', -1, 1), -1).to.equal;
  });
  it('check second argument is 0', () => {
    expect(calculateNumber('DIVIDE', 2.2, 0), 'Error').to.equal;
  });
  it('check arguments', () => {
    expect(isNaN(calculateNumber('DIVIDE', 2.2)), true).to.equal;
    expect(isNaN(calculateNumber('DIVIDE')), true).to.equal;
    expect(isNaN(calculateNumber(2.2, 2.2)), true).to.equal;
    expect(isNaN(calculateNumber(2.2)), true).to.equal;
    expect(isNaN(calculateNumber()), true).to.equal;
  });
});

describe('SUM', () => {
    it('returns rounded positive sum', () => {
      expect(calculateNumber('SUM', 4, 8)).to.equal(12);
      expect(calculateNumber('SUM', 1.9, 0)).to.equal(2);
      expect(calculateNumber('SUM', 6.1, 6.1)).to.equal(12);
      expect(calculateNumber('SUM', 0.1, 0.2)).to.equal(0);
      expect(calculateNumber('SUM', 0.1, 0.6)).to.equal(1);
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
  
    it('returns rounded negative sum', () => {
      expect(calculateNumber('SUM', -1, -3)).to.equal(-4);
      expect(calculateNumber('SUM', -1.4, -3.6)).to.equal(-5);
    });
  
    });
  
  describe('SUBTRACT', () => {
    it('returns rounded positive substract', () => {
      expect(calculateNumber('SUBTRACT', 8, 4)).to.equal(4);
      expect(calculateNumber('SUBTRACT', 1.9, 0)).to.equal(2);
      expect(calculateNumber('SUBTRACT', 6.1, 6.1)).to.equal(0);
      expect(calculateNumber('SUBTRACT', 1, 0.2)).to.equal(1);
      expect(calculateNumber('SUBTRACT', 0.6, 0.1)).to.equal(1);
      expect(calculateNumber('SUBTRACT', 4.5, 1.4)).to.equal(4);
    });
  
    it('returns rounded negative substract', () => {
      expect(calculateNumber('SUBTRACT', -1, -3), 2);
      expect(calculateNumber('SUBTRACT', -1.4, -3.6), 3);
    });
  
  });
  
  describe('DIVIDE', () => {
    it('returns rounded positive divide', () => {
      expect(calculateNumber('DIVIDE', 8, 4), 2);
      expect(calculateNumber('DIVIDE', 6.1, 1.7), 3);
      expect(calculateNumber('DIVIDE', 6.1, 6.1), 1);
      expect(calculateNumber('DIVIDE', 2.0, 1.1), 2);
      expect(calculateNumber('DIVIDE', 0.6, 0.9), 1);
      expect(calculateNumber('DIVIDE', 4.5, 5), 1);
    });
  
    it('returns rounded negative divide', () => {
      expect(calculateNumber('DIVIDE', -2, 1.1), -2);
      expect(calculateNumber('DIVIDE', -4.4, -2.2), 2);
    });
  
    it('returns Error', () => {
      expect(calculateNumber('DIVIDE', 2, 0), 'Error');
      expect(calculateNumber('DIVIDE', 3, 0), 'Error');
      expect(calculateNumber('DIVIDE', 4, 0), 'Error');
    });
  
  });

  describe('calculateNumber', function () {
    describe('SUM no Round', function () {
      it('should return 5', function () {
        expect(calculateNumber('SUM', 1, 4)).to.equal(5);
      });
    });
  
    describe('SUM first round', function () {
      it('should return 6', function () {
        expect(calculateNumber('SUM', 2.4, 4)).to.equal(6);
      });
    });
  
    describe('SUM second round ', function () {
      it('should return 6', function () {
        expect(calculateNumber('SUM', 4, 2.4)).to.equal(6);
      });
    });
  
    describe('SUM both round', function () {
      it('should return 6', function () {
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
      });
    });
  
    describe('SUBTRACT no round', function () {
      it('should return 2', function () {
        expect(calculateNumber('SUBTRACT', 5, 3)).to.equal(2);
      });
    });
  
    describe('SUBTRACT first round', function () {
      it('should return -3', function () {
        expect(calculateNumber('SUBTRACT', 2, 4.5)).to.equal(-3);
      });
    });
  
    describe('SUBTRACT second round', function () {
      it('should return 3', function () {
        expect(calculateNumber('SUBTRACT', 4.5, 2)).to.equal(3);
      });
    });
  
    describe('SUBTRACT both round', function () {
      it('should return -4', function () {
        expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
      });
    });
  
    describe('DIVIDE no round', function () {
      it('should return 2', function () {
        expect(calculateNumber('DIVIDE', 8, 4)).to.equal(2);
      });
    });
  
    describe('DIVIDE first round', function () {
      it('should return 5', function () {
        expect(calculateNumber('DIVIDE', 9.5, 2)).to.equal(5);
      });
    });
  
    describe('DIVIDE second round', function () {
      it('should return 0.2', function () {
        expect(calculateNumber('DIVIDE', 2, 9.5)).to.equal(0.2);
      });
    });
  
    describe('DIVIDE both round', function () {
      it('should return 0.2', function () {
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
      });
    });
  
    describe('DIVIDE Error', function () {
      it('should return Error', function () {
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
      });
    });
  });