export default function getStudentsByLocation(arrayobj, city) {
  return arrayobj.filter((locations) => locations.location === city);
}
