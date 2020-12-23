export default function getListStudentIds(arrayobj) {
  return arrayobj.reduce((suma, students) => suma + students.id, 0);
}
