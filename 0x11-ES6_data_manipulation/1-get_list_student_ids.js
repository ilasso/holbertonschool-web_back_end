export default function getListStudentIds(arrayobj) {
  if (!Array.isArray(arrayobj)) {
    return [];
  }
  return arrayobj.map((studentid) => studentid.id);
}
