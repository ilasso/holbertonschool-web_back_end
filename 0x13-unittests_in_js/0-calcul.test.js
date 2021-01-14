var assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
    it('checks the output', () => {
      assert.equal(calculateNumber(1.1, 2.5), 4);
      assert.equal(calculateNumber(0.0, 0), 0);
      assert.equal(calculateNumber(1.9, 0), 2);
      assert.equal(calculateNumber(0, 1.9), 2);
      assert.strictEqual(calculateNumber(4, 8), 12);
    assert.strictEqual(calculateNumber(1.9, 0), 2);
    assert.strictEqual(calculateNumber(6.1, 6.1), 12);
    assert.strictEqual(calculateNumber(0.1, 0.2), 0);
    assert.strictEqual(calculateNumber(0.1, 0.6), 1);
    });
    it('negative numbers', () => {
      assert.equal(calculateNumber(-1, 1), 0);
      assert.equal(calculateNumber(-1.5, 0), -1);
    });
    it('checks arguments', () => {
      assert.equal(isNaN(calculateNumber(2.2)), true);
      assert.equal(isNaN(calculateNumber()), true);
      assert.strictEqual(calculateNumber(-1, -3), -4);
    assert.strictEqual(calculateNumber(-1.4, -3.6), -5);
    });
  });
  