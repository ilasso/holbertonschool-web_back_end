const constants = require('./0-constants.js')

test('task1', () => {
	expect(constants.taskFirst() + ' ' + constants.taskNext()).toBe('I prefer const when I can. But sometimes let is okay');
		});
