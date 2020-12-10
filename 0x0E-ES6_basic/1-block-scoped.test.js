import taskBlock from './1-block-scoped.js'

test('case 1: true', () => {
	expect(taskBlock(true)).toEqual([false, true]);
		});
test('case 2: false ', () => {
	expect(taskBlock(false)).toEqual([false, true]);
		});
