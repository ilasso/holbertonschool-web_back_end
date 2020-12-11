export default function appendToEachArrayValue(array, appendString) {
  let idx;
  const otharray = [];
  for (const value of array) {
    idx = array.indexOf(value);
    otharray[idx] = appendString + value;
  }

  return otharray;
}
