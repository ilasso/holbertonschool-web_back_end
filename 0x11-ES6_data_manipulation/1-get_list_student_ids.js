export default function getListStudentIds(arrayobj) {
  if (typeof (arrayobj) !== 'object') {
    return [];
  }
  return arrayobj.map((studentid) => studentid.id);
}
