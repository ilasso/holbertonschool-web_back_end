import getNeighborhoodsList from './2-arrow.js'

const neighborhoodsList = new getNeighborhoodsList();
const res = neighborhoodsList.addNeighborhood('Noe Valley');

test('case 1', () => {
	expect(res).toEqual([ 'SOMA', 'Union Square', 'Noe Valley' ]);
		});
